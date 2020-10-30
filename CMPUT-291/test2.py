pid = "p99999"
pid = int(pid[1:]) + 1
newpid = "P"
for i in range(3 - len(str(pid))):
    newpid += '0'
newpid += str(pid)
print(newpid)