import subprocess
cmd = [['ipconfig'], ['tracert','google.com']]

for i in range(len(cmd)):
    subprocess.run(cmd[i], stdout=open('sub'+i.__str__()+'.txt', 'w'))
