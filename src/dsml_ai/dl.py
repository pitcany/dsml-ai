"""
Deep learning utilities and wrappers.
"""

__all__ = ["relu", "softmax"]

import numpy as np

def relu(x: np.ndarray) -> np.ndarray:
    """Apply the ReLU activation element-wise."""
    return np.maximum(0, x)

def softmax(x: np.ndarray) -> np.ndarray:
    """Compute the softmax of the input array along the last axis."""
    exp_shifted = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_shifted / np.sum(exp_shifted, axis=-1, keepdims=True)
