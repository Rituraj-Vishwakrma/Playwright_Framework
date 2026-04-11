def take_screenshot(page, name):
    # Function to take screenshot of the current browser page
    # page → Playwright page object (browser tab)
    # name → name of the screenshot file (given by user)
    # page.screenshot() is a Playwright built-in method
    # It captures the current screen of the browser
    # path= defines where the screenshot will be saved
    # f"reports/{name}.png" is a formatted string (f-string)
    # It dynamically creates file path like:
    # "reports/login_failed.png"
    # reports/ → folder where screenshots will be stored
    # {name} → dynamic file name passed in function
    # .png → file format of screenshot image
    page.screenshot(path=f"reports/{name}.png")
    # 🔍 3. What  does / mean?
    #  👉 / means: Go inside this folder”
        # Example:
    # If function is called as:
    # take_screenshot(page, "login_error")
    #
    # Then screenshot will be saved as:
    # reports/login_error.png

    # This function is mainly used for:
    # - Debugging test failures
    # - Capturing proof of execution
    # - Reporting issues