import importlib.util
import os

import pytest

APP_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.py")


def load_app():
    """Load the student's app.py as a fresh module."""
    spec = importlib.util.spec_from_file_location("student_app", APP_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def assert_returns(result, expected, call):
    assert result is not None, f"{call} returned None. Did you forget the return statement?"
    assert result == expected, f"{call} should return {expected!r}, but it returned {result!r}"


@pytest.mark.it("The function first_decimal_digit should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "first_decimal_digit", None)), "Define a function called first_decimal_digit in app.py"


@pytest.mark.it("The function first_decimal_digit should return a value of type int")
def test_return_type():
    app = load_app()
    result = app.first_decimal_digit(1.79)
    assert isinstance(result, int), f"first_decimal_digit should return a int, but it returned {type(result).__name__}"


@pytest.mark.it("first_decimal_digit(1.79) should return 7")
def test_case_1():
    app = load_app()
    result = app.first_decimal_digit(1.79)
    assert_returns(result, 7, "first_decimal_digit(1.79)")


@pytest.mark.it("first_decimal_digit(10.2) should return 2")
def test_case_2():
    app = load_app()
    result = app.first_decimal_digit(10.2)
    assert_returns(result, 2, "first_decimal_digit(10.2)")


@pytest.mark.it("first_decimal_digit(3.05) should return 0")
def test_case_3():
    app = load_app()
    result = app.first_decimal_digit(3.05)
    assert_returns(result, 0, "first_decimal_digit(3.05)")


@pytest.mark.it("first_decimal_digit(0.9) should return 9")
def test_case_4():
    app = load_app()
    result = app.first_decimal_digit(0.9)
    assert_returns(result, 9, "first_decimal_digit(0.9)")
