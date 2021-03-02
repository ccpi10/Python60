from gpiozero import LED
from time import sleep
import network
import socket

def clearled():
    led1.off()
    led2.off()
    led3.off()

def main():
    s = socket.socket()
    ai = socket.getaddrinfo("0.0.0.0", 8080)
    addr = ai[0][-1]
    
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    s.bind(addr)
    s.listen(5)
    print("Listening, connect your brower to http://<this host>:8080/")
    
    while True:
        
        html= b"""\
HTTP/1.0 200 OK

<body><font size='+6'>%s From Hello Raspberry3</font></body>!
"""

        html2= b"""\
HTTP/1.0 200 OK

<body><font size='+6'>Hello Raspberry3</font></body>!
# <br/>
# <input type='button' id='bt1' name='bt1' value='send' onclick='fun1()' style='width:200px;height:100px;'/>
# </body>!
"""

        try:
            res = s.accept()
            client_s = res[0]
            req =str(client_s.recv(4096))
            
            chin=req.split("/?t1=")
            len1=len(chin)
            
            if len1>1:
                
                kdata=chin[1].split(" ")
                result=kdata[0]
                
                if result=="1":
                    k="LED-1".encode()
                    clearled()
                    led1.on()
                
                if result=="2":
                    k="LED-2".encode()
                    clearled()
                    led2.on()
                
                if result=="3":
                    k="LED-3".encode()
                    clearled()
                    led3.on()
                
                if result=="4":
                    k="LED ALL ON".encode()
                    clearled()
                    led1.on()
                    led2.on()
                    led3.on()
                    led4.on()
                    led5.on()
                if result=="5":
                    k="LED ALL OFF".encode()
                    clearled()
                    
                clinet_s.send(html % k)
            else:
                clearled()
                client_s.send(html2)
                
            client_s.close()
        except:
            client_s.send(html % k)

led1=LED(5)
led2=LED(6)
led3=LED(26)
led4=LED(19)
led5=LED(22)
clearled()
main()
        


            