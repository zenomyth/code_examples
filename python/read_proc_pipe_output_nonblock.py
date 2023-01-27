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
    # cmd = "ls -1"
    # cmd = "cat read_proc_pipe_output_nonblock.py"
    proc = subprocess.Popen(
        shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    # p = Popen(['myprogram.exe'], stdout=PIPE, bufsize=1, close_fds=ON_POSIX)
    q = Queue()
    t = Thread(target=enqueue_output, args=(proc.stdout, q))
    t.daemon = True # thread dies with the program
    t.start()
    start_time = time.monotonic()
    timeout = 5
    proc_normal_end = True
    while True:
        try:  line = q.get_nowait() # or q.get(timeout=.1)
        except Empty:
            # print('no output yet')
            pass
        else:
            print(line)
        if proc.poll() != None:
            break
        if timeout != None and time.monotonic() - start_time > timeout:
            proc_normal_end = False
            break
        time.sleep(0.01)
    if not proc_normal_end:
        proc.kill()
        proc.wait()
    t.join()
    if proc_normal_end:
        while not q.empty():
            line = q.get()
            print(line)

if __name__ == '__main__':
    main()
