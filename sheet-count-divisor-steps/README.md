# Divisor Loop

Advanced | dsa-sheet | basics | counting-steps

The inner loop jumps by `i` each time:

```python
count = 0
for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        count += 1
```

Implement `count_divisor_steps(n)` so it returns the final value of `count`.

Looping `i` from `1` to `n` is too slow for the largest inputs.

### Examples

**Example 1**

Input:

```python
count_divisor_steps(5)
```

Output:

```text
10
```

`5//1 + 5//2 + 5//3 + 5//4 + 5//5 = 5 + 2 + 1 + 1 + 1`.

**Example 2**

Input:

```python
count_divisor_steps(10)
```

Output:

```text
27
```

### Constraints

- `1 <= n <= 10**10`
- An answer that loops `n` times will time out on the large tests.
