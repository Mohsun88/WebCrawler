from selenium import webdriver
import time
import re
import pandas as pd

carray = []
darray = []
larray = []
market = []
sarray = []

url = "https://e27.co/startups"
browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
browser.get(url)
for i in range(1,10):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)


links   =  browser.find_elements_by_tag_name('a')
ml      = browser.find_elements_by_xpath('//*[@data-ct]')

for l in links:
    if re.search("/startup/", str(l.get_attribute("href"))):
        larray.append(l)


total = len(larray)
print("Total"+str(total))
k = 0

market2 = []
for link in links:
    if re.search("/startup/", str(link.get_attribute("href"))):
        k += 1
        q = link.get_attribute("outerHTML")

        company = browser.find_elements_by_class_name("company-name")
        cd = browser.find_elements_by_class_name("company-description")
        url = link.get_attribute("href")

        site = browser.find_elements_by_xpath('//*[@id="startup-list"]/div[' + str(k) + ']/div/div[4]/div[2]/a')
        for ss in site:
            sarray.append(ss.get_attribute("href"))

for c in company:
    carray.append(c.text)
    # carray.append(c.text)

for d in cd:
    darray.append(d.text)


df = pd.DataFrame(carray, columns = ['Company Name'])
df2 = pd.DataFrame(darray, columns = ['Company Description'])
df3 = pd.DataFrame(sarray, columns = ['SiteColumn'])

r  = df.join(df2, how="outer")
r2 = r.join(df3, how='outer')
print(r2)
r2.to_csv("crawlerCsv.csv")