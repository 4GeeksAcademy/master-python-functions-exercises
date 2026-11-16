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


@pytest.mark.it("The function digital_clock should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "digital_clock", None)), "Define a function called digital_clock in app.py"


@pytest.mark.it("digital_clock(150) should return (2, 30)")
def test_case_1():
    app = load_app()
    result = app.digital_clock(150)
    assert_returns(result, (2, 30), "digital_clock(150)")


@pytest.mark.it("digital_clock(1441) should return (0, 1)")
def test_case_2():
    app = load_app()
    result = app.digital_clock(1441)
    assert_returns(result, (0, 1), "digital_clock(1441)")


@pytest.mark.it("digital_clock(0) should return (0, 0)")
def test_case_3():
    app = load_app()
    result = app.digital_clock(0)
    assert_returns(result, (0, 0), "digital_clock(0)")


@pytest.mark.it("digital_clock(1439) should return (23, 59)")
def test_case_4():
    app = load_app()
    result = app.digital_clock(1439)
    assert_returns(result, (23, 59), "digital_clock(1439)")
