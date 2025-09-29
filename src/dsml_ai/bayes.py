"""
Bayesian modeling utilities.
"""

__all__ = ["beta_posterior", "expected_beta"]

def beta_posterior(
    alpha: float, beta: float, successes: int, failures: int
) -> tuple[float, float]:
    """Compute the posterior alpha and beta for a Beta prior given data."""
    return alpha + successes, beta + failures

def expected_beta(alpha: float, beta: float) -> float:
    """Return the expected value (mean) of a Beta distribution."""
    return alpha / (alpha + beta)
