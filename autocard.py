from selenium import webdriver as wd
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC

# Create a new instance of Firefox driverabs
driver = wd.Firefox()
wait = WebDriverWait(driver, 10)
# go to the google home page
driver.get("http://www.ebay.com")

driver.implicitly_wait(10)

signInLink = driver.find_element_by_link_text("Sign in")

signInLink.click()

userName = "hohshoes"
password = "suzanne1"

userIDform = driver.find_element_by_id("userid")
userIDform.send_keys(userName)

passwordForm = driver.find_element_by_id("pass")
passwordForm.send_keys(password)

signInButton = driver.find_element_by_id("sgnBt")

signInButton.click()

action = AC(driver)
myEbayMenu = driver.find_element_by_link_text("My eBay")
action.move_to_element(myEbayMenu).perform()
wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Selling"))).click()
#selling = driver.find_element_by_link_text("Selling")
#action.move_to_element(selling).perform()

sell = driver.find_element_by_link_text("Sell")
sell.click()

createListing = driver.find_element_by_xpath("(//button[@type='button'])[6]")
createListing.click()

singleListing = driver.find_element_by_link_text("Single listing")
singleListing.click()

driver.switch_to.frame(0)
titleSelling = driver.find_element_by_id("w0-find-product-search-bar-search-field")
year = "1982"
brand = "Topps"
player = "Joe Deer"
team = "Oakland Athletics"
cardNo = "414"
sport = "Baseball"
condition = "NM-MNT"
itemSelling = "Original " + year + " " + brand + " " + player + " " + team + " #" + cardNo + " " + sport + " card " + condition
titleSelling.send_keys(itemSelling)

getStarted = driver.find_element_by_xpath("//div[2]/div/div/button")
getStarted.click()

cont = driver.find_element_by_css_selector("div.continue-without-product > button.btn")
cont.click()

# find the element that's name attribute is q (the google search box)
#inputElement = driver.find_element_by_name("q")

# type in the search
#inputElement.send_keys("Cheese!")

# submit the form (although google automatically searches now without submitting)
#inputElement.submit()

# the page is ajaxy so the title is originally this:
print(driver.title)

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

    # You should see "cheese! - Google Search"
    print(driver.title)

finally:
    driver.quit()
