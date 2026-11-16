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


@pytest.mark.it("The function previous_next should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "previous_next", None)), "Define a function called previous_next in app.py"


@pytest.mark.it("previous_next(179) should return (178, 180)")
def test_case_1():
    app = load_app()
    result = app.previous_next(179)
    assert_returns(result, (178, 180), "previous_next(179)")


@pytest.mark.it("previous_next(0) should return (-1, 1)")
def test_case_2():
    app = load_app()
    result = app.previous_next(0)
    assert_returns(result, (-1, 1), "previous_next(0)")


@pytest.mark.it("previous_next(-10) should return (-11, -9)")
def test_case_3():
    app = load_app()
    result = app.previous_next(-10)
    assert_returns(result, (-11, -9), "previous_next(-10)")
