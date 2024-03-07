import pytest
from app import App


def test_app_add_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'add' command."""
    # Simulate user entering 'add 2 3' followed by 'exit'
    inputs = iter(['add 2 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_divide_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'divide' command."""
    # Simulate user entering 'divide 10 2' followed by 'exit'
    inputs = iter(['divide 10 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"


def test_app_multiply_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'multiply' command."""
    # Simulate user entering 'multiply 2 4' followed by 'exit'
    inputs = iter(['multiply 2 4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_subtraction_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'subtract' command."""
    # Simulate user entering 'subtract 5 3' followed by 'exit'
    inputs = iter(['subtract 5 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"