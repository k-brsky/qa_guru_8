import pytest
import os
from zipfile import ZipFile, ZIP_DEFLATED
from os.path import basename
import shutil
@pytest.fixture(scope='session', autouse=True)
def make_and_remove_zip():
    path = 'tests/resources'
    file_dir = os.listdir(path)
    if not os.path.exists('tests/tmp'):
        os.mkdir('tests/tmp')
    with ZipFile('tests/tmp/homework.zip', mode='w', compression=ZIP_DEFLATED) as zf:
        for file in file_dir:
            add_file = os.path.join(path, file)
            zf.write(add_file, basename(add_file))

    yield

    shutil.rmtree('tests/tmp')
