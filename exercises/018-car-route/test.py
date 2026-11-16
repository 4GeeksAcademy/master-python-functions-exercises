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


@pytest.mark.it("The function car_route should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "car_route", None)), "Define a function called car_route in app.py"


@pytest.mark.it("car_route(20, 40) should return 2")
def test_case_1():
    app = load_app()
    result = app.car_route(20, 40)
    assert_returns(result, 2, "car_route(20, 40)")


@pytest.mark.it("car_route(20, 41) should return 3")
def test_case_2():
    app = load_app()
    result = app.car_route(20, 41)
    assert_returns(result, 3, "car_route(20, 41)")


@pytest.mark.it("car_route(700, 750) should return 2")
def test_case_3():
    app = load_app()
    result = app.car_route(700, 750)
    assert_returns(result, 2, "car_route(700, 750)")


@pytest.mark.it("car_route(100, 50) should return 1")
def test_case_4():
    app = load_app()
    result = app.car_route(100, 50)
    assert_returns(result, 1, "car_route(100, 50)")
