import time
from pynput.keyboard import Key, Controller
import clipboard  # 用于获取剪贴板内容

keyboard = Controller()

# 打印提示符
print("准备")
# 休眠5秒后, 开始进行粘贴, 模拟脚本精灵
time.sleep(5)

# 循环执行50次
for i in range(3):
    # 获取剪贴板内容
    clipboard_content = clipboard.paste()
    print(clipboard_content)   
    # 模拟粘贴操作
    keyboard.press(Key.cmd)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.cmd)
    
    # 模拟回车键
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
    # 延迟一些时间以确保操作完成
    time.sleep(1)


