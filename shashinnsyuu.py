
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import numpy as np
import re
import time

chromeoptions=webdriver.ChromeOptions()
chromeoptions.add_argument('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')

driver = webdriver.Chrome(chrome_options=chromeoptions)

driver.get('https://www.weibo.com/5261779502/Hf028knLs?type=repost')

time.sleep(20)

pagesource=driver.page_source

#print(driver.page_source)

id=[]
#<div class="WB_text"><a target="_blank" href="https://weibo.com/5417654583" usercard="id=5417654583" node-type="name">桥七一生推</a>：
f=open('shashinnsyuu.txt','w')
for i in range(0,25):
    i=i+1
    pagesource=driver.page_source
    find_re = re.compile(r'<div class="WB_text"><a target="_blank" href="https://weibo.com.+?" usercard="id=.+?" node-type="name">(.+?)</a>', re.DOTALL)
    for x in find_re.findall(pagesource):
        id.append(x)
        print(x)
        f.writelines(str(id)+'\n')
    #action_data="[action-data='id=4335750524857914&max_id=4353360649265778&page=%s']"%str(i+1)
    i+=1
    if i > 25:
        break
    #driver.find_element_by_css_selector(action_data).click()
    driver.find_element_by_css_selector("[class='page next S_txt1 S_line1']").click()
    url=driver.current_url
    time.sleep(10)
print(id)

f.writelines('\n'+'\n')


#driver.find_element_by_css_selector("[action-data='id=4335750524857914&max_id=4353360649265778&page=2']").click()
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


#print(pagenaiyou)
