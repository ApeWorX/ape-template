import os
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


@pytest.fixture(scope="session", autouse=True)
def from_tests_dir():
    tests_dir = Path(__file__).parent
    curr_dir = os.curdir
    os.chdir(str(tests_dir))
    yield tests_dir
    os.chdir(curr_dir)


@pytest.fixture
def project_path():
    project_path = Path(__file__).parent / "TokenProject"

    if project_path.exists():
        shutil.rmtree(project_path)

    yield project_path

    if project_path.exists():
        shutil.rmtree(project_path)
