import shutil
from pathlib import Path


def test_template(runner, ape_cli):
    project_path = Path("./TokenProject/")

    if project_path.exists():
        shutil.rmtree(project_path)

    result = runner.invoke(ape_cli, ["gh:ApeAcademy/ERC20"], input="\n\n\n\n\n\n\n\n\n\n\n")
    assert result.exit_code == 0
    assert project_path.exists()
    assert project_path.joinpath("contracts").exists()
    assert project_path.joinpath("scripts").exists()
    assert project_path.joinpath("tests").exists()
    shutil.rmtree(project_path)
