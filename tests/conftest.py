import pytest
import os
from applitools.selenium import (
    Eyes,
    VisualGridRunner,
    BatchInfo,
    BrowserType,
    DeviceName)


@pytest.fixture(scope='function')
def py_eyes():
    runner = VisualGridRunner(10)
    py_eyes = Eyes(runner)
    # You can get your api key from the Applitools dashboard
    api_key = os.environ["APPLITOOLS_API_KEY"]
    print("API_KEY = " + api_key)
    py_eyes.configure.set_api_key(api_key)

    # create a new batch info instance and set it to the configuration
    py_eyes.configure.set_batch(BatchInfo("UFG Hackaton"))

    # Add browsers with different viewports
    # Add mobile emulation devices in Portrait mode
    (
        py_eyes.configure.add_browser(1200, 700, BrowserType.CHROME)
            .add_browser(1200, 700, BrowserType.FIREFOX)
            .add_browser(1200, 700, BrowserType.EDGE_CHROMIUM)
            .add_browser(768, 700, BrowserType.CHROME)
            .add_browser(1200, 700, BrowserType.FIREFOX)
            .add_browser(1200, 700, BrowserType.EDGE_CHROMIUM)
            .add_device_emulation(DeviceName.iPhone_X)  # Portrait mode
    )
    yield py_eyes
    all_test_results = runner.get_all_test_results(False)
    print(all_test_results)