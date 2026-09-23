"""Core implementation of the extended Euclidean algorithm."""

from __future__ import annotations


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return `(gcd, x, y)` such that `a*x + b*y = gcd` for integers `a` and `b`.

    The coefficients `x` and `y` are the Bézout coefficients.  The
    function uses the iterative form of the extended Euclidean
    algorithm rather than recursion to avoid hitting Python's
    recursion limit for large inputs.

    The returned `gcd` is always non-negative, even for negative
    inputs.  This matches the convention used by Python's `math.gcd`.
    """

    if a == 0 and b == 0:
        # Both inputs are zero.  The greatest common divisor is
        # conventionally defined as zero in this case, and any pair
        # (x, y) satisfies the identity.  Returning (0, 0) keeps the
        # result deterministic and simple to reason about.
        return (0, 0, 0)

    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # Normalize the gcd to be non-negative.  If it is negative,
    # negate all three values so that the identity still holds.
    if old_r < 0:
        old_r = -old_r
        old_s = -old_s
        old_t = -old_t

    return (old_r, old_s, old_t)
