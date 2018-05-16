def test_cli_runner(testdir):
    testdir.makepyfile("""
import sys

import click


@click.command()
@click.argument('name')
def hello(name):
    click.echo('Hello %s!' % name)


def test_invoke(cli_runner):
    result = cli_runner.invoke(hello, ['Peter'])
    assert result.exit_code == 0
    assert result.output == 'Hello Peter!\\n'


def test_invoke_and_assert(cli_runner):
    result = cli_runner.invoke_and_assert_exit(0, hello, ['Peter'])
    assert result.output == 'Hello Peter!\\n'


def test_invoke_and_assert_fail(cli_runner):
    ''' This will fail '''
    result = cli_runner.invoke_and_assert_exit(1, hello, ['Peter'])
    assert result.output == 'Hello Peter!\\n'
""")

    result = testdir.runpytest()
    result.assert_outcomes(passed=2, failed=1)
