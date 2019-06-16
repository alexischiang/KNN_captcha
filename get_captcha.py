from PIL import Image,ImageEnhance
from selenium import webdriver
import requests
import images

url  = 'http://jwxt.upc.edu.cn/verifycode.servlet'

browser = webdriver.Chrome()
browser.get(url)
loc = browser.find_element_by_tag_name('img').location
left = loc['x']+2
top = loc['y']+2
right = left + 41
bot = top + 17

for index in range(200,401):
    # 保存截图处理
    browser.get_screenshot_as_file('images/full.png')
    browser.refresh()   
    img = Image.open('images/full.png')
    img = img.crop((left,top,right,bot))
    img = img.convert('L')
    threshold = 127
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    img = img.point(table,'1')
    img.save('images/'+ str(index) + '.png')
    # 传入切割
    # 如可切割则保存
    images.import_cutting(index)

browser.quit()

