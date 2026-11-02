# Square Root Loop

Beginner | dsa-sheet | basics | counting-steps

This loop runs while `i * i` has not passed `n`:

```python
count = 0
i = 1
while i * i <= n:
    count += 1
    i += 1
```

Implement `count_square_loop(n)` so it returns the final value of `count`.

`n` can be as large as `10**18`, so you cannot run the loop.

### Examples

**Example 1**

Input:

```python
count_square_loop(10)
```

Output:

```text
3
```

`i = 1, 2, 3` run (3 * 3 = 9 <= 10); `i = 4` gives 16 > 10.

**Example 2**

Input:

```python
count_square_loop(16)
```

Output:

```text
4
```

`i = 1, 2, 3, 4` run.

### Constraints

- `0 <= n <= 10**18`
