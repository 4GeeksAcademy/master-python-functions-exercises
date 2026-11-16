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


@pytest.mark.it("The function hours_minutes should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "hours_minutes", None)), "Define a function called hours_minutes in app.py"


@pytest.mark.it("hours_minutes(3900) should return (1, 5)")
def test_case_1():
    app = load_app()
    result = app.hours_minutes(3900)
    assert_returns(result, (1, 5), "hours_minutes(3900)")


@pytest.mark.it("hours_minutes(60) should return (0, 1)")
def test_case_2():
    app = load_app()
    result = app.hours_minutes(60)
    assert_returns(result, (0, 1), "hours_minutes(60)")


@pytest.mark.it("hours_minutes(7322) should return (2, 2)")
def test_case_3():
    app = load_app()
    result = app.hours_minutes(7322)
    assert_returns(result, (2, 2), "hours_minutes(7322)")


@pytest.mark.it("hours_minutes(59) should return (0, 0)")
def test_case_4():
    app = load_app()
    result = app.hours_minutes(59)
    assert_returns(result, (0, 0), "hours_minutes(59)")
