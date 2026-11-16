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


@pytest.mark.it("The function count_digits should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "count_digits", None)), "Define a function called count_digits in app.py"


@pytest.mark.it("count_digits(2026) should return 4")
def test_case_1():
    app = load_app()
    result = app.count_digits(2026)
    assert_returns(result, 4, "count_digits(2026)")


@pytest.mark.it("count_digits(7) should return 1")
def test_case_2():
    app = load_app()
    result = app.count_digits(7)
    assert_returns(result, 1, "count_digits(7)")


@pytest.mark.it("count_digits(0) should return 1")
def test_case_3():
    app = load_app()
    result = app.count_digits(0)
    assert_returns(result, 1, "count_digits(0)")


@pytest.mark.it("count_digits(1000000) should return 7")
def test_case_4():
    app = load_app()
    result = app.count_digits(1000000)
    assert_returns(result, 7, "count_digits(1000000)")


@pytest.mark.it("You should use a while loop and not convert the number to a string")
def test_uses_while():
    with open(APP_PATH, encoding="utf-8") as fh:
        content = fh.read()
    assert "while" in content, "Use a while loop to solve this exercise"
    assert "str(" not in content and "len(" not in content, "Solve it with numbers: don't use str() or len()"
