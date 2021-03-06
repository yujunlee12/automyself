from selenium import webdriver
import pyautogui as pt
import time
import pyperclip
def auto(x,y,t):
    time.sleep(1)
    pt.moveTo(x,y,duration=t)
    pt.click()
#dr=webdriver.Chrome()
pt.FAILSAFE=False
op=webdriver.ChromeOptions()
op.add_argument("--start-maximized")
dr=webdriver.Chrome(options=op)
dr.get("https://hcs.eduro.go.kr/#/relogin")
auto(903,697,1)
pt.click()
auto(681,443,1)
auto(743,884,1)#시, 도 설정
auto(675,569,1)
auto(676,815,1)#학력 설정
auto(765,687,1)
pyperclip.copy("양지고등학교")
pt.hotkey('ctrl','v')
auto(1592,697,1)
auto(388,852,1)
pt.scroll(-500)
auto(1038,883,1)#설정 완료
auto(911,843,1)
pyperclip.copy("이유준")
pt.hotkey('ctrl','v')
auto(862,995,1)
pyperclip.copy("050624")
pt.hotkey('ctrl','v')
pt.scroll(-600)
auto(1120,659,1)#개인정보 입력 완료
auto(1192,591,1)
pyperclip.copy("7862")
pt.hotkey('ctrl','v')
auto(1102,761,1)#비밀번호 입력
auto(537,971,1)
for i in range(5):
    pt.scroll(-200)
auto(139,864,1)
for i in range(12):
    pt.scroll(-300)
auto(124,446,1)
auto(124,779,1)
auto(857,910,1)
