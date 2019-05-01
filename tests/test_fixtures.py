from pathlib import Path
import tempfile

import pytest


def test_test_data_no_path(test_data, monkeypatch):
    monkeypatch.setattr(test_data, 'BASE_PATH', None)
    with pytest.raises(Exception) as e:
        test_data.read('hello.txt')

    assert 'Exception: TestData.BASE_PATH is not set. Please set this' in str(e)


def test_test_data_normal(test_data, monkeypatch):
    with tempfile.TemporaryDirectory() as tmp:
        monkeypatch.setattr(test_data, 'BASE_PATH', tmp)
        test_data.write('hello.txt', 'Hello World', serialize=False)
        assert test_data.read('hello.txt', deserialize=False) == 'Hello World'


def test_test_data_json(test_data, monkeypatch):
    with tempfile.TemporaryDirectory() as tmp:
        monkeypatch.setattr(test_data, 'BASE_PATH', Path(tmp))
        test_data.write('hello.json', {'text': 'Hello World'})
        assert test_data.read('hello.json') == {'text': 'Hello World'}
