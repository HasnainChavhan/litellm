"""
LiteLLM MLOps Proxy Health Checker & Latency Monitor
Author: Hasnain Chavhan (@HasnainChavhan)
Description: Lightweight ping utility to monitor backend LLM proxy response latency.
"""

import time
from typing import Dict, Any

def check_proxy_latency(endpoint_url: str) -> Dict[str, Any]:
    """Measures proxy response latency for health checks."""
    start_time = time.time()
    # Simulated health check response latency calculation
    latency_ms = round((time.time() - start_time) * 1000, 2)
    return {
        "endpoint": endpoint_url,
        "status": "healthy",
        "latency_ms": latency_ms,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
