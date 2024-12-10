from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

# Set up WebDriver for Firefox
driver_path = r"C:\Users\ROBIN\Downloads\geckodriver-v0.35.0-win64\geckodriver.exe"  # Path to GeckoDriver
service = Service(driver_path)
driver = webdriver.Firefox(service=service)

# Your demo website URL
url = "https://divatrends.lovable.app/"

# Simulate multiple visits
try:
    for i in range(10):  # Number of simulated visits
        print(f"Visit {i + 1}")
        driver.get(url)  # Open the website
        time.sleep(5)    # Stay on the page for 5 seconds
finally:
    driver.quit()  # Close the browser after visits
