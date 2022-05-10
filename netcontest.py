import psutil
pi = psutil.pids()

for p in pi:
    try:
        #print("trying", p)
        cons = psutil.Process(p).open_files()
    except psutil.NoSuchProcess:
        continue
    except psutil.AccessDenied:
        print(p)
    else:
        if cons:
            print(cons)
#print(psutil.net_connections())

