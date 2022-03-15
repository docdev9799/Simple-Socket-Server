import socket
import json
  
from _thread import *
import threading
  
print_lock = threading.Lock()

def getdef(data):
    f = open('data.json',)
    dictionary = json.load(f)
    for s in range(len(dictionary['dictionary'])):
      if dictionary['dictionary'][s]["term"] == data.decode('ascii'):
        f.close()
        return "The definition of {} is {}.".format(dictionary['dictionary'][s]["term"], dictionary['dictionary'][s]["definition"])
      elif s == len(dictionary['dictionary'])-1 and dictionary['dictionary'][s]["term"] != data.decode('ascii'):
        f.close()
        return "Error: Term does not exist!"
  
def threaded(c):
    while True:
            data = c.recv(1024)
            if not data:
                print_lock.release()
                break
    
            data = getdef(data).encode('ascii')
    
            c.send(data)
  
    c.close()
  
  
def Main():
    host = '127.0.0.1'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    s.listen(5)
    print("socket is listening")

    while True:

        c, addr = s.accept()

        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        start_new_thread(threaded, (c,))
  
if __name__ == '__main__':
    Main()