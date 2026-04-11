from pages.login_page import LoginPage
# Import LoginPage class (Page Object Model)
from utils.data_reader import read_json
# Import utility function to read JSON test data
def test_valid_login(page):
    # Test function
    # 'page' is provided by pytest fixture (browser tab)

    data = read_json("test_data/login_data.json")
    # Read JSON file and store data in variable
    # data becomes a Python dictionary

    login = LoginPage(page)
    # Create object of LoginPage--it's came from page--LoginPage class
    # Pass Playwright page (browser) to it

    login.open_website()
    # Open application URL (using navigate method internally)

    login.Login(
        data["valid_User"]["username"],
        data["valid_User"]["password"]
    )
    # Perform login action
    # Fetch username and password from JSON data
    # data["valid_user"]["username"] → "standard_user"

    assert "Products" in login.get_inventory_text()
    # Validate login success
    # get_inventory_text() gets text from page
    # Check if "Products" is present after login