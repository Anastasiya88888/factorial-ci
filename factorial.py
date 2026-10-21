def factorial(n: int) -> int:
    """Повертає n! для цілого невід'ємного числа n."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n):
        result *= i
    return result