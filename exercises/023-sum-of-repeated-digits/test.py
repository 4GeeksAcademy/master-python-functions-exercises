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


@pytest.mark.it("The function sum_of_repeated_digits should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "sum_of_repeated_digits", None)), "Define a function called sum_of_repeated_digits in app.py"


@pytest.mark.it("sum_of_repeated_digits(9) should return 11106")
def test_case_1():
    app = load_app()
    result = app.sum_of_repeated_digits(9)
    assert_returns(result, 11106, "sum_of_repeated_digits(9)")


@pytest.mark.it("sum_of_repeated_digits(1) should return 1234")
def test_case_2():
    app = load_app()
    result = app.sum_of_repeated_digits(1)
    assert_returns(result, 1234, "sum_of_repeated_digits(1)")


@pytest.mark.it("sum_of_repeated_digits(5) should return 6170")
def test_case_3():
    app = load_app()
    result = app.sum_of_repeated_digits(5)
    assert_returns(result, 6170, "sum_of_repeated_digits(5)")
