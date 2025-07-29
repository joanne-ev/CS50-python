'''
In a file called `fuel.py`, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

- `convert` expects a `str` in `X/Y` format as input, wherein each of `X` and `Y` is an integer, and returns that fraction as a percentage rounded to the nearest `int` between `0` and `100`, inclusive. If `X` and/or `Y` is not an integer, or if `X` is greater than `Y`, then `convert` should raise a `ValueError`. If `Y` is `0`, then convert should raise a `ZeroDivisionError`.

- gauge expects an `int` and returns a `str` that is:
    - "E" if that `int` is less than or equal to `1`,
    - "F" if that `int` is greater than or equal to `99`,
    - and `"Z%"` otherwise, wherein `Z` is that same `int`.


def main():
    ...


def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()


Then, in a file called `test_fuel.py`, implement two or more functions that collectively test your implementations of convert and gauge thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

pytest test_fuel.py

'''
import sys

def main():
    fraction = input('Fraction: ')
    percentage = convert(fraction)
    print(percentage)
    fuel = gauge(percentage)
    print(fuel)


def convert(fraction):
    frac = fraction.split('/')

    try:
        division = round(int(frac[0]) / int(frac[1]), 2)

    # Handle ValueError for non-integer input
    except ValueError:
        return "ValueError: A number was not entered"
    
    # Handle ZeroDivisionError
    except ZeroDivisionError:
       return 'ZeroDivisionError: Denomenator cannot be zero'

    # Handle ValueError for improper fractions
    else:
        if division > 1:
            return "ValueError: Improper fractions are not accepted"
        else:
            return division


def gauge(percentage):
    if 0.99 <= percentage <= 1:
        gauge = 'F' # Full
    elif 0 <= percentage <= 0.1:
        gauge = 'E' # Empty
    else:
        gauge = (f'{int(round((percentage * 100), 0))}%')
    return gauge


if __name__ == "__main__":
    main()
