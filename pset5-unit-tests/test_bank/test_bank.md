# Back to the Bank 🏦

In a file called `bank.py`, reimplement [Home Federal Savings Bank](https://cs50.harvard.edu/python/2022/psets/1/bank/) from Problem Set 1, restructuring your code per the below, wherein `value` expects a `str` as input and returns an `int`, namely `0` if that `str` starts with “hello”, `20` if that `str` starts with an “h” (but not “hello”), or `100` otherwise, treating the `str` case-insensitively. You can assume that the string passed to the `value` function will not contain any leading spaces. Only `main` should call `print`.

```python
def main():
    ...


def value(greeting):
    ...


if __name__ == "__main__":
    main()
```

Then, in a file called `test_bank.py`, implement three or more functions that collectively test your implementation of `value` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```python
pytest test_bank.py
```
