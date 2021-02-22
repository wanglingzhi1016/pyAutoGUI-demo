[Python] PyAutoGUI - 拟人的自动化操作工具

拟人的自动化操作工具，可以控制键盘和鼠标

## 官网
https://pyautogui.readthedocs.io/

## 安装
```bash
pip install PyAutoGUI
```
## 基本使用方法

### 获取基础信息
```python
import pyautogui
# 屏幕大小
size = pyautogui.size()
print(size)
# 鼠标位置
mouse_pos = pyautogui.position()
print(mouse_pos)
# 判断鼠标坐标(100, 100)是否在屏幕内
print(pyautogui.onScreen(100, 100))
```

### 鼠标移动
```python
import pyautogui
size = pyautogui.size()
# 把鼠标移动到(10, 10)的位置，周期1秒
pyautogui.moveTo(10, 10, duration=1)
# 把鼠标一到屏幕中央，周期0.5秒
pyautogui.moveTo(size.width/2, size.height/2, duration=0.5)
# 鼠标相对移动，周期1秒
pyautogui.moveRel(100, 0, duration=1)
```

### 实时获取鼠标的位置
```python
import pyautogui
# 上一次鼠标的位置
last_pos = pyautogui.position()
try:
  while True:
    new_pos = pyautogui.position()
    if last_pos != new_pos:
      print(new_pos)
      last_pos = new_pos
except:
  print('\n退出')
```

### 鼠标移动加点击
```python
import pyautogui
import time
# 系统准备时间
time.sleep(2)
# 获取帮助菜单的位置(随便在屏幕上截个图命名为btn_help.png，此方法会找到这张图片的坐标)
help_pos = pyautogui.locateOnScreen("btn_help.png")
goto_pos = pyautogui.center(help_pos)
# 移动鼠标
pyautogui.moveTo(goto_pos, duration=0.5)
# 点击【帮助】按钮
pyautogui.click()
# 移动鼠标到(590, 588)这个位置[关于]
pyautogui.moveTo(590, 588, duration=0.5)
# 再点击
pyautogui.click()
```

### 键盘输入
```python
import pyautogui
import time
# 系统准备时间
time.sleep(2)
# 点击一次编辑器
pyautogui.click(button='left')
# 输入
pyautogui.typewrite('I like python')
# 输入回车，继续输入内容
pyautogui.typewrite('\nI like python too.', 0.25)
# 输入【good】, 然后将头文字改为大写G,然后在行尾写个句号
pyautogui.typewrite(['g','o','o','d','left','left','left','backspace','G','end','.'], 0.25)
# 输入中文【全军出击】
p = 'q u a n j u n c h u j i 1'.split(' ')
pyautogui.typewrite(p, 0.25)
```

### 组合键使用
```python
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
```