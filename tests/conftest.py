import pytest
from click.testing import CliRunner


@pytest.fixture(scope="session")
def ape_cli():
    from ape_template._cli import cli

    yield cli


@pytest.fixture(scope="session")
def runner():
    yield CliRunner()
