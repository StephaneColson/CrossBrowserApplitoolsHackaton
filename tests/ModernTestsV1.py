from applitools.selenium import Target


def test_modern_approach_demo_task1(py, py_eyes):
    try:
        # Navigate to the url we want to test
        py.visit("https://demo.applitools.com/gridHackathonV2.html")

        # Call Open on eyes to initialize a test session
        py_eyes.open(py.webdriver, "Cross Browser Testing Demo App", "Task 1", {"width": 800, "height": 600})

        # Check the app page
        py_eyes.check("", Target.window().fully().with_name("Cross-Device Elements Test"))

        # Call Close on eyes to let the server know it should display the results
        py_eyes.close_async()
    except Exception as e:
        py_eyes.abort_async()
        print(e)



