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


@pytest.mark.it("The function area_of_triangle should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "area_of_triangle", None)), "Define a function called area_of_triangle in app.py"


@pytest.mark.it("area_of_triangle(3, 5) should return 7.5")
def test_case_1():
    app = load_app()
    result = app.area_of_triangle(3, 5)
    assert result is not None, "area_of_triangle(3, 5) returned None. Did you forget the return statement?"
    assert result == pytest.approx(7.5, abs=0.01), f"area_of_triangle(3, 5) should return 7.5, but it returned {result!r}"


@pytest.mark.it("area_of_triangle(4, 2) should return 4.0")
def test_case_2():
    app = load_app()
    result = app.area_of_triangle(4, 2)
    assert result is not None, "area_of_triangle(4, 2) returned None. Did you forget the return statement?"
    assert result == pytest.approx(4.0, abs=0.01), f"area_of_triangle(4, 2) should return 4.0, but it returned {result!r}"


@pytest.mark.it("area_of_triangle(10, 7) should return 35.0")
def test_case_3():
    app = load_app()
    result = app.area_of_triangle(10, 7)
    assert result is not None, "area_of_triangle(10, 7) returned None. Did you forget the return statement?"
    assert result == pytest.approx(35.0, abs=0.01), f"area_of_triangle(10, 7) should return 35.0, but it returned {result!r}"
