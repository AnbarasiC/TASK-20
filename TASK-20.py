'''Using Python Selenium and the URL https://www.cowin.gov.in/ you have to:-

1) Click on the "Create "FAQ" and "Partners" anchor tags present on the Home page
and open two new windows.
2) Now, you have to fetch the opened Windows/Frame ID and display the same
on the console.
3) Kindly close the two new windows and come back to the Home page also.'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class CowinWebsite:
    # Set up the driver
    def __init__(self):
        self.driver = webdriver.Chrome()

    # Open the URL
    def open_website(self):
        self.driver.get("https://www.cowin.gov.in/")
        self.driver.maximize_window()

    # Finding specific element and perform click action
    def click_link(self, link_text):
        self.driver.find_element(By.XPATH, f"//a[normalize-space()='{link_text}']").click()
        time.sleep(5)

    # Get the window ids using window_handles
    def get_window_ids(self):
        return self.driver.window_handles

    # Switching to specific window
    def switch_to_window(self, window_id):
        self.driver.switch_to.window(window_id)

    # Close the specific window
    def close_current_window(self):
        self.driver.close()

    # Close the browser window
    def quit_browser(self):
        self.driver.quit()

# Creating cowin object for accessing the class CowinWebsite()
cowin = CowinWebsite()

# Click on the "FAQ" and "Partners" anchor tags present on the Home page
cowin.open_website()
cowin.click_link("FAQ")
cowin.click_link("Partners")

# Fetch the opened Windows ID's. WindowsIDs are stored in the form of list.
window_ids = cowin.get_window_ids()
parent_id = window_ids[0]
faq_id = window_ids[1]
partners_id = window_ids[2]

# Print window ID's of opened browser windows
print("Window ID of the home page of CoWIN:", parent_id)
print("Window ID of FAQ page:", faq_id)
print("Window ID of PARTNERS page:", partners_id)

# WindowID is dynamic. So, everytime it will change.

# Closing the opened new windows FAQ and Partners
cowin.switch_to_window(faq_id)
cowin.close_current_window()
time.sleep(5)

cowin.switch_to_window(partners_id)
cowin.close_current_window()
time.sleep(5)

# Switch to the home page of CoWIN
cowin.switch_to_window(parent_id)
time.sleep(5)

# Close the browser window
cowin.quit_browser()