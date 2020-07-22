#This code is essentially wrote using selenium and python with time module. Don't forget to get the browser Driver and store in the directory
#where you have this code or you will need to modify the path. 
# pip install selenium --> for installing selenium
# I had problems with using selenium with chromium so check this for webdriver manager-- >  https://github.com/bonigarcia/webdrivermanager
# also google didn't allow me to login because i was using selenium, so if you cant login. close the opened tab. go to gmail and 
# login manually with your username and password and send 2-4 emails from the selenium browser. It will be verified then. thatss what worked for me.


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import time
import signal



# Code will stop executing after 720 seconds == 10 mins.
signal.alarm(720) 



now = datetime.datetime.now()
current_time = now.strftime("%H:%M / %A")
 # %A is to get the name of the Day!
justtime = now.strftime("%H:%M")
print (current_time)

#  Code to allow access for Microphone, Camera and notifications
# 0 is disable and 1 is allow.
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1, 
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1, 
"profile.default_content_setting_values.notifications": 1 
})

# Conditions to check time and append if necessary
while justtime !=  "09:50" or justtime != "13:50" or justtime != "15:20" or  justtime != "16:50":
    time.sleep(20)
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M / %A")
    justtime = now.strftime("%H:%M")
    print(justtime)
    if justtime == "09:50" or justtime == "13:50" or justtime == "15:20" or  justtime == "16:50":
        print("Class is going to start in 10 Minutes.")
        break
    
# directing to the link to be visited; The program first logs into gmail for all around access of google services.
def gmail_login():
    driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")
    time.sleep(4)
    driver.find_element_by_xpath("//input[@name='identifier']").send_keys("####EMAIL ADDRESS HERE####")
    time.sleep(2)
        # Next Button:
    driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
    time.sleep(5)
        #Password:
    driver.find_element_by_xpath("//input[@name='password']").send_keys("#your email password herer###")
    time.sleep(2)
        #next button:
    driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
    time.sleep(5)
        # #opening Meet:
    driver.get(sub)
    driver.refresh()
    time.sleep(5)
        # Turning off video 
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div").click()
    time.sleep(5)
        # turning off audio
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div").click()
    time.sleep(180)
        # Join class
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span").click()

# Conditions which checks the time and goes to the classlink if Classes are happening at that time.

# Math Class --> Link Conf.
if current_time == "09:50 / Monday" or current_time == "16:50 / Tuesday" or current_time == "13:50 / Thursday" or current_time == "15:20 / Friday":
    #sub is the class id with the meet link. sub changes with the time accoriding to the class.
    sub = "###hangouts meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver') 
    #you will need to change the executable_path=r'chromedriver' to the path where you have downloaded the chromedriver or any browerdrive. I used chromium for the test.
    gmail_login()
    

# Physics  //not conf.,,,###########
elif current_time == "13:50 / Monday" or current_time == "16:50 / Wednesday":
    sub = " ###hangouts meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    gmail_login()
    

# Nepali --> Link Conf.
elif current_time == "15:20 / Monday" or current_time == "16:50 / Thursday" :
    sub = "###hangouts meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    gmail_login()
    

#Chemistry RDP -->Link Conf.
elif current_time == "16:50 / Monday" or current_time == "15:20 / Wednesday":
    sub = "###hangouts meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    gmail_login()
    

#Chemistry SM ---> Link Conf.
elif current_time == "13:52 / Tuesday" or current_time == "16:50 / Friday":
    sub = "###hangouts meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    gmail_login()
    

# English --> Link Conf.
elif current_time == "15:20 / Tuesday" or current_time == "13:50 / Friday":
    sub = "###hangouts meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    gmail_login()
    

# Physics MR -->Link Conf.
elif current_time == "13:50 / Wednesday" or current_time == "15:20 / Thursday":
    sub = "###hangouts meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    gmail_login()
    

else:
    print("No classes right now")


    
