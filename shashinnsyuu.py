
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import numpy as np
import re
import time

chromeoptions=webdriver.ChromeOptions()
chromeoptions.add_argument('###')#header

driver = webdriver.Chrome(chrome_options=chromeoptions)

driver.get('###')#url

time.sleep(20)

pagesource=driver.page_source

id=[]

f=open('###','w')#file name
for i in range(0,25):
    i=i+1
    pagesource=driver.page_source
    find_re = re.compile(r'###', re.DOTALL)#regular expression
    for x in find_re.findall(pagesource):
        id.append(x)
        print(x)
        f.writelines(str(id)+'\n')
    i+=1
    if i > 25:
        break
    driver.find_element_by_css_selector("###").click()#css element
    url=driver.current_url
    time.sleep(10)
print(id)

f.writelines('\n'+'\n')


time.sleep(5)
idlist=list(set(id))#去重
length=len(idlist)
print('参与抽奖总数：', length)
nameit=[]
listit=np.random.randint(0,length,3)
for i in listit:
    nameit.append(idlist[i])
    print(idlist[i])
    f.writelines(idlist[i]+'\n')
print('抽奖结果：',nameit)
f.close()

