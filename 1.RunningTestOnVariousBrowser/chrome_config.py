from selenium import webdriver

def chrome_browser():
    driver = webdriver.Chrome(executable_path="F:\SoftwareTesting\Project\TestAoutomationBITM16\Drivers\chromedriver.exe")

    # Open Website
    driver.get("https://www.google.com/")

chrome_browser()