import pytest

from src.service.build import Build


@pytest.fixture(scope="module")
def start_stop_webcalculator():
    build_func = Build()
    result = build_func.up()
    yield result
    build_func.down()


@pytest.fixture()
def start_webcalculator_app():
    build_app = Build()
    return build_app


@pytest.fixture()
def start_stop_webcalculator_app():
    build_app = Build()
    build_app.up(default=True)
    yield build_app
    build_app.down()
