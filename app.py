from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from datetime import time, datetime, timezone, timedelta


"""
Steps:
1. Inspect the site
2. Check if issue was created recently
3. Send message if an issue is found
4. Deploy with cronjob on VPS
"""

# params
url = "https://gitlab.com/groups/gitlab-org/-/issues/?sort=created_date&state=opened&label_name%5B%5D=frontend&label_name%5B%5D=quick%20win&label_name%5B%5D=Community%20contribution&first_page_size=100"


options = Options()
# comment below line to watch process
# options.add_argument("--headless")
options.page_load_strategy = "normal"

# driver = webdriver.Chrome(
#     service=ChromeService(ChromeDriverManager().install()), options=options
# )

# driver.get(url)
# sleep(5)

# issued_date_element = driver.find_element(
#     By.XPATH,
#     "//div[@class='issuable-main-info']/div[@class='issuable-info']/span[2]/span[2]/span",
# )
# issued_date_string = issued_date_element.get_attribute("title")
issued_date_string = "22 December 2023 at 05:02:27 GMT+11"

print(issued_date_string)

formatted_date_string = issued_date_string.split("G")[0]

print(formatted_date_string)

date_object = datetime.strptime(formatted_date_string, "%d %B %Y at %H:%M:%S ")
print(type(date_object))
print(date_object)  # printed in default format
