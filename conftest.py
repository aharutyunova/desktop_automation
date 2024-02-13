from pywinauto import Application
import pytest
import config


@pytest.fixture()
def app():
    try:
        application = Application(backend='uia').start(config.exe_name, timeout=10)
        application.connect(best_match=config.app_name, timeout=5)
        window_app = application[config.app_name]
        yield window_app
        application.kill()
    except Exception as error:
        raise Exception(error)