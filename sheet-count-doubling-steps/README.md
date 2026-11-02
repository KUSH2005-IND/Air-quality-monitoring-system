# Doubling Steps

Beginner | dsa-sheet | basics | counting-steps

This loop doubles `i` until it reaches `n`:

```python
count = 0
i = 1
while i < n:
    i *= 2
    count += 1
```

Implement `count_doubling_steps(n)` so it returns the final value of `count`.

### Examples

**Example 1**

Input:

```python
count_doubling_steps(8)
```

Output:

```text
3
```

`i` goes 1, 2, 4, 8.

**Example 2**

Input:

```python
count_doubling_steps(9)
```

Output:

```text
4
```

`i` goes 1, 2, 4, 8, 16.

### Constraints

- `1 <= n <= 10**18`
