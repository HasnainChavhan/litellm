"""
LiteLLM Redis Cache Hit-Rate & Latency Benchmark
Author: Hasnain Chavhan (@HasnainChavhan)
Description: Benchmarks response latency differences between cached and uncached LLM completion requests.
"""

import time
from typing import Dict, Any

def benchmark_cache_latency(uncached_latency_ms: float, cached_latency_ms: float) -> Dict[str, Any]:
    speedup = round(uncached_latency_ms / cached_latency_ms, 2) if cached_latency_ms > 0 else 1.0
    return {
        "uncached_ms": uncached_latency_ms,
        "cached_ms": cached_latency_ms,
        "speedup_factor": f"{speedup}x",
        "cache_saving_pct": f"{round((1 - cached_latency_ms / uncached_latency_ms) * 100, 1)}%"
    }
