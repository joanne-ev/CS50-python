from bank import value


# `0` if that str starts with “hello”, `20` if that `str` starts with an “h” (but not “hello”), or `100` otherwise

def test_zero():
    assert value('hello!') == 0
    assert value('HELLO!') == 0
    assert value('Hello! How is it going?') == 0


def test_twenty():
    assert value('hi!') == 20
    assert value('HEY!') == 20
    assert value("He isn't going to say hi is he?") == 20


def test_hundred():
    assert value('MORNING!') == 100
    assert value('') == 100
    assert value("She said that costs $20") == 100
