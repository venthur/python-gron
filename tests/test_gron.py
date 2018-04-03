from gron import gron


def test_github_data():
    with open('./tests/data/github.json', 'r') as fh:
        IN = fh.read().strip()
    with open('./tests/data/github.gron', 'r') as fh:
        OUT = fh.read().strip()
    out = gron(IN)
    assert out == OUT

# not implemented yet
#def test_stream():
#    with open('./tests/data/stream.json', 'r') as fh:
#        IN = fh.read().strip()
#    with open('./tests/data/stream.gron', 'r') as fh:
#        OUT = fh.read().strip()
#    out = gron(IN)
#    assert out == OUT


def test_one():
    with open('./tests/data/one.json', 'r') as fh:
        IN = fh.read().strip()
    with open('./tests/data/one.gron', 'r') as fh:
        OUT = fh.read().strip()
    out = gron(IN)
    assert out == OUT


def test_two():
    with open('./tests/data/two.json', 'r') as fh:
        IN = fh.read().strip()
    with open('./tests/data/two.gron', 'r') as fh:
        OUT = fh.read().strip()
    out = gron(IN)
    assert out == OUT


def test_three():
    with open('./tests/data/three.json', 'r') as fh:
        IN = fh.read().strip()
    with open('./tests/data/three.gron', 'r') as fh:
        OUT = fh.read().strip()
    out = gron(IN)
    assert out == OUT


def test_ugly():
    with open('./tests/data/ugly.json', 'r') as fh:
        IN = fh.read().strip()
    with open('./tests/data/ugly.gron', 'r') as fh:
        OUT = fh.read().strip()
    out = gron(IN)
    assert out == OUT
