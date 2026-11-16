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


@pytest.mark.it("The function factorial should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "factorial", None)), "Define a function called factorial in app.py"


@pytest.mark.it("factorial(5) should return 120")
def test_case_1():
    app = load_app()
    result = app.factorial(5)
    assert_returns(result, 120, "factorial(5)")


@pytest.mark.it("factorial(8) should return 40320")
def test_case_2():
    app = load_app()
    result = app.factorial(8)
    assert_returns(result, 40320, "factorial(8)")


@pytest.mark.it("factorial(0) should return 1")
def test_case_3():
    app = load_app()
    result = app.factorial(0)
    assert_returns(result, 1, "factorial(0)")


@pytest.mark.it("factorial(1) should return 1")
def test_case_4():
    app = load_app()
    result = app.factorial(1)
    assert_returns(result, 1, "factorial(1)")


@pytest.mark.it("You should solve it with a loop, not with math.factorial()")
def test_no_math_factorial():
    with open(APP_PATH, encoding="utf-8") as fh:
        content = fh.read()
    assert "math.factorial" not in content, "Use a for or while loop instead of math.factorial()"
