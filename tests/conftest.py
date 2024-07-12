from base.web_driver_factory import Web_Driver_Factory
import pytest

@pytest.fixture(scope="class")
def init_driver(whichBrowser, request):

    wdf = Web_Driver_Factory(whichBrowser)
    driver = wdf.webDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--whichBrowser")

@pytest.fixture(scope = "session")
def whichBrowser(request):
    return request.config.getoption("--whichBrowser")