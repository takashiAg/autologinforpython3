import urllib
import urllib.request as urllib2
import base64
import time
import socket

username=""
password=""
for line in open('login', 'r'):
    item=line.split(",")
    username=item[0]
    password=item[1]


print(username)
print(password)
basiclogin=base64.b64encode((username+":"+password).encode('ascii')).decode('utf-8')
print(basiclogin)

while 1:
    print(socket.gethostbyname(socket.gethostname()))
    if socket.gethostbyname(socket.gethostname())[0:4]=="172.":
        try:
            url="https://secwall.tokyo-ct.ac.jp:6082/php/uid.php?vsys=1&url=http://wiki.ros.org%2fja"
            data='inputStr=&escapeUser=%s&user=%s&passwd=%s&ok=Login'%(username,username,password)
            res=urllib2.urlopen(url,data.encode('ascii'),timeout=5).read()
            print(res)
            time.sleep(30.0)
        except:
            print("error")
            time.sleep(1.0)
    else:
        try:
            req=urllib2.Request("http://login.tokyo-ct.ac.jp/hello",headers={'Authorization': "Basic "+basiclogin})
            res=urllib2.urlopen(req).read()
            print(res)
            time.sleep(25.0)
        except:
            print("error")
            time.sleep(2.0)
