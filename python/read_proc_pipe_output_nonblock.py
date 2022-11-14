# Source: https://stackoverflow.com/questions/375427/a-non-blocking-read-on-a-subprocess-pipe-in-python

import subprocess
import shlex
import time
from threading  import Thread
from queue import Queue, Empty

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()
    print("Thread end")

def main():
    cmd = "ping 127.0.0.1 -q"
    proc = subprocess.Popen(
        shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    # p = Popen(['myprogram.exe'], stdout=PIPE, bufsize=1, close_fds=ON_POSIX)
    q = Queue()
    t = Thread(target=enqueue_output, args=(proc.stdout, q))
    t.daemon = True # thread dies with the program
    t.start()
    num = 0
    while True:
        try:  line = q.get_nowait() # or q.get(timeout=.1)
        except Empty:
            print('no output yet')
        else:
            print(line)
        num += 1
        print(num)
        if num == 5:
            break
        time.sleep(0.01)
    proc.kill()
    proc.wait()
    t.join()

if __name__ == '__main__':
    main()
