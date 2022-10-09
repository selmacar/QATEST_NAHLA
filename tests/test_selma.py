from pages.home_page import HomePage
import time


def test_login(driver):
    home_page = HomePage(driver)
    home_page.go_to("https://www.saucedemo.com/")
    home_page.login("standard_user", "secret_sauce")
    assert home_page.get_text() == "PRODUCTS"
    home_page.add_to_cart("add-to-cart-sauce-labs-backpack")
    home_page.add_to_cart("add-to-cart-test.allthethings()-t-shirt-(red)")
    home_page.click("shopping_cart_container")
    assert home_page.get_text() == "YOUR CART"
    assert home_page.get_text_item("item_4_title_link") == "Sauce Labs Backpack"
    assert home_page.get_text_item("item_3_title_link") == "Test.allTheThings() T-Shirt (Red)"
    home_page.click("checkout")
    assert home_page.get_text() == "CHECKOUT: YOUR INFORMATION"
    home_page.checkout("Selma", "Causevic-Arapovic", "71000")
    home_page.click("continue")
    assert home_page.get_text() == "CHECKOUT: OVERVIEW"
    assert home_page.get_text_item("item_4_title_link") == "Sauce Labs Backpack"
    assert home_page.get_text_item("item_3_title_link") == "Test.allTheThings() T-Shirt (Red)"
    home_page.click("finish")
    assert home_page.get_text() == "CHECKOUT: COMPLETE!"
    home_page.click("react-burger-menu-btn")
    home_page.click("logout_sidebar_link")
    home_page.check_login()
    time.sleep(5)



   
   