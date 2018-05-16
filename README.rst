pytest-fixtures
===============

Common fixtures for pytest

Click Fixtures
--------------

Fixtures for Click <http://click.pocoo.org/>

.. code-block:: python

    def test_cli(cli_runner):
        result = cli_runner.invoke( ... )                       # Prints out stdout/stderr from result with headings
        result = cli_runner.invoke_and_assert_exit(0, ... )     # Same as above and asserts exit code == 0

Links & Contact Info
====================

| PyPI Package: https://pypi.python.org/pypi/pytest-fixtures
| GitHub Source: https://github.com/maxzheng/pytest-fixtures
| Report Issues/Bugs: https://github.com/maxzheng/pytest-fixtures/issues
|
| Follow: https://twitter.com/MaxZhengX
| Connect: https://www.linkedin.com/in/maxzheng
| Contact: maxzheng.os @t gmail.com
