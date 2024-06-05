from python_imagesearch.imagesearch import imagesearch,imagesearcharea
import webbrowser
import time
import pyautogui
import os
from datetime import datetime


#define variable
work_path =  os.path.dirname(os.path.abspath(__file__))+"\\" # add path to script
loginStatus=False
collectedStatus=False
CoinGeckoUrl="https://www.coingecko.com"
CoinGeckoCandyUrl="https://www.coingecko.com"

ButtonsPath = work_path+"PNG\\Buttons\\" # path to png ico

CandyPod_Button=ButtonsPath+"CandyPod.png"
CandyCollect_Button=ButtonsPath+"CandyCollectButton.png"
CapchaCheck_Button=ButtonsPath+"CapchaCheck.png"
CapchaCheckBox_Button=ButtonsPath+"CapchaCheckBox.png"
EmptyEnterEmailField_Button=ButtonsPath+"EmptyEnterEmailField.png"
EmptyEnterPasswordField_Button=ButtonsPath+"EmptyEnterPasswordField.png"
LoginButton_Button=ButtonsPath+"LoginButton.png"
LoginGreenButton_Button=ButtonsPath+"LoginGreenButton.png"
LoginTrue_Button=ButtonsPath+"LoginTrue.png"
RememberMeCheckBox_Button=ButtonsPath+"RememberMeCheckBox.png"
TodayGreen_Button=ButtonsPath+"TodayGreen.png"
TodayWhite_Button=ButtonsPath+"TodayWhite.png"

logfile =  work_path + "BotLogFile.log"    # log file path
is_accessible = os.access(logfile,os.F_OK)

with open(logfile, "a") as logFile:
    logFile.write("\n")
    logFile.write("Bot Start at: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    logFile.write("\n")
    logFile.write("File Access: " + str(is_accessible))
    logFile.write("\n")
    logFile.write("Log file path: " + logfile)
    logFile.write("\n")
#open CoinGeckoUrl
print("start")
webbrowser.open(CoinGeckoCandyUrl)
print("\nOpen URL ")
with open(logfile, "a") as logFile:
 logFile.write("Open URL: " + CoinGeckoUrl)
 logFile.write("\n")
time.sleep(10)
#open CoinGeckoUrl


#check login status start
for i in range(1,5,1):
 posLoginTrue_Button = imagesearch(LoginTrue_Button)
 if posLoginTrue_Button[0] != -1:
    loginStatus=True
    with open(logfile, "a") as logFile:
     logFile.write("Login status: " + str(loginStatus))
     logFile.write("\n")
    break
 else:
   logFile.write("Login not confirmed")
 time.sleep(10) 
#check login status end




#login status false start
if loginStatus==False:
  with open(logfile, "a") as logFile:
   logFile.write("Attempt Login")
   logFile.write("\n")

#login status false end



#login status true start
if loginStatus==True:
 for i in range(1,5,1):
  posCandyPod_Button = imagesearch(CandyPod_Button)
  if posCandyPod_Button[0] != -1:
    with open(logfile, "a") as logFile:
     logFile.write("posCandyPod_Button found")
     logFile.write("\n")
    print(str(posCandyPod_Button[0])+ " " + str(posCandyPod_Button[1]))
    pyautogui.moveTo(posCandyPod_Button[0]+4, posCandyPod_Button[1]-60, duration = 1)
    pyautogui.click()
    time.sleep(2)
    break
  time.sleep(5)
  
#collected  start
 for i in range(1,5,1):
   posCollect_Button = imagesearch(CandyCollect_Button)
   if posCollect_Button[0] != -1:
    pyautogui.moveTo(posCollect_Button[0]+4, posCollect_Button[1]-60, duration = 1)
    pyautogui.click()
    with open(logfile, "a") as logFile:
     logFile.write("Candy Collected")
     logFile.write("\n")
    break
   time.sleep(5)  
#collected end

  
#collected status check start

 for i in range(1,5,1):
   Collected_Button = imagesearch(TodayGreen_Button)
   if Collected_Button[0] != -1:
    with open(logfile, "a") as logFile:
     logFile.write("Collected Confirmed")
     logFile.write("\n")
    collectedStatus=True
    break
   time.sleep(5)
  #collected status check end 
  
  #collected status false start
 if collectedStatus==False: 
  with open(logfile, "a") as logFile:
   logFile.write("Collected Not Corfimed")
   logFile.write("\n")
  collectedStatus=False
 
  #collected status false end 
#login status true end

#close CoinGeckoUrl start
time.sleep(5)
pyautogui.click() #return focus to page if change
time.sleep(2)
pyautogui.hotkey("ctrl", "w") # close tab
time.sleep(2)
#close CoinGeckoUrl end

with open(logfile, "a") as logFile:
 logFile.write("Bot End at: "+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
 logFile.write("\n")
