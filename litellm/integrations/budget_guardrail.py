"""
LiteLLM Enterprise Cost Guardrail & Token Budget Enforcement
Author: Hasnain Chavhan (@HasnainChavhan)
Description: Automated request interceptor to prevent API budget overruns in production LLM gateways.
"""

from typing import Dict, Any

class LiteLLMBudgetGuardrail:
    def __init__(self, max_budget_usd: float = 100.0):
        self.max_budget_usd = max_budget_usd
        self.current_usage_usd = 0.0

    def validate_request(self, estimated_cost: float) -> bool:
        """Enforces token cost limits before forwarding completion requests to LLM APIs."""
        if self.current_usage_usd + estimated_cost > self.max_budget_usd:
            raise ValueError(
                f"[LiteLLM Guardrail] Budget Exceeded! Max limit: ${self.max_budget_usd}, "
                f"Current: ${self.current_usage_usd}, Request cost: ${estimated_cost}"
            )
        self.current_usage_usd += estimated_cost
        return True

    def reset_usage(self) -> None:
        self.current_usage_usd = 0.0
