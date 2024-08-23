"""Test gron."""

from gron import gron


def test_github_data() -> None:
    """Test github data."""
    with open('./tests/data/github.json') as fh:
        IN = fh.read().strip()
    with open('./tests/data/github.gron') as fh:
        OUT = fh.read().strip()
    out = gron(IN)
    assert out == OUT


# not implemented yet
# def test_stream():
#     with open('./tests/data/stream.json', 'r') as fh:
#         IN = fh.read().strip()
#     with open('./tests/data/stream.gron', 'r') as fh:
#         OUT = fh.read().strip()
#     out = gron(IN)
#     assert out == OUT


def test_one() -> None:
    """Test one."""
    with open('./tests/data/one.json') as fh:
        IN = fh.read().strip()
    with open('./tests/data/one.gron') as fh:
        OUT = fh.read().strip()
    out = gron(IN)
    assert out == OUT


def test_two() -> None:
    """Test two."""
    with open('./tests/data/two.json') as fh:
        IN = fh.read().strip()
    with open('./tests/data/two.gron') as fh:
        OUT = fh.read().strip()
    out = gron(IN)
    assert out == OUT


def test_three() -> None:
    """Test three."""
    with open('./tests/data/three.json') as fh:
        IN = fh.read().strip()
    with open('./tests/data/three.gron') as fh:
        OUT = fh.read().strip()
    out = gron(IN)
    assert out == OUT


def test_ugly() -> None:
    """Test ugly."""
    with open('./tests/data/ugly.json') as fh:
        IN = fh.read().strip()
    with open('./tests/data/ugly.gron') as fh:
        OUT = fh.read().strip()
    out = gron(IN)
    assert out == OUT
