pytest-fixtures
===============

Common fixtures for pytest

To use, just install it and pytest will automatically detect and load all fixtures::

    pip install pytest-fixtures

To install automatically, add it to your test requirements in `tox.ini` or `setup.py`.

No Dependencies
---------------

This package does not depend on any other packages and never will. It uses standard libraries or uses run-time
imports and therefore it is lightweight to add to any project. As for which external run-time dependency a fixture
needs, that is documented here and shouldn't matter as you would only use the fixtures that your project already has
dependencies on.

Standard Fixtures
-----------------

Fixtures based on standard Python libraries


test_data
~~~~~~~~~

To get path, read, and write test data in `tests/data` folder, use the `test_data` fixture.

First, setup the path to test data path in `tests/conftest.py`:

.. code-block:: python

    from pathlib import Path
    from fixtures import TestData

    TestData.BASE_PATH = Path(__file__).parent / 'data'

And then get path to data files in `tests/data` using `test_data` fixture:

.. code-block:: python

    def test_integration(test_data):
        obj = MyClass(test_data.path('sample.csv'))

To write out test data:

.. code-block:: python

    def test_integration(test_data):
        output = run_cli()
        test_data.write('test_integration.output', output)

Then read the test data to assert:

.. code-block:: python

    def test_integration(test_data):
        output = run_cli()
        expected_output = test_data.read('test_integration.output')
        assert expected_output == output

Click Fixtures
--------------

Fixtures for Click <http://click.pocoo.org/>

cli_runner
~~~~~~~~~~

To invoke, assert exit, with stdout/stderr outputs on error::

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
