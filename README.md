# ape-template

The ape-template plugin allows you to use cookiecutter to template an ape project.

## Dependencies

* [python3](https://www.python.org/downloads) version 3.7.2 or greater, python3-dev
* [cookiecutter](https://cookiecutter.readthedocs.io/en/2.0.2/) version 2.1.1
* [eth-ape](https://docs.apeworx.io/ape/stable/) 0.3.0 or greater,

## Installation

### via `pip`

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install ape-template
```

### via `setuptools`

You can clone the repository and use [`setuptools`](https://github.com/pypa/setuptools) for the most up-to-date version:

```bash
git clone https://github.com/ApeWorX/ape-template.git
cd ape-template
python3 setup.py install
```

## Quick Usage

Use `-h` to list all the commands.

```bash
ape template -h
```

Template use example

```bash
ape template gh:<github org>/<project>

ape template <URI>
```
[cookiecutter docs](https://cookiecutter.readthedocs.io/en/stable/)

## Development

This project is in development and should be considered a beta.
Things might not be in their final state and breaking changes may occur.
Comments, questions, criticisms and pull requests are welcomed.

## License

This project is licensed under the [Apache 2.0](LICENSE).
