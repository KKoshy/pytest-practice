"""
This file holds the practice on using pytest.RaisesExc
"""

import pytest
import logging

log = logging.getLogger(__name__)


def validate_age(value):
    if isinstance(value, int):
        if value<18:
            raise ValueError(f"Invalid age: {value}")
        else:
            return "OK"
    raise TypeError(f"Incorrect age value: {type(value)}")

def test_raises_exc_01():
    log.info("Validating Exception details of exception group with RaisesExc")
    with pytest.RaisesGroup(pytest.RaisesExc(ValueError, match="foo"), pytest.RaisesExc(TypeError, match="msg"), match="fin"):
        raise ExceptionGroup("fin", [ValueError("foo"), TypeError("msg")])
    

@pytest.mark.parametrize(argnames="age, expected", argvalues=[
    (12, pytest.RaisesExc(ValueError, match=r"Invalid age")), 
    (19, "OK"), 
    ("23", pytest.RaisesExc(TypeError, match=r"Incorrect age value"))
    ],
    ids=["underage", "adult", "wrong-type"]
    )
def test_raises_exc_02(age, expected):
    log.info(f"Validating for age: {age} of type {type(age)}")
    if isinstance(expected, pytest.RaisesExc):
        with pytest.raises(expected_exception=expected.expected_exceptions, match=expected.match):
            validate_age(age)
    else:
        assert validate_age(age) is expected
    
    


