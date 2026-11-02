# Halving Steps

Beginner | dsa-sheet | basics | counting-steps

This loop keeps halving `n`, rounding down:

```python
count = 0
while n > 1:
    n //= 2
    count += 1
```

Implement `count_halving_steps(n)` so it returns the final value of `count`.

### Examples

**Example 1**

Input:

```python
count_halving_steps(8)
```

Output:

```text
3
```

8 → 4 → 2 → 1 is 3 steps.

**Example 2**

Input:

```python
count_halving_steps(1000)
```

Output:

```text
9
```

1000 → 500 → 250 → 125 → 62 → 31 → 15 → 7 → 3 → 1 is 9 steps.

### Constraints

- `1 <= n <= 10**18`
