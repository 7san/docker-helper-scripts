import os

t = []

i=0
while i<100:

  x = os.popen("docker swarm join-token worker --rotate").read()
  i = i+1

  l = x.split(" ")
  t.append(l[26])

#print t

f = open("swarm_tokens.txt", 'w')

for item in t:
  f.write("%s\n" % item)


