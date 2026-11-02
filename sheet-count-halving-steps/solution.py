def count_halving_steps(n: int) -> int:
    """Return how many times the loop body runs."""
    # TODO: write your solution here
    return n.bit_length()-1
