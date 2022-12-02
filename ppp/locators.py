from selenium.webdriver.common.by import By


locator = {
    "login": (By.ID, "login-button"),
    "Username": (By.ID, "user-name"),
    "password": (By.ID, "password"),


    "add_to_cart_backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
    "add_to_cart_bike_light": (By.ID, "add-to-cart-sauce-labs-bike-light"),
    "add_to_cart_bolt_tshirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
    "add_to_cart_fleece_jacket": (By.ID, "add-to-cart-sauce-labs-fleece-jacket"),
    "add_to_cart_onesie": (By.ID, "add-to-cart-sauce-labs-onesie"),
    "add_to_cart_red_tshirt": (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"),

    "shopping_cart_link": (By.CLASS_NAME, "shopping_cart_link"),

    "continue_shopping_button": (By.ID, "continue-shopping"),
    "checkout_button": (By.ID, "checkout"),

    "First_Name": (By.ID, "first-name"),
    "Last_Name": (By.ID, "last-name"),
    "Zip_Postal_Code": (By.ID, "postal-code"),
    "CONTINUE_button": (By.ID, "continue"),

    "FINISH_button": (By.ID, "finish"),
    "BACK_HOME_button": (By.ID, "back-to-products"),
    "menu_button": (By.ID, "react-burger-menu-btn"),
    "logout_button": (By.ID, "logout_sidebar_link"),

}
