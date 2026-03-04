/**
 * Token-bucket rate limiter with configurable limits per API backend.
 *
 * Each backend gets its own bucket. When a request is made, the limiter
 * checks if there are tokens available. If not, it waits until a token
 * is replenished. Tokens are added at a steady rate (capacity / interval).
 */

export interface RateLimiterConfig {
  /** Maximum tokens (burst capacity) */
  maxTokens: number;
  /** Refill rate: tokens added per second */
  refillRate: number;
}

/** Per-backend rate-limit presets (requests per second). */
export const BACKEND_LIMITS: Record<string, RateLimiterConfig> = {
  rechtspraak: { maxTokens: 5, refillRate: 5 },
  openRechtspraak: { maxTokens: 10, refillRate: 10 },
  koopSru: { maxTokens: 5, refillRate: 5 },
  kvk: { maxTokens: 3, refillRate: 3 },
  eurlex: { maxTokens: 2, refillRate: 2 },
  overheid: { maxTokens: 5, refillRate: 5 },
};

interface Bucket {
  tokens: number;
  lastRefill: number;
  config: RateLimiterConfig;
}

class RateLimiter {
  private buckets = new Map<string, Bucket>();

  /**
   * Acquire a token for the given backend. Resolves when the token is
   * available. If the bucket is empty the promise will delay until a
   * token has been replenished.
   */
  async acquire(backend: string): Promise<void> {
    const bucket = this.getOrCreate(backend);
    this.refill(bucket);

    if (bucket.tokens >= 1) {
      bucket.tokens -= 1;
      return;
    }

    // Wait for one token to be replenished
    const waitMs = ((1 - bucket.tokens) / bucket.config.refillRate) * 1000;
    await this.sleep(waitMs);
    this.refill(bucket);
    bucket.tokens = Math.max(0, bucket.tokens - 1);
  }

  private getOrCreate(backend: string): Bucket {
    let bucket = this.buckets.get(backend);
    if (!bucket) {
      const config = BACKEND_LIMITS[backend] ?? { maxTokens: 5, refillRate: 5 };
      bucket = {
        tokens: config.maxTokens,
        lastRefill: Date.now(),
        config,
      };
      this.buckets.set(backend, bucket);
    }
    return bucket;
  }

  private refill(bucket: Bucket): void {
    const now = Date.now();
    const elapsed = (now - bucket.lastRefill) / 1000;
    bucket.tokens = Math.min(
      bucket.config.maxTokens,
      bucket.tokens + elapsed * bucket.config.refillRate,
    );
    bucket.lastRefill = now;
  }

  private sleep(ms: number): Promise<void> {
    return new Promise((resolve) => setTimeout(resolve, Math.ceil(ms)));
  }
}

/** Singleton rate-limiter shared across all clients. */
export const rateLimiter = new RateLimiter();
