import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_btn_addtocart(browser):
    browser.get(link)
    cart_btn = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert cart_btn, "Add to card button not found"
    time.sleep(15)
