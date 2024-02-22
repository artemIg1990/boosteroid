from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import env
import time
import logging


def logging_configuration():
    logging.basicConfig(
        level=logging.INFO, filename=env.logging_filename, filemode=env.logfilemode
    )  # can be set to DEBUG, INFO, WARNING, ERROR, CRITICAL


logging_configuration()


def tear_down(driver):
    try:
        driver.close()
        logging.info(f"{time.strftime("%y_%m_%d_%H:%M:%S")} Driver closed")
    except:
        logging.error(f"Unable to close driver. Error: {Exception()}")


def screenshot(driver, screenshot_page=""):
    try:
        driver.save_screenshot(f"{screenshot_page}_{time.strftime("%y_%m_%d_%H.%M.%S")}.png")
        logging.info("Screenshot done")
    except(Exception.args):
        logging.error(f"Failed to take screenshot. url: {driver.current_url} \n Error: {Exception}")


def wait_for_element(driver, element_xpath="/html/body", await_time=10):
    try:
        element = WebDriverWait(driver, await_time).until(
            ec.presence_of_element_located((By.XPATH, element_xpath))
        )
        time.sleep(1)
    except:
        logging.error(f"{time.strftime("%H:%M:%S")} element not found. Element xpath: {element_xpath}")
        tear_down(driver)


def run_driver():
    selected_env = int(input(f"type 1 to run on stage \ntype 2 to run on sandbox \nto abort process type 0 \n"))
    if selected_env == 0:
        print("Process finished")
        logging.info(f"{time.strftime("%H:%M:%S")} Manually finished")
        return
    elif selected_env == 1:
        basic_url = env.stage["url"]
        login = env.stage["login"]
        password = env.stage["password"]
        logging.info(f"Selected env == stage. Execution started at {time.strftime("%y_%m_%d_%H:%M:%S")}")
    elif selected_env == 2:
        basic_url = env.sandbox["url"]
        login = env.sandbox["login"]
        password = env.sandbox["password"]
        logging.info(f"Selected env == sandbox. Execution started at {time.strftime("%y_%m_%d_%H:%M:%S")}")
    elif selected_env == 5:
        basic_url = "http://cloud.boosteroid.com/"
        login = "a.ihnatenko@boosteroid.com"
        password = "123123123"
        logging.info(f"Selected env == PROD. Execution started at {time.strftime("%y_%m_%d_%H:%M:%S")}")
    else:
        print("teardown")
        logging.info("finishing process. No valid env selected")
        return
    try:
        driver = webdriver.Firefox()
        logging.info(f"driver created. {time.strftime("%y_%m_%d_%H:%M:%S")}")
    except:
        logging.error(
            f". Execution started at {time.strftime("%y_%m_%d_%H:%M:%S")}\n Failed to create driver. Error: {Exception}")
        return
    try:
        driver.get(basic_url)
        wait_for_element(driver)
    except:
        logging.error(
            f". Execution started at {time.strftime("%y_%m_%d_%H:%M:%S")} \nFailed to find element. \n Finishing process \nError: {Exception}")
        tear_down(driver)
    return {"driver": driver, "login": login, "password": password}


def object_interact(driver, element_xpath, value=""):
    wait_for_element(driver, element_xpath)
    try:
        interacted_element = driver.find_element(By.XPATH, element_xpath)
        logging.debug(f"{time.strftime("%H:%M:%S")}  Element found. Element xpath: {element_xpath}")
        if interacted_element.tag_name == "input":
            interacted_element.click()
            interacted_element.send_keys(value)
            logging.info(f"{time.strftime("%H:%M:%S")} Interacted with {element_xpath}. Sent {value}")
        elif interacted_element.tag_name == "svg-icon" or "button":
            interacted_element.click()
            logging.info(f"{time.strftime("%H:%M:%S")} Interacted with {element_xpath}. Clicked")
        elif interacted_element.tag_name == "button":
            interacted_element.click()
        else:
            print(f'Unknown element type. XPATH: {element_xpath}, role: {interacted_element.tag_name}')
    except:
        logging.error(f"{time.strftime("%H:%M:%S")} Unable to interact element. Element: {element_xpath}. "
                      f"Error: {Exception}")


def get_object_value(driver, element_xpath):
    try:
        interacted_element = driver.find_element(By.XPATH, element_xpath)
        if interacted_element.type == "checkbox":
            logging.info(
                f"{time.strftime("%H:%M:%S")}. Element value is {driver.find_element(By.XPATH, element_xpath).is_enabled()}")
            return interacted_element.is_selected()
        else:
            print(f"can't find text")
    except:
        logging.info(f"{time.strftime("%H:%M:%S")} Unable to get value of element. Element xpath: {element_xpath}")
