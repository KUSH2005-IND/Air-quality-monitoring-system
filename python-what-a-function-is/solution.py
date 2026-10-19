def is_even(n: int) -> bool:
    """
    Return True if n is even, False otherwise.
    """
    b=n%2==0
    return b


def greet_formal(name: str, title: str) -> str:
    """
    Return a greeting string in the exact form:
      "Good day, {title} {name}."
    Example: greet_formal("Smith", "Dr.") -> "Good day, Dr. Smith."
    """
    greetings= f"Good day, {title} {name}."
    return greetings


def apply_twice(func, value):
    """
    Call `func` on `value`, then call `func` again on the result
    of that first call. Return the final result.
    Example: apply_twice(lambda x: x + 1, 5) -> 7
    """
    return func(func(value))
