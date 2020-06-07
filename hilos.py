import threading,time

def cuenta(h,n,t):
    i=0
    while(i<n):
        time.sleep(t)
        i+=1     #i=i+1
        print("Hilo numero ",h," cuenta numero: ", i,"\n")

t1=threading.Thread(target=cuenta,args=(1,4,0.9))
t2=threading.Thread(target=cuenta,args=(2,6,1.3))
t3=threading.Thread(target=cuenta,args=(3,5,0.3))

t1.start()
t2.start()
t3.start()
