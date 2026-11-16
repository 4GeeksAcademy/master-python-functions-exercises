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


@pytest.mark.it("The function last_two_digits should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "last_two_digits", None)), "Define a function called last_two_digits in app.py"


@pytest.mark.it("last_two_digits(1234) should return 34")
def test_case_1():
    app = load_app()
    result = app.last_two_digits(1234)
    assert_returns(result, 34, "last_two_digits(1234)")


@pytest.mark.it("last_two_digits(1205) should return 5")
def test_case_2():
    app = load_app()
    result = app.last_two_digits(1205)
    assert_returns(result, 5, "last_two_digits(1205)")


@pytest.mark.it("last_two_digits(10) should return 10")
def test_case_3():
    app = load_app()
    result = app.last_two_digits(10)
    assert_returns(result, 10, "last_two_digits(10)")


@pytest.mark.it("last_two_digits(987654) should return 54")
def test_case_4():
    app = load_app()
    result = app.last_two_digits(987654)
    assert_returns(result, 54, "last_two_digits(987654)")
