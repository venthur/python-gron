# python-gron

Make JSON grep-able, a Python implementation of
[gron](https://github.com/tomnomnom/gron).


## Installation

`gron` is available on [PyPi](https://pypi.org/project/gron/), to install it
use:

```bash
$ pip install gron
```


## Documentation

The API documentation can be found
[here](http://gron.readthedocs.io/en/latest/).


## Usage

Given a JSON file with the content:

```json
{
  "one": 1,
  "two": 2.2,
  "three-b": "3",
  "four": [1,2,3,4],
  "five": {
    "alpha": ["fo", "fum"],
    "beta": {
      "hey": "How's tricks?"
    }
  },
  "abool": true,
  "abool2": false,
  "isnull": null,
  "id": 66912849
}
```

you can use `gron` like this:

```bash
$ gron tests/data/one.json
json = {};
json.abool = true;
json.abool2 = false;
json.five = {};
json.five.alpha = [];
json.five.alpha[0] = "fo";
json.five.alpha[1] = "fum";
json.five.beta = {};
json.five.beta.hey = "How's tricks?";
json.four = [];
json.four[0] = 1;
json.four[1] = 2;
json.four[2] = 3;
json.four[3] = 4;
json.id = 66912849;
json.isnull = null;
json.one = 1;
json.two = 2.2;
json["three-b"] = "3";``
```

Without any arguments `gron` will read from `STDIN`:

```bash
$ cat tests/data/one.json | gron
json = {};
json.abool = true;
json.abool2 = false;
json.five = {};
json.five.alpha = [];
json.five.alpha[0] = "fo";
json.five.alpha[1] = "fum";
json.five.beta = {};
json.five.beta.hey = "How's tricks?";
json.four = [];
json.four[0] = 1;
json.four[1] = 2;
json.four[2] = 3;
json.four[3] = 4;
json.id = 66912849;
json.isnull = null;
json.one = 1;
json.two = 2.2;
json["three-b"] = "3";
```
