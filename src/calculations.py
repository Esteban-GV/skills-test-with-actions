# System Modules
import math

import pytest

# Installed Modules
# - None


def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def get_nth_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n < 0:
        raise ValueError("n cannot be negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
        
def test_fibonacci_negative():
    """Test that negative input raises ValueError."""
    with pytest.raises(ValueError, match="n cannot be negative"):
        get_nth_fibonacci(-1)

def test_fibonacci_zero():
    """Test that fibonacci(0) returns 0."""
    assert get_nth_fibonacci(0) == 0