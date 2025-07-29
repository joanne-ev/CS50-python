from plates import is_valid

### Plates must have a maximum of six and a minimum of two characters ###
def test_len():
    assert is_valid('a') == False
    assert is_valid('abcdefg') == False
    assert is_valid('ab') == True
    assert is_valid('abcdef') == True


### Plates must start with at least two letters ###
def test_start_alpha():
    assert is_valid('1abcd') == False
    assert is_valid('12abc') == False
    assert is_valid('abcde') == True


### Plates must not have periods, spaces, or punctuation marks ###
def test_alphanum():
    assert is_valid('   abc') == False
    assert is_valid('abc!!!') == False
    assert is_valid('abc.d') == False
    assert is_valid('abcde') == True


## Plates cannot be used in the middle of a plate (they must come at the end) ###
def test_mid_num():
    assert is_valid('ab12cd') == False
    assert is_valid('12ab') == False
    assert is_valid('ab12') == True


### Plates cannot have zero as the leading number ###
def test_zero_check():
    assert is_valid('0ab') == False
    assert is_valid('ab0') == False
    assert is_valid('ab10') == True
