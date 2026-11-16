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


@pytest.mark.it("The function two_timestamps should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "two_timestamps", None)), "Define a function called two_timestamps in app.py"


@pytest.mark.it("two_timestamps(1, 1, 1, 2, 2, 2) should return 3661")
def test_case_1():
    app = load_app()
    result = app.two_timestamps(1, 1, 1, 2, 2, 2)
    assert_returns(result, 3661, "two_timestamps(1, 1, 1, 2, 2, 2)")


@pytest.mark.it("two_timestamps(1, 2, 30, 1, 3, 20) should return 50")
def test_case_2():
    app = load_app()
    result = app.two_timestamps(1, 2, 30, 1, 3, 20)
    assert_returns(result, 50, "two_timestamps(1, 2, 30, 1, 3, 20)")


@pytest.mark.it("two_timestamps(0, 0, 0, 23, 59, 59) should return 86399")
def test_case_3():
    app = load_app()
    result = app.two_timestamps(0, 0, 0, 23, 59, 59)
    assert_returns(result, 86399, "two_timestamps(0, 0, 0, 23, 59, 59)")
