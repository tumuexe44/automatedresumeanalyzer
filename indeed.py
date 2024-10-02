from selenium import webdriver
from bs4 import BeautifulSoup

# Webdriver başlatma
driver = webdriver.Chrome(executable_path='your_chrome_driver_path')
url = 'https://www.linkedin.com/jobs'
driver.get(url)

# Sayfa kaynağını alma
soup = BeautifulSoup(driver.page_source, 'html.parser')

# İş ilanlarını parse etme (örnek bir yapı)
job_titles = soup.find_all('h3', class_='job-title')

for job in job_titles:
    print(job.text.strip())

driver.quit()
