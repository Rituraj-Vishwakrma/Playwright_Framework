class BasePage:

    def __init__(self, page):
        # This is a constructor (runs automatically when object is created)
        # 'page' is Playwright page object (browser tab)
        # We store it so all methods in this class can use it
        self.page = page

    def navigate(self, url):
        # This method is used to open any URL in browser
        # Example: login_page.navigate("https://example.com")
        self.page.goto(url)

    def fill(self, locator, value):
        # This method types text into an input field
        # locator = element selector (like #username)
        # value = text to enter (like "admin")
        # Example: fill("#username", "admin")
        self.page.fill(locator, value)

    def click(self, locator):
        # This method clicks on a button or any clickable element
        # locator = selector of the element
        # Example: click("#login-button")
        self.page.click(locator)

    def get_text(self, locator):
        # This method gets text from an element
        # Used for validation (assertions)
        # Example: get_text(".title") → "Products"
        return self.page.text_content(locator)