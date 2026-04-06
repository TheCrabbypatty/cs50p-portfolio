import pytest
from jar import Jar


def test_init():
    with pytest.raises(ValueError):
        Jar(-5)
    with pytest.raises(ValueError):
        Jar("cat")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(10)
    with pytest.raises(ValueError):
        jar.deposit("cat")


def test_withdraw():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.withdraw(14)
    with pytest.raises(ValueError):
        jar.withdraw("cat")