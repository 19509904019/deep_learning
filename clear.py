import datetime
import os
import subprocess
import time

from pykeyboard import PyKeyboard

while True:
    start = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(start)
    subprocess.Popen(r"D:\安全管家\QQPCMgr\15.5.23009.217\QQPCRealTimeSpeedup.exe")
    keyboard = PyKeyboard()
    keyboard.tap_key(keyboard.alt_key, n=2, interval=0.1)  # 点击小键盘5

    time.sleep(300)
    os.system("cls")
