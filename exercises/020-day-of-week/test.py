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


@pytest.mark.it("The function day_of_week should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "day_of_week", None)), "Define a function called day_of_week in app.py"


@pytest.mark.it("day_of_week(1) should return 4")
def test_case_1():
    app = load_app()
    result = app.day_of_week(1)
    assert_returns(result, 4, "day_of_week(1)")


@pytest.mark.it("day_of_week(4) should return 0")
def test_case_2():
    app = load_app()
    result = app.day_of_week(4)
    assert_returns(result, 0, "day_of_week(4)")


@pytest.mark.it("day_of_week(10) should return 6")
def test_case_3():
    app = load_app()
    result = app.day_of_week(10)
    assert_returns(result, 6, "day_of_week(10)")


@pytest.mark.it("day_of_week(365) should return 4")
def test_case_4():
    app = load_app()
    result = app.day_of_week(365)
    assert_returns(result, 4, "day_of_week(365)")
