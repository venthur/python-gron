import gron


def test_version() -> None:
    assert hasattr(gron, '__VERSION__')
