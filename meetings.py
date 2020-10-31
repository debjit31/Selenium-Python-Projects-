from selenium import webdriver
import pyperclip as pc
import time
import csv

def signIn():
    username = "debjitchatterjee31@outlook.com"
    password = "Debjit#31"
    signinBtn = driver.find_element_by_xpath('//a[@class = "c-button f-secondary ow-slide-in ow-slide-in-2 xs-ow-mr-0 ow-mt-10 ow-txt-trans-upper ow-bvr-signin"]')
    signinBtn.click()
    time.sleep(10)
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    time.sleep(2)
    email_input = driver.find_element_by_xpath('//input[@name = "loginfmt"]')
    email_input.send_keys(username)
    time.sleep(3)
    next = driver.find_element_by_xpath('//input[@id = "idSIButton9"]')
    next.click()
    time.sleep(6)
    pass_input = driver.find_element_by_xpath('//input[@id = "i0118"]')
    pass_input.send_keys(password)
    time.sleep(2)
    sign_in = driver.find_element_by_xpath('//input[@id = "idSIButton9"]')
    sign_in.click()
    time.sleep(4)
    no_btn = driver.find_element_by_xpath('//input[@id = "idBtn_Back"]')
    no_btn.click()
def createandJoinMeeting():
    meet = driver.find_element_by_xpath('//button[@id = "app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c"]')
    meet.click()
    time.sleep(2)
    start_a_meeting = driver.find_element_by_xpath('//button[@title = "Start a meeting right away."]')
    start_a_meeting.click()
    time.sleep(10)

    camera_off = driver.find_element_by_xpath('//span[@title = "Turn camera off"]')
    camera_off.click()
    time.sleep(2)
    audio_off = driver.find_element_by_xpath('//span[@title = "Mute microphone"]')
    audio_off.click()
    time.sleep(2)
    join_meeting = driver.find_element_by_xpath('//button[@class = "join-btn ts-btn inset-border ts-btn-primary"]')
    join_meeting.click()
    time.sleep(4)
    share_invite = driver.find_element_by_xpath('//button[@class = "ts-btn ts-btn-fluent ts-btn-fluent-with-icon ts-btn-fluent-secondary create-team"]')
    share_invite.click()
    time.sleep(2)
    copy_meeting_link = driver.find_element_by_xpath('//button[@class = "button-box shadow-level-1"]')
    copy_meeting_link.click()
    link = pc.paste()
    cl = driver.find_element_by_xpath('//button[@class = "ts-sym icons-close app-icons-fill-hover app-icons-fill-focus inset-border inset-border-round inset-border-themed"]')
    cl.click()
    print("Meeting URL :- {}".format(link))
    time.sleep(2)
    return link
def sendMeetingLink(url):
    driver.execute_script("window.open('https://web.whatsapp.com/');")
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(15)
    for name in names:
        chat = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
        chat.click()
        time.sleep(2)
        input_box = driver.find_element_by_xpath('//div[@class = "_3uMse"]')
        time.sleep(2)
        input_box.send_keys(url)
        time.sleep(2)
        send = driver.find_element_by_xpath('//button[@class = "_1U1xa"]')
        send.click()
        time.sleep(2)

names = []
with open('names.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        names.append(row[0])

options = webdriver.ChromeOptions()
options.add_argument("use-fake-ui-for-media-stream")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.microsoft.com/en-in/microsoft-365/microsoft-teams/group-chat-software')
time.sleep(8)
signIn()
time.sleep(40)
url = createandJoinMeeting()
time.sleep(3)
sendMeetingLink(url)
driver.quit()