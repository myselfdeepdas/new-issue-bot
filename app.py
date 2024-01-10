from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import time
from time import sleep

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

driver = webdriver.Chrome(options=options)
driver.get(url)
sleep(5)

issuable_info = driver.find_element(
    By.XPATH,
    "//div[@class='issuable-main-info']/div[@class='issuable-info']/span[2]/span[2]/span",
)
content = issuable_info.get_attribute("title")

print(content)

"""
$x("//div[@class='issuable-main-info']/div[@class='issuable-info']/span[2]/span[2]")
driver.find_element(By.XPATH, "//input[@value='f']")
"""


"""<span title="15 December 2023 at 12:01:13 GMT-8" data-testid="issuable-created-at">
                3 weeks ago
              </span>"""
