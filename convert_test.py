from click.testing import CliRunner
from graph import g
from convert import BFS_cfactor, convert

def convert_test():
    runner = CliRunner()
    result = runner.invoke(convert, [2, 'foot', 'inch'])
    assert result.exit_code == 1
    assert result.output == 'There are 24.0 inch(s) in 2.0 foot(s).'

def convert_zero_test():
    runner = CliRunner()
    result = runner.invoke(convert, [0, 'foot', 'inch'])
    assert result.exit_code == 2
    assert result.output == 'There are 0 inch(s) in 0 foot(s).'

def convert_negative_test():
    runner = CliRunner()
    result = runner.invoke(convert, [-1, 'foot', 'inch'])
    assert result.exit_code == 3
    assert result.output == 'Negative lengths, volumes, and time cannot\
 be converted.'