from pywinauto import Application
import pytest
import logging
import config


@pytest.fixture()
def app():
    try:
        app = Application(backend='uia').start(config.exe_name, timeout=10)
        app.connect(best_match=config.app_name, timeout=5)
        window_app = app[config.app_name]
        yield window_app
        app.kill()
    except Exception as error:
        raise Exception(error)


def pytest_configure():
    logging.basicConfig(filename= "my_log.log",
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S'
                        )