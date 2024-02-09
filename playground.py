from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import time, datetime, timezone, timedelta


# params
url = "https://gitlab.com/groups/gitlab-org/-/issues/?sort=created_date&state=opened&label_name%5B%5D=frontend&label_name%5B%5D=quick%20win&label_name%5B%5D=Community%20contribution&first_page_size=100"


options = Options()
# comment below line to watch process
# options.add_argument("--headless")
# options.page_load_strategy = "normal"

# driver = webdriver.Chrome(
#     service=ChromeService(ChromeDriverManager().install()), options=options
# )

# driver.get(url)
# sleep(10)

# issued_date_element = driver.find_element(
#     By.XPATH,
#     "//div[@class='issuable-main-info']/div[@class='issuable-info']/span[2]/span[2]/span",
# )

# WebDriverWait(driver, 20).until(EC.presence_of_element_located((issued_date_element)))
# issued_date_string = issued_date_element.get_attribute("title")

issued_date_string = "22 December 2023 at 05:02:27 GMT+11"


formatted_date_string = issued_date_string.split("G")[0]


date_object = datetime.strptime(formatted_date_string, "%d %B %Y at %H:%M:%S ")

# pywhatkit.sendwhatmsg("+17734599211", "New GitLab Issue!!", 22, 28)


current_time = datetime.now()
new_time = current_time + timedelta(minutes=1)


hour = new_time.hour
minute = new_time.minute

issued_date_string = "December 21, 2023 at 10:02:27 AM PST"
formatted_date_string = issued_date_string.split("A")[0]
issued_date_object = datetime.strptime(formatted_date_string, "%B %d, %Y at %I:%M:%S ")
print(issued_date_object)

# parse the HTML element to convert to datetime object
issued_date_string = issued_date_element.get_attribute("title")
formatted_date_string = issued_date_string.split("G")[0]

# convert string to datetime object
issued_date_object = datetime.strptime(formatted_date_string, "%d %B %Y at %H:%M:%S ")
