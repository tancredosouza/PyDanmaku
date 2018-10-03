#!/usr/bin/env python3
import danmaku
import random
import time
from math import pi, sin

FPS = 60
wait = 1/FPS
previous = time.time()

def framerate():
    global previous, wait, FPS
    now = time.time()
    delta = now - previous
    to_wait = wait - delta
    previous += wait
    if to_wait < 0:
        print('bad'); return
    time.sleep(to_wait)

x = danmaku.DanmakuGroup()
x.add_bullet(320, 240, False, 1, 1, 0, 0, 0, 0.01)
i = 0
try:
    danmaku.init()
    start = time.time()
    i = 0
    while True:
        i+=1
        x.run()
        x.render()
        #framerate()

finally:
    danmaku.close()

