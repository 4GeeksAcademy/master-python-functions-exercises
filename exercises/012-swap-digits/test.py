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


@pytest.mark.it("The function swap_digits should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "swap_digits", None)), "Define a function called swap_digits in app.py"


@pytest.mark.it("The function swap_digits should return a value of type int")
def test_return_type():
    app = load_app()
    result = app.swap_digits(79)
    assert isinstance(result, int), f"swap_digits should return a int, but it returned {type(result).__name__}"


@pytest.mark.it("swap_digits(79) should return 97")
def test_case_1():
    app = load_app()
    result = app.swap_digits(79)
    assert_returns(result, 97, "swap_digits(79)")


@pytest.mark.it("swap_digits(30) should return 3")
def test_case_2():
    app = load_app()
    result = app.swap_digits(30)
    assert_returns(result, 3, "swap_digits(30)")


@pytest.mark.it("swap_digits(12) should return 21")
def test_case_3():
    app = load_app()
    result = app.swap_digits(12)
    assert_returns(result, 21, "swap_digits(12)")
