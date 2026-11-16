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


@pytest.mark.it("The function apple_sharing should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "apple_sharing", None)), "Define a function called apple_sharing in app.py"


@pytest.mark.it("apple_sharing(6, 50) should return (8, 2)")
def test_case_1():
    app = load_app()
    result = app.apple_sharing(6, 50)
    assert_returns(result, (8, 2), "apple_sharing(6, 50)")


@pytest.mark.it("apple_sharing(5, 10) should return (2, 0)")
def test_case_2():
    app = load_app()
    result = app.apple_sharing(5, 10)
    assert_returns(result, (2, 0), "apple_sharing(5, 10)")


@pytest.mark.it("apple_sharing(4, 3) should return (0, 3)")
def test_case_3():
    app = load_app()
    result = app.apple_sharing(4, 3)
    assert_returns(result, (0, 3), "apple_sharing(4, 3)")
