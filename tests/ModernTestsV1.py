from applitools.selenium import Target
from selenium.webdriver.common.by import By


def test_modern_approach_demo_task1(py, py_eyes):
    try:
        # Navigate to the url we want to test
        py.visit(py.config.custom['environment']['url'])

        # Call Open on eyes to initialize a test session
        py_eyes.open(py.webdriver, "Cross Browser Testing Demo App", "Task 1", {"width": 800, "height": 600})

        # Check the app page
        py_eyes.check("Task 1",
                      Target.window().fully().with_name("Cross-Device Elements Test"))

        # Call Close on eyes to let the server know it should display the results
        py_eyes.close_async()
    except Exception as e:
        py_eyes.abort_async()
        print(e)


def test_modern_approach_demo_task2(py, py_eyes):
    try:
        # Navigate to the url we want to test
        py.visit(py.config.custom['environment']['url'])

        # Filter Black Shoes
        filterBlack = py.get('#colors__Black')
        filterBlack.click()
        filterBlack.is_checked()

        py.get('#filterBtn').click()

        # Call Open on eyes to initialize a test session
        py_eyes.open(py.webdriver, "Cross Browser Testing Demo App", "Task 2", {"width": 800, "height": 600})

        # Check the app page
        py_eyes.check("Task 2",
                      Target.region(py.webdriver.find_element_by_id('product_grid')))

        # Call Close on eyes to let the server know it should display the results
        py_eyes.close_async()
    except Exception as e:
        py_eyes.abort_async()
        print(e)


def test_modern_approach_demo_task3(py, py_eyes):
    try:
        # Navigate to the url we want to test
        py.visit(py.config.custom['environment']['url'])

        # Filter Black Shoes
        filterBlack = py.get('#colors__Black')
        filterBlack.click()
        filterBlack.is_checked()
        py.get('#filterBtn').click()

        # Open the first result
        py.find('#product_grid').first().click()

        # Call Open on eyes to initialize a test session
        py_eyes.open(py.webdriver, "Cross Browser Testing Demo App", "Task 3", {"width": 800, "height": 600})

        # Check the app page
        py_eyes.check("Task 3",
                      Target.window().fully().with_name("Product Details test"))

        # Call Close on eyes to let the server know it should display the results
        py_eyes.close_async()
    except Exception as e:
        py_eyes.abort_async()
        print(e)