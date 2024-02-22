import seleniumMethods
import time
import logging

logging.basicConfig(
    level=logging.INFO, filename=seleniumMethods.env.logging_filename, filemode=seleniumMethods.env.logfilemode
)  # can be set to DEBUG, INFO, WARNING, ERROR, CRITICAL

seleniumMethods.logging_configuration()


def login_positive_flow():
    try:
        driver_list = seleniumMethods.run_driver()
        login_field_xpath = '//*[@id="authLoginEmailField"]'
        seleniumMethods.object_interact(driver_list["driver"], login_field_xpath, driver_list["login"])
        password_field_xpath = '//*[@id="authLoginPasswordField"]'
        seleniumMethods.object_interact(driver_list["driver"], password_field_xpath, driver_list["password"])
        seleniumMethods.screenshot(driver_list["driver"])
        submit_button = '/html/body/app-root/app-auth/div/app-auth-login/form/app-primary-button'
        seleniumMethods.object_interact(driver_list["driver"], submit_button)
        seleniumMethods.wait_for_element(driver_list["driver"])
        seleniumMethods.screenshot(driver_list["driver"])
        seleniumMethods.object_interact(driver_list["driver"],
                                        '/html/body/app-root/app-available-time-modal/div/div[2]/button/svg-icon')
        seleniumMethods.screenshot(driver_list["driver"])
        time.sleep(1)
        return driver_list["driver"]
    except:
        logging.error(f"Logging in flow failed {time.strftime("%H:%M:%S")}. Error: {Exception}")


def remember_me():
    try:
        driver_list = seleniumMethods.run_driver()
        login_field_xpath = '//*[@id="authLoginEmailField"]'
        seleniumMethods.object_interact(driver_list["driver"], login_field_xpath, driver_list["login"])
        password_field_xpath = '//*[@id="authLoginPasswordField"]'
        seleniumMethods.object_interact(driver_list["driver"], password_field_xpath, driver_list["password"])
        seleniumMethods.screenshot(driver_list["driver"])


    except:
        logging.error(f"Failed to remember me {time.strftime("%H:%M:%S")}. Error: {Exception}")

def log_out(driver):
    print("TO DO")

login_positive_flow()
