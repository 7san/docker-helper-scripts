import docker
import threading
import random
import multiprocessing

client = docker.from_env()

#this value currently hardcoded
image = "dock.location.com/example"

#brief list of things to fuzz
cmds = [["ls","-a"],["echo", "hello", "world"],["/bin/sh"],["echo", "hello",">","test.txt"],["touch", "hello.test"]]


def run_cmd():
  #print("thread")
  cmd = random.choice(cmds)
  print(cmd)
  client.containers.run(image, cmd)

#threading version
for i in range(100):
  t = threading.Thread(target = run_cmd)
  t.start()

'''
#multiprocessing version
jobs = []
for i in range(100):
  p = multiprocessing.Process(target = run_cmd)
  jobs.append(p)
  p.start()
'''

exit()
