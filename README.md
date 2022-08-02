# ape-template

The ape-template plugin allows you to use cookiecutter to template an ape project.

## Dependencies

* [python3](https://www.python.org/downloads) version 3.7.2 or greater, python3-dev

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

To use the `template` command, provide either a GitHub repository ID or a raw URI:

```bash
ape template gh:<github org>/<project>

ape template <URI>
```

For more information on Cookiecutter, see their [documentation](https://cookiecutter.readthedocs.io/en/stable/).

## Development

Please see the [contributing guide](CONTRIBUTING.md) to learn more how to contribute to this project.
Comments, questions, criticisms and pull requests are welcomed.

## License

This project is licensed under the [Apache 2.0](LICENSE).
