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


@pytest.mark.it("The function square should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "square", None)), "Define a function called square in app.py"


@pytest.mark.it("square(6) should return 36")
def test_case_1():
    app = load_app()
    result = app.square(6)
    assert_returns(result, 36, "square(6)")


@pytest.mark.it("square(-3) should return 9")
def test_case_2():
    app = load_app()
    result = app.square(-3)
    assert_returns(result, 9, "square(-3)")


@pytest.mark.it("square(0) should return 0")
def test_case_3():
    app = load_app()
    result = app.square(0)
    assert_returns(result, 0, "square(0)")


@pytest.mark.it("square(1.5) should return 2.25")
def test_case_4():
    app = load_app()
    result = app.square(1.5)
    assert_returns(result, 2.25, "square(1.5)")
