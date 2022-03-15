import socket
from tkinter import *

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

root = Tk(className='multi-threaded socket server gui')
root.configure(bg='black')
root.geometry("700x75")
root.resizable(False, False)
e = Entry(root, width=50)
e.pack()
e.insert(0, "dog")
myLabel = (Label(root, text="null"))

def myClick():
  message = e.get()
  if message == 'quit':
    s.close()
    exit()

  s.send(message.encode('ascii'))

  data = s.recv(1024)

  myLabel.config(text=data.decode('ascii'))
  myLabel.pack()
  
  
def Main():

  host = '127.0.0.1'

  port = 12345

  s.connect((host,port))

  while True:
    myButton = Button(root, text="Get Definiton", command=myClick)
    myButton.pack()
    root.mainloop()
  
if __name__ == '__main__':
    Main()