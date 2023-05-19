import pytest, json, shutil, time

@pytest.fixture(scope='module', autouse=True)
def delete_all_lesson():
    pass