import pyautogui
import time
# 系统准备时间
time.sleep(2)
# 每个动作间隔0.5秒
pyautogui.PLASE = 0.5
# 记事本打出三行内容
pyautogui.click(button="left")
pyautogui.typewrite('hello')
pyautogui.typewrite('\nhello')
pyautogui.typewrite('\nhello')
# 按下ctrl键
pyautogui.keyDown('ctrl')
# 按下a键，全选
pyautogui.press('a')
# 按下c键，复制
pyautogui.press('c')
# 松开ctrl键
pyautogui.keyUp('ctrl')
# 点击记事本，放开全选内容
pyautogui.click()
# 输入两个空行
pyautogui.typewrite('\n\n')
# 粘贴
pyautogui.hotkey('ctrl', 'v')