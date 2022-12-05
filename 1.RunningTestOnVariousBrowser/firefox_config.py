from selenium import webdriver


def firefox_browser():
    driver = webdriver.Firefox(executable_path="F:\\SoftwareTesting\\Project\\TestAoutomationBITM16\\Drivers\\geckodriver.exe")

    # Open Website
    driver.get("https://www.google.com/")

    # Close Active Tab
    driver.close()




firefox_browser()