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


@pytest.mark.it("The function total_cost should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "total_cost", None)), "Define a function called total_cost in app.py"


@pytest.mark.it("total_cost(10, 15, 2) should return (20, 30)")
def test_case_1():
    app = load_app()
    result = app.total_cost(10, 15, 2)
    assert_returns(result, (20, 30), "total_cost(10, 15, 2)")


@pytest.mark.it("total_cost(2, 50, 4) should return (10, 0)")
def test_case_2():
    app = load_app()
    result = app.total_cost(2, 50, 4)
    assert_returns(result, (10, 0), "total_cost(2, 50, 4)")


@pytest.mark.it("total_cost(0, 99, 3) should return (2, 97)")
def test_case_3():
    app = load_app()
    result = app.total_cost(0, 99, 3)
    assert_returns(result, (2, 97), "total_cost(0, 99, 3)")
