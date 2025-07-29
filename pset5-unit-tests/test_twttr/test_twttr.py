from twttr import shorten

def test_lowercase():
    assert shorten('lol') == 'll'
    assert shorten('police') == 'plc'
    assert shorten('python') == 'pythn'


def test_uppercase():
    assert shorten('LOL') == 'LL'
    assert shorten('POLICE') == 'PLC'
    assert shorten('PYTHON') == 'PYTHN'


def test_both_cases():
    assert shorten('LoL') == 'LL'
    assert shorten('PolicE') == 'Plc'
    assert shorten('pYtHoN') == 'pYtHN'


def test_numbers():
    assert shorten('LoL1') == 'LL1'
    assert shorten('2PolicE') == '2Plc'
    assert shorten('3pYtHoN3') == '3pYtHN3'


def test_punctuation():
    assert shorten('LoL!!!') == 'LL!!!'
    assert shorten('##PolicE##') == '##Plc##'
    assert shorten('>>>pYtHoN') == '>>>pYtHN'
