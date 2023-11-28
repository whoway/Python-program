from pynput.keyboard import Key, Controller as KeyboardController, Listener
import time 
import pyperclip
import clipboard  

kb = KeyboardController()
timestamp_win = 0

# 为了解决百度如流,字节飞书等软件在浏览器里面没有多级标题快捷键的问题


def on_press(key):
    global timestamp_win
    try:  
        # 首先按下ctrl的时候, 下面监测的是mac电脑的ctrl而不是command
        if key == Key.ctrl:     
            timestamp_win = time.time()

        # 接着按下对应标题的时候
        target = ['1', '2', '3', '4', '5', '6', '7', '8']
        if key.char in target:
            if time.time() - timestamp_win < 0.5:
                # Todo
                # 获取剪切板内容以备恢复
                print("ctrl+", key.char)
                # 往剪切板传递 n个 #号
                str= int(key.char)*'#'
                pyperclip.copy(str)
                # clipboard.paste()
                kb.press(Key.cmd)
                kb.press('v')
                kb.release('v')
                kb.release(Key.cmd)
                # Todo
                # 恢复代码
                # pyperclip.copy(save_old)

    except AttributeError:      
        pass

def on_release(key): 
    if key == Key.esc: 
        return False

while True:
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
