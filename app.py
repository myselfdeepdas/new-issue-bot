from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from datetime import time, datetime, timezone, timedelta
import pywhatkit


# params
url = "https://gitlab.com/groups/gitlab-org/-/issues/?sort=created_date&state=opened&label_name%5B%5D=frontend&label_name%5B%5D=quick%20win&label_name%5B%5D=Community%20contribution&first_page_size=100"
options = Options()
options.add_argument("--headless")
options.page_load_strategy = "normal"
recent_issue = False

# access GitLab issue page
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options
)

driver.get(url)
sleep(10)

# find the element containing when the ticket was issued
issued_date_element = driver.find_element(
    By.XPATH,
    "//div[@class='issuable-main-info']/div[@class='issuable-info']/span[2]/span[2]/span",
)

# parse the HTML element to convert to datetime object
issued_date_string = issued_date_element.get_attribute("title")
formatted_date_string = issued_date_string.split("G")[0]

# convert string to datetime object
issued_date_object = datetime.strptime(formatted_date_string, "%d %B %Y at %H:%M:%S ")

# find the current datetime
current_time = datetime.now()
hour = current_time.hour
minute = current_time.minute

# check if first ticket on page was issued within 24hrs
if current_time - timedelta(hours=24) <= issued_date_object <= current_time:
    recent_issue = True


message_send_time = current_time + timedelta(minutes=1)
hour = message_send_time.hour
minute = message_send_time.minute

pywhatkit.sendwhatmsg("+17734599211", "New GitLab Issue!!", hour, minute)
