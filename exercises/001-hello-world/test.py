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


@pytest.mark.it("Your code should print Hello World in the console")
def test_prints_hello_world(capsys):
    load_app()
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n", f"Expected 'Hello World' but the console shows {captured.out!r}"
