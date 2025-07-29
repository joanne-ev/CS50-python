from fuel import convert, gauge

def test_string():
    assert convert('3/4') == 0.75
    assert convert('2/4') == 0.5
    assert convert('cat/4') == "ValueError: A number was not entered"
    assert convert('3/cat') == "ValueError: A number was not entered"

def test_zero_denominator():
    assert convert('2/6') == 0.33
    assert convert('2/0') == 'ZeroDivisionError: Denomenator cannot be zero'
    assert convert('0/4') == 0.00


def test_improper_fraction():
    assert convert('6/4') == "ValueError: Improper fractions are not accepted"
    assert convert('8/4') == "ValueError: Improper fractions are not accepted"


def test_full():
    assert gauge(0.99) == 'F'
    assert gauge(0.99999) == 'F'
    assert gauge(1) == 'F'
    assert gauge(0.98) == '98%'


def test_empty():
    assert gauge(0.001) == 'E'
    assert gauge(0.1) == 'E'
    assert gauge(0) == 'E'
    assert gauge(0.11) == '11%'

