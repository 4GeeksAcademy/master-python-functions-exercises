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


@pytest.mark.it("The function order_quantity should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "order_quantity", None)), "Define a function called order_quantity in app.py"


@pytest.mark.it("The function order_quantity should return a value of type int")
def test_return_type():
    app = load_app()
    result = app.order_quantity(150)
    assert isinstance(result, int), f"order_quantity should return a int, but it returned {type(result).__name__}"


@pytest.mark.it("order_quantity(150) should return 22")
def test_case_1():
    app = load_app()
    result = app.order_quantity(150)
    assert_returns(result, 22, "order_quantity(150)")


@pytest.mark.it("order_quantity(100) should return 18")
def test_case_2():
    app = load_app()
    result = app.order_quantity(100)
    assert_returns(result, 18, "order_quantity(100)")


@pytest.mark.it("order_quantity(30) should return 10")
def test_case_3():
    app = load_app()
    result = app.order_quantity(30)
    assert_returns(result, 10, "order_quantity(30)")
