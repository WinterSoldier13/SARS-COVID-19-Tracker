 
'''PYTHON 2 Script'''


from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options 
#from win10toast import ToastNotifier as toast
import notify2


notify2.init('')



def display():
    time.sleep(1200)
    
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  

    browser = webdriver.Chrome('F://chromedriver_win32/chromedriver.exe',options=chrome_options)
    url='https://www.worldometers.info/coronavirus/'
    browser.get(url)
    x_path='/html/body/div[3]/div[2]/div[1]/div/div[4]/div/span'
    a = browser.find_element_by_xpath(x_path)

    total_cases_world_wide= a.text

    x_path='/html/body/div[3]/div[2]/div[1]/div/div[6]/div/span'
    a = browser.find_element_by_xpath(x_path)

    total_death_world_wide = a.text

    x_path='/html/body/div[3]/div[2]/div[1]/div/div[7]/div/span'
    b = browser.find_element_by_xpath(x_path)
    
     total_recovery_world_wide = b.text

    x_path='/html/body/div[3]/div[3]/div/div[3]/div[1]/div/table/tbody[1]/tr[44]/td[2]'
    a = browser.find_element_by_xpath(x_path)

    total_cases_india= a.text
    n = notify2.Notification("Update","Total WorldWide: "+str(total_cases_world_wide)+"\nTotal WorldWide Recovery: "+str(total_recovery_world_wide)+
                 "\nTotal Deaths WorldWide: "+str(total_death_world_wide)+"\nTotal Cases in INDIA: "+str(total_cases_india),"icon.ico"   # Icon name)
    n.show()
    display()

if __name__ == '__main__':
    display()



 #download any suitable icon of your choice and rename it icon.ico
