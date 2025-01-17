import pytest
import os
from applitools.selenium import (
    Eyes,
    VisualGridRunner,
    BatchInfo,
    BrowserType,
    DeviceName)

toDisplayType = {
    0: "MOBILE",
    1: "TABLET",
    2: "DESKTOP",
}


@pytest.fixture
def py_eyes():
    runner = VisualGridRunner(10)
    py_eyes = Eyes(runner)
    # You can get your api key from the Applitools dashboard
    api_key = os.environ["APPLITOOLS_API_KEY"]
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


def getDisplayType(item):
    Id = item.funcargs["displayType"] if "displayType" in item.fixturenames else -1
    return toDisplayType.get(Id, "Invalid display type!")


def logTaskReport(writer, py_config, test_case, item):
    if item.rep_call is None:
        return
    # testName = test_case.name
    testName = item.funcargs["testName"] if "testName" in item.fixturenames else test_case.name

    if test_case.name.find('task1') != -1:
        taskNumber = "1"
    elif test_case.name.find('task2') != -1:
        taskNumber = "2"
    elif test_case.name.find('task3') != -1:
        taskNumber = "3"
    else:
        taskNumber = "?"

    testResult = "Pass" if item.rep_call is not None and item.rep_call.passed else "Fail"
    browserName = py_config.driver.browser
    log = writer.log
    p = {
        "w": item.funcargs["width"] if "width" in item.fixturenames else "",
        "h": item.funcargs["height"] if "height" in item.fixturenames else "",
        "display": getDisplayType(item),
    }
    # assertionError = ""
    # if item.rep_call.longrepr is not None and item.rep_call.longrepr.reprcrash is not None:
    #     assertionError = item.rep_call.longrepr.reprcrash.message

    domId = item.funcargs["location"] if "location" in item.fixturenames else None

    # reportMessage = f"Task: {taskNumber}, Test Name: {testName}, DOM Id: {domId}, Browser: {browserName}, " \
    #                 f"Viewport: {p['w']}x{p['h']}, Device: {p['display']}, Status: {testResult} ({assertionError})"

    reportMessage = f"Task: {taskNumber}, Test Name: {testName}, DOM Id: {domId}, Browser: {browserName}, " \
                    f"Viewport: {p['w']}x{p['h']}, Device: {p['display']}, Status: {testResult}"

    log(reportMessage)


class ReportWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def log(self, string):
        with open(self.file_path, 'a+') as file:
            file.write(f'\n{string}')


@pytest.fixture(scope='session')
def reportWriter(test_run):
    test_reporter_path = f'{test_run}/traditional-report.txt'
    return ReportWriter(test_reporter_path)


@pytest.fixture()
def report_generator(request, test_case, py_config, reportWriter):
    yield
    logTaskReport(reportWriter, py_config, test_case, request.node)

