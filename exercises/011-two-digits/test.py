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


@pytest.mark.it("The function two_digits should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "two_digits", None)), "Define a function called two_digits in app.py"


@pytest.mark.it("two_digits(79) should return (7, 9)")
def test_case_1():
    app = load_app()
    result = app.two_digits(79)
    assert_returns(result, (7, 9), "two_digits(79)")


@pytest.mark.it("two_digits(30) should return (3, 0)")
def test_case_2():
    app = load_app()
    result = app.two_digits(30)
    assert_returns(result, (3, 0), "two_digits(30)")


@pytest.mark.it("two_digits(11) should return (1, 1)")
def test_case_3():
    app = load_app()
    result = app.two_digits(11)
    assert_returns(result, (1, 1), "two_digits(11)")
