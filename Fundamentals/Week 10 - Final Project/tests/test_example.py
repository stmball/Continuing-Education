"""Sample tests to make sure everything is working correctly."""
from main import main


def test_pytest():
    """Test pytest can do simple maths."""
    assert 2 + 2 == 4


def test_import():
    """Test imports are working correctly."""
    assert main()
