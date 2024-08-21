from numb3rs import validate
def test_numbers():
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True
    assert validate("34.192.168.123") == True
    assert validate("1.275.3.4") == False
def test_other():
    assert validate("255.234") == False
    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("pizza") == False

