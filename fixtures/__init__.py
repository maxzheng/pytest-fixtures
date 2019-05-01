"""
Fixtures for standard libraries
"""

import json
from pathlib import Path

import pytest


class TestData:
    """ Helper functions to access/write test data """
    #: Base directory to test data, so we can easily refer to test data by name instead of full path
    BASE_PATH = None

    @classmethod
    def path(cls, name):
        """ Return a Path object to the given test file name """
        if not cls.BASE_PATH:
            raise Exception('TestData.BASE_PATH is not set. Please set this in test/conftest.py to the directory '
                            'with test data (e.g. full path to $project_root/test/data)')
        return Path(cls.BASE_PATH) / name

    @classmethod
    def write(cls, name, content, serialize=True):
        """
        Write test file with the given content

        :param str name: Name of the file to write
        :param obj content: Content to write to file. This can be any JSON serializable object.
        :param bool serialize: If True, serialize to JSON
        """
        with cls.path(name).open('w') as fp:
            if serialize:
                json.dump(content, fp, indent=4)
            else:
                fp.write(content)

    @classmethod
    def read(cls, name, deserialize=True):
        """
        Read test file with the given name

        :param str name: Name of the test file to read
        :param bool deserialize: If True, deserialize from JSON
        """
        with cls.path(name).open() as fp:
            if deserialize:
                return json.load(fp)
            else:
                return fp.read()


@pytest.fixture
def test_data():
    return TestData
