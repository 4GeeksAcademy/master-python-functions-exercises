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


@pytest.mark.it("The function tens_digit should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "tens_digit", None)), "Define a function called tens_digit in app.py"


@pytest.mark.it("tens_digit(1234) should return 3")
def test_case_1():
    app = load_app()
    result = app.tens_digit(1234)
    assert_returns(result, 3, "tens_digit(1234)")


@pytest.mark.it("tens_digit(179) should return 7")
def test_case_2():
    app = load_app()
    result = app.tens_digit(179)
    assert_returns(result, 7, "tens_digit(179)")


@pytest.mark.it("tens_digit(5) should return 0")
def test_case_3():
    app = load_app()
    result = app.tens_digit(5)
    assert_returns(result, 0, "tens_digit(5)")
