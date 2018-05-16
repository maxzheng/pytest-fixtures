""""
Fixtures for Click <http://click.pocoo.org/>
"""

import sys
from traceback import print_tb

import pytest


@pytest.fixture(scope='session')
def cli_runner():
    """ Return an enhanced version of :cls:`click.testing.CliRunner` with better output to aid in debugging """

    from click.testing import CliRunner

    class _CliRunner(CliRunner):
        """ Customize CliRunner with additional helper methods to make testing easier """

        def invoke(self, *args, **kwargs):
            """ Invoke and show stdout/stderr """
            result = super().invoke(*args, **kwargs)

            if result.exception:
                print('--- stderr from CliRunner.invoke ---')
                print(result.exception)
                print_tb(result.exception.__traceback__, file=sys.stdout)
                print('--- stderr end ---')

            if result.output:
                print('--- stdout from CliRunner.invoke ---')
                print(result.output)
                print('--- stdout end ---')

            return result

        def invoke_and_assert_exit(self, expected_exit_code, *args, **kwargs):
            """
            Invoke and assert exit code

            :param int expected_exit_code: The exit code that we expect to see
            :param list args: Positional args to pass to :meth:`CliRunner.invoke`
            :param dict kwargs: Keyword args to pass to :meth:`CliRunner.invoke`
            :return: Result from :meth:`CliRunner.invoke`
            :raises AssertionError: if exit code is not as expected
            """
            result = self.invoke(*args, **kwargs)

            assert expected_exit_code == result.exit_code, \
                'Expected exit code {}, but got {}'.format(expected_exit_code, result.exit_code)

            return result

    return _CliRunner()
