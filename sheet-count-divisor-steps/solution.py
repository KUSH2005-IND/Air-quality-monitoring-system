def count_divisor_steps(n: int) -> int:
    """Return how many times `count += 1` runs."""
    # TODO: write your solution here
    total=0
    i=1
    while i<=n:
        q=n//i
        j=n//q
        total+=q*(j-i+1)
        i=j+1
    return total
