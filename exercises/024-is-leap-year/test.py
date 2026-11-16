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


@pytest.mark.it("The function is_leap_year should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "is_leap_year", None)), "Define a function called is_leap_year in app.py"


@pytest.mark.it("is_leap_year(2024) should return True")
def test_case_1():
    app = load_app()
    result = app.is_leap_year(2024)
    assert_returns(result, True, "is_leap_year(2024)")


@pytest.mark.it("is_leap_year(1900) should return False")
def test_case_2():
    app = load_app()
    result = app.is_leap_year(1900)
    assert_returns(result, False, "is_leap_year(1900)")


@pytest.mark.it("is_leap_year(2000) should return True")
def test_case_3():
    app = load_app()
    result = app.is_leap_year(2000)
    assert_returns(result, True, "is_leap_year(2000)")


@pytest.mark.it("is_leap_year(2023) should return False")
def test_case_4():
    app = load_app()
    result = app.is_leap_year(2023)
    assert_returns(result, False, "is_leap_year(2023)")
