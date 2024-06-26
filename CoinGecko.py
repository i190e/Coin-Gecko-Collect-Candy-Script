from random import randint
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

# Programm Function
# Search ico function 
def searchIco(icoPath: str , click_Needed: bool):
  for i in range(1,5,1):
   posIco_Button = imagesearch(icoPath)
   if (posIco_Button[0] != -1):
    if(click_Needed==True): # if need Click - click on ico
     pyautogui.moveTo(posIco_Button[0]+4, posIco_Button[1]-60, duration = 1)
     pyautogui.click()
     time.sleep(randint(1,3))
     break
    else:
     return True # return True if ico found
  return False # return False if ico not found

# Write message to log file
def writeToFile(filePath: str, messageString: str):
 with open(filePath, "a") as logFile:
    logFile.write("\n")
    logFile.write(messageString)
 return



# Programm body
logfile =  work_path + "BotLogFile.log"    # log file path
is_accessible = os.access(logfile,os.F_OK) # Check access to file

writeToFile(logfile,"Bot Start at: " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
writeToFile(logfile,"File Access: " + str(is_accessible))
writeToFile(logfile,"Log file path: " + logfile)

#open CoinGeckoUrl start
webbrowser.open(CoinGeckoCandyUrl)
writeToFile(logfile,"Open URL: " + CoinGeckoUrl)
time.sleep(randint(5,10))
#open CoinGeckoUrl end


#check login status start
if (searchIco(LoginTrue_Button,False)):
    loginStatus=True
    writeToFile(logfile,"Login status: " + str(loginStatus))
else:
    writeToFile(logfile,"Login not confirmed")
time.sleep(randint(5,10)) 
#check login status end

#login status false start
if loginStatus==False:
  writeToFile(logfile,"Attempt Login")
if (searchIco(LoginButton_Button,True)):
  writeToFile(logfile,"LoginButton_Button found")
  time.sleep(randint(1,3))

 # attempt login if auto fill enabled and work
if (searchIco(RememberMeCheckBox_Button,False)):
  writeToFile(logfile,"RememberMeCheckBox enable")
  time.sleep(randint(1,3))
else:
  writeToFile(logfile,"RememberMeCheckBox enabled not found")
  time.sleep(randint(1,3))

 # write code to enable check box if empty (create ico for seach)
 #
 #
if (searchIco(LoginGreenButton_Button,True)):
  writeToFile(logfile,"LoginGreenButton_Button found")
  time.sleep(randint(1,3))
time.sleep(randint(7,10))

if (searchIco(CapchaCheck_Button,False)):
  writeToFile(logfile,"CapchaCheck found")
  time.sleep(randint(1,3))
time.sleep(randint(5,10))

if (searchIco(CapchaCheckBox_Button,True)):
  writeToFile(logfile,"CapchaCheckBox_Button found")
  time.sleep(randint(1,3))
time.sleep(randint(5,10))

#login status false end

#repeat check login status start
if (searchIco(LoginTrue_Button,False)):
    loginStatus=True
    writeToFile(logfile,"Login attempt status: " + str(loginStatus))
else:
    writeToFile(logfile,"Attempt Login not confirmed")
time.sleep(randint(5,10)) 
#repeat check login status end


#login status true start
if loginStatus==True:
 if (searchIco(CandyPod_Button,True)):
    writeToFile(logfile,"posCandyPod_Button found")
    time.sleep(randint(1,3))
 time.sleep(randint(2,6))
  
#collected  start
 if (searchIco(CandyCollect_Button,True)):
    writeToFile(logfile,"Candy Collected")
 time.sleep(randint(2,6))  
#collected end

  
 #collected status check start
 if (searchIco(TodayGreen_Button,False)):
    writeToFile(logfile,"Collected Confirmed")
    collectedStatus=True
 time.sleep(randint(2,6))
 #collected status check end 
  
 #collected status false start
 if collectedStatus==False: 
  writeToFile(logfile,"Collected Not Corfimed")
  collectedStatus=False
 
  #collected status false end 
#login status true end

#close CoinGeckoUrl start
time.sleep(randint(2,5))
pyautogui.click() #return focus to page if change
time.sleep(randint(1,3))
pyautogui.hotkey("ctrl", "w") # close tab
time.sleep(randint(1,3))
#close CoinGeckoUrl end
writeToFile(logfile,"Bot End at: " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


