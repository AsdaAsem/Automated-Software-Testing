import time

from selenium import webdriver
from locators import locator
from csv import reader

driver = webdriver.Firefox()

driver.implicitly_wait(10)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

with open('data.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=',')

    # successful login and buying items
    line1 = next(csvreader)
    driver.find_element(*locator["Username"]).send_keys(line1[0])
    time.sleep(1)
    driver.find_element(*locator["password"]).send_keys(line1[1])
    time.sleep(1)
    assert driver.find_element(*locator["login"]).is_displayed()
    driver.find_element(*locator["login"]).click()
    time.sleep(1)

    driver.find_element(*locator["add_to_cart_backpack"]).click()
    time.sleep(1)
    driver.find_element(*locator["add_to_cart_bike_light"]).click()
    time.sleep(1)
    driver.find_element(*locator["add_to_cart_bolt_tshirt"]).click()
    time.sleep(1)
    driver.find_element(*locator["add_to_cart_fleece_jacket"]).click()
    time.sleep(1)
    driver.find_element(*locator["add_to_cart_onesie"]).click()
    time.sleep(1)
    driver.find_element(*locator["add_to_cart_red_tshirt"]).click()
    time.sleep(1)

    driver.find_element(*locator["shopping_cart_link"]).click()
    time.sleep(1)
    driver.find_element(*locator["checkout_button"]).click()
    time.sleep(1)
    # testing checkout fields
    with open('checkout_data.csv') as csvfile2:
        csvreader2 = reader(csvfile2, delimiter=',')
        for row in csvreader2:
            driver.find_element(*locator["First_Name"]).send_keys(row[0])
            time.sleep(1)
            driver.find_element(*locator["Last_Name"]).send_keys(row[1])
            time.sleep(1)
            driver.find_element(*locator["Zip_Postal_Code"]).send_keys(row[2])
            time.sleep(1)
            driver.find_element(*locator["CONTINUE_button"]).click()
            time.sleep(1)
            driver.refresh()

    driver.find_element(*locator["FINISH_button"]).click()
    time.sleep(1)
    driver.find_element(*locator["BACK_HOME_button"]).click()
    time.sleep(1)

    # successful login but not buying anything
    driver.find_element(*locator["shopping_cart_link"]).click()
    time.sleep(1)
    driver.find_element(*locator["checkout_button"]).click()
    time.sleep(1)
    # testing checkout fields
    with open('checkout_data.csv') as csvfile2:
        csvreader2 = reader(csvfile2, delimiter=',')
        for row in csvreader2:
            driver.find_element(*locator["First_Name"]).send_keys(row[0])
            time.sleep(1)
            driver.find_element(*locator["Last_Name"]).send_keys(row[1])
            time.sleep(1)
            driver.find_element(*locator["Zip_Postal_Code"]).send_keys(row[2])
            time.sleep(1)
            driver.find_element(*locator["CONTINUE_button"]).click()
            time.sleep(1)
            driver.refresh()

    driver.find_element(*locator["FINISH_button"]).click()
    time.sleep(1)
    driver.find_element(*locator["BACK_HOME_button"]).click()
    time.sleep(1)

    driver.find_element(*locator["menu_button"]).click()
    time.sleep(1)
    driver.find_element(*locator["logout_button"]).click()
    time.sleep(1)


    # unsuccessful login (username but no password)
    line2 = next(csvreader)
    driver.find_element(*locator["Username"]).send_keys(line2[0])
    time.sleep(1)
    driver.find_element(*locator["password"]).send_keys(line2[1])
    time.sleep(1)
    assert driver.find_element(*locator["login"]).is_displayed()
    driver.find_element(*locator["login"]).click()
    time.sleep(1)

    driver.refresh()

    # unsuccessful login (no username but just a password)
    line3 = next(csvreader)
    driver.find_element(*locator["Username"]).send_keys(line3[0])
    time.sleep(1)
    driver.find_element(*locator["password"]).send_keys(line3[1])
    time.sleep(1)
    assert driver.find_element(*locator["login"]).is_displayed()
    driver.find_element(*locator["login"]).click()
    time.sleep(1)

    driver.refresh()

    #unsuccessful login (no username no password)
    line4 = next(csvreader)
    driver.find_element(*locator["Username"]).send_keys(line4[0])
    time.sleep(1)
    driver.find_element(*locator["password"]).send_keys(line4[1])
    time.sleep(1)
    assert driver.find_element(*locator["login"]).is_displayed()
    driver.find_element(*locator["login"]).click()
    time.sleep(1)

    driver.refresh()

#unsccessful login with diffrent username locked_out_user

    line5 = next(csvreader)
    driver.find_element(*locator["Username"]).send_keys(line5[0])
    time.sleep(1)
    driver.find_element(*locator["password"]).send_keys(line5[1])
    time.sleep(1)
    assert driver.find_element(*locator["login"]).is_displayed()
    driver.find_element(*locator["login"]).click()
    time.sleep(1)
    driver.refresh()
# unccessful login with diffrent username locked_out_user wrong password
    line6 = next(csvreader)
    driver.find_element(*locator["Username"]).send_keys(line6[0])
    time.sleep(1)
    driver.find_element(*locator["password"]).send_keys(line6[1])
    time.sleep(1)
    assert driver.find_element(*locator["login"]).is_displayed()
    driver.find_element(*locator["login"]).click()
    time.sleep(1)
    driver.refresh()


#successful login with diffrent username problem_user
    line7 = next(csvreader)
    driver.find_element(*locator["Username"]).send_keys(line7[0])
    time.sleep(1)
    driver.find_element(*locator["password"]).send_keys(line7[1])
    time.sleep(1)
    assert driver.find_element(*locator["login"]).is_displayed()
    driver.find_element(*locator["login"]).click()
    time.sleep(1)

    driver.find_element(*locator["add_to_cart_backpack"]).click()
    time.sleep(1)
    driver.find_element(*locator["add_to_cart_bike_light"]).click()
    time.sleep(1)
    driver.find_element(*locator["add_to_cart_bolt_tshirt"]).click()
    time.sleep(1)
    driver.find_element(*locator["add_to_cart_fleece_jacket"]).click()
    time.sleep(1)
    driver.find_element(*locator["add_to_cart_onesie"]).click()
    time.sleep(1)
    driver.find_element(*locator["add_to_cart_red_tshirt"]).click()
    time.sleep(1)

    driver.find_element(*locator["shopping_cart_link"]).click()
    time.sleep(1)
    driver.find_element(*locator["checkout_button"]).click()
    time.sleep(1)

    # testing checkout fields
    with open('checkout_data.csv') as csvfile2:
        csvreader2 = reader(csvfile2, delimiter=',')
        line7 = next(csvreader2)
        driver.find_element(*locator["First_Name"]).send_keys(line7[0])
        time.sleep(1)
        driver.find_element(*locator["Last_Name"]).send_keys(line7[1])
        time.sleep(1)
        driver.find_element(*locator["Zip_Postal_Code"]).send_keys(line7[2])
        time.sleep(1)
        driver.find_element(*locator["CONTINUE_button"]).click()
        time.sleep(1)
        driver.find_element(*locator["menu_button"]).click()
        time.sleep(1)
        driver.find_element(*locator["logout_button"]).click()
        time.sleep(1)
#successful login with diffrent username performance_glitch_user
    line8 = next(csvreader)
    driver.find_element(*locator["Username"]).send_keys(line8[0])
    time.sleep(1)
    driver.find_element(*locator["password"]).send_keys(line8[1])
    time.sleep(1)
    assert driver.find_element(*locator["login"]).is_displayed()
    driver.find_element(*locator["login"]).click()
    time.sleep(1)
    driver.find_element(*locator["shopping_cart_link"]).click()
    time.sleep(1)
    driver.find_element(*locator["checkout_button"]).click()
    time.sleep(1)
    with open('checkout_data.csv') as csvfile2:
        csvreader2 = reader(csvfile2, delimiter=',')
        line7 = next(csvreader2)
        driver.find_element(*locator["First_Name"]).send_keys(line7[0])
        time.sleep(1)
        driver.find_element(*locator["Last_Name"]).send_keys(line7[1])
        time.sleep(1)
        driver.find_element(*locator["Zip_Postal_Code"]).send_keys(line7[2])
        time.sleep(1)
        driver.find_element(*locator["CONTINUE_button"]).click()
        time.sleep(1)
        driver.find_element(*locator["menu_button"]).click()
        time.sleep(1)
        driver.find_element(*locator["logout_button"]).click()
        time.sleep(1)




#unsccessful login with diffrent username performance_glitch_user wrong password
    line9 = next(csvreader)
    driver.find_element(*locator["Username"]).send_keys(line9[0])
    time.sleep(1)
    driver.find_element(*locator["password"]).send_keys(line9[1])
    time.sleep(1)
    assert driver.find_element(*locator["login"]).is_displayed()
    driver.find_element(*locator["login"]).click()
    time.sleep(1)
    driver.refresh()
#unsccessful login username standard_user and wrong password
    line10 = next(csvreader)
    driver.find_element(*locator["Username"]).send_keys(line10[0])
    time.sleep(1)
    driver.find_element(*locator["password"]).send_keys(line10[1])
    time.sleep(1)
    assert driver.find_element(*locator["login"]).is_displayed()
    driver.find_element(*locator["login"]).click()
    time.sleep(1)
    driver.refresh()

# driver.quit()
