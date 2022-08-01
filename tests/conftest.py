import shutil
from pathlib import Path

import pytest
from click.testing import CliRunner

from ape_template._cli import cli as template_cli


@pytest.fixture(scope="session")
def cli():
    return template_cli


@pytest.fixture(scope="session")
def runner():
    yield CliRunner()


@pytest.fixture
def project_path():
    project_path = Path(__file__).parent / "TokenProject"

    if project_path.exists():
        shutil.rmtree(project_path)

    yield project_path

    if project_path.exists():
        shutil.rmtree(project_path)
