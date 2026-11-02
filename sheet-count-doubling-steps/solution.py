def count_doubling_steps(n: int) -> int:
    """Return how many times the loop body runs."""
    # TODO: write your solution here
    return (n-1).bit_length()
