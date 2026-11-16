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


@pytest.mark.it("The function century should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "century", None)), "Define a function called century in app.py"


@pytest.mark.it("century(2001) should return 21")
def test_case_1():
    app = load_app()
    result = app.century(2001)
    assert_returns(result, 21, "century(2001)")


@pytest.mark.it("century(2000) should return 20")
def test_case_2():
    app = load_app()
    result = app.century(2000)
    assert_returns(result, 20, "century(2000)")


@pytest.mark.it("century(1) should return 1")
def test_case_3():
    app = load_app()
    result = app.century(1)
    assert_returns(result, 1, "century(1)")


@pytest.mark.it("century(1950) should return 20")
def test_case_4():
    app = load_app()
    result = app.century(1950)
    assert_returns(result, 20, "century(1950)")
