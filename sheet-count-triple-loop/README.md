# Three Nested Loops

Intermediate | dsa-sheet | basics | counting-steps

This code has three loops that each start where the previous one is:

```python
count = 0
for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            count += 1
```

Implement `count_triple_loop(n)` so it returns the final value of `count`.

### Examples

**Example 1**

Input:

```python
count_triple_loop(3)
```

Output:

```text
10
```

The triples are (0,0,0) (0,0,1) (0,0,2) (0,1,1) (0,1,2) (0,2,2) (1,1,1) (1,1,2) (1,2,2) (2,2,2).

**Example 2**

Input:

```python
count_triple_loop(5)
```

Output:

```text
35
```

### Constraints

- `0 <= n <= 10**6`
