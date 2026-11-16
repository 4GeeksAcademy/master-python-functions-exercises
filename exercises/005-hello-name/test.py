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


@pytest.mark.it("The function hello_name should exist")
def test_function_exists():
    app = load_app()
    assert callable(getattr(app, "hello_name", None)), "Define a function called hello_name in app.py"


@pytest.mark.it("hello_name('Harry') should return 'Hello, Harry!'")
def test_case_1():
    app = load_app()
    result = app.hello_name('Harry')
    assert_returns(result, 'Hello, Harry!', "hello_name('Harry')")


@pytest.mark.it("hello_name('Ana') should return 'Hello, Ana!'")
def test_case_2():
    app = load_app()
    result = app.hello_name('Ana')
    assert_returns(result, 'Hello, Ana!', "hello_name('Ana')")


@pytest.mark.it("hello_name('4Geeks') should return 'Hello, 4Geeks!'")
def test_case_3():
    app = load_app()
    result = app.hello_name('4Geeks')
    assert_returns(result, 'Hello, 4Geeks!', "hello_name('4Geeks')")
