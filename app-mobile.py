import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse

# Function to validate the URL format
def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# Prompt the user for the URL of the website and validate it
while True:
    url = input("Enter the URL of the website you want to visit: ")
    if is_valid_url(url):
        break
    else:
        print("Invalid URL format. Please enter a valid URL.")

# Define user agents for mobile Chrome
mobile_chrome_user_agents = [
    "Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Mobile; rv:98.0) Gecko/98.0 Firefox/98.0 Mobile Safari/98.0",
    "Mozilla/5.0 (Linux; Android 9; Mobile; rv:97.0) Gecko/97.0 Firefox/97.0 Mobile Safari/97.0",
    "Mozilla/5.0 (Linux; Android 8.1; Mobile; rv:96.0) Gecko/96.0 Firefox/96.0 Mobile Safari/96.0",
    "Mozilla/5.0 (Linux; Android 8.1; Mobile; rv:95.0) Gecko/95.0 Firefox/95.0 Mobile Safari/95.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; Mobile; rv:98.0) Gecko/98.0 Firefox/98.0 Mobile Safari/98.0",
    "Mozilla/5.0 (Linux; Android 10; Mobile; rv:97.0) Gecko/97.0 Firefox/97.0 Mobile Safari/97.0",
]

# Initialize a Selenium webdriver with a random mobile user agent
def get_random_user_agent(user_agents_list):
    return random.choice(user_agents_list)

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={get_random_user_agent(mobile_chrome_user_agents)}")
options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'})  # Simulate iPhone X
driver = webdriver.Chrome(options=options)

# Define the scrolling function using JavaScript
def scroll_down(driver):
    driver.execute_script("window.scrollBy(0, 500);")  # Scroll down by 500 pixels

# Visit the URL at 10-minute intervals, scroll through the page, and change user agent
try:
    while True:
        driver.get(url)
        time.sleep(random.uniform(5, 10))  # Wait for a random time before scrolling

        for _ in range(random.randint(5, 15)):  # Scroll a random number of times
            scroll_down(driver)

        time.sleep(random.uniform(5, 10))  # Wait for a random time before the next visit

        # Change user agent for the next visit
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-agent={get_random_user_agent(mobile_chrome_user_agents)}")
        options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'})
        driver = webdriver.Chrome(options=options)
except KeyboardInterrupt:
    pass

# Close the WebDriver when done
driver.quit()
