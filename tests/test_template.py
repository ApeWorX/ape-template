def test_template(runner, cli, project_path):
    result = runner.invoke(cli, ["gh:ApeAcademy/ERC20"], input="\n\n\n\n\n\n\n\n\n\n\n")
    assert result.exit_code == 0, result.output
    assert project_path.exists()
    assert project_path.joinpath("contracts").exists()
    assert project_path.joinpath("scripts").exists()
    assert project_path.joinpath("tests").exists()


def test_help(runner, cli):
    result = runner.invoke(cli, "--help")
    assert result.exit_code == 0
