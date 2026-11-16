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


@pytest.mark.it("The function square_root should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "square_root", None)), "Define a function called square_root in app.py"


@pytest.mark.it("square_root(50) should return 7.07")
def test_case_1():
    app = load_app()
    result = app.square_root(50)
    assert_returns(result, 7.07, "square_root(50)")


@pytest.mark.it("square_root(16) should return 4.0")
def test_case_2():
    app = load_app()
    result = app.square_root(16)
    assert_returns(result, 4.0, "square_root(16)")


@pytest.mark.it("square_root(2) should return 1.41")
def test_case_3():
    app = load_app()
    result = app.square_root(2)
    assert_returns(result, 1.41, "square_root(2)")
