
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.makemytrip.com/railways/'
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.binary_location = './/CFT driver/chrome-win64/chrome.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url)
driver.maximize_window()


# Check if you have landed on the correct page
if "MakeMyTrip" in driver.title:
    print("Landed on the correct page")

# Print the URL and Title of the Page
print("Current URL:", driver.current_url)
print("Current Title:", driver.title)



# Click on FROM
from_city_element = driver.find_element(By.ID, "fromCity")
from_city_element.click()
from_city_element.send_keys("NDLS")

# Enter the city in FROM: DELHI
from_city_input = driver.find_element(By.ID, "react-autowhatever-1-section-0-item-0")
from_city_input.click()
from_city_input.send_keys(Keys.RETURN)

# Click on TO
to_city_element = driver.find_element(By.ID, "toCity")
to_city_element.click()
to_city_element.send_keys("LKO")

# Enter the city in TO: LUCKNOW
to_city_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/input')
to_city_input.click()
to_city_input.send_keys(Keys.RETURN)

# Click on Travel Date
travel_date_element = driver.find_element(By.ID, "travelDate")
travel_date_element.click()

# Select a date: 20 May
date_picker_element = driver.find_element(By.XPATH, "//td[text()='20']")
date_picker_element.click()

# Click on class
class_element = driver.find_element(By.ID, "travelFor")
class_element.click()

# Select a class from dropdown: Third AC.
third_ac_element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div[4]/label/span').click()
select_third_ac_element = driver.find_element(By.XPATH, '//*[@id="travelFor"]').click()

# Click on SEARCH Button
search_button_element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[2]/p/a')
search_button_element.click()

# Close the browser when done
driver.quit()



