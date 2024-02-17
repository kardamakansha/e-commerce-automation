import pytest
import pathlib
import json


@pytest.fixture
def json_data(request):
    file = pathlib.Path(request.node.fspath.strpath)
    data = file.with_name('data.json')
    with data.open() as fp:
        return json.load(fp)