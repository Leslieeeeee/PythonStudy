#客户端仅能连接一个服务器，而服务器可以连接多个客户端
#服务器多线程处理

#只能单方面开始链接

from Tkinter import *
import socket, threading

def acceptMessage(s, text, theSystem):
    sock, addr = s.accept()
    theSystem.sock =sock
    while True:
        text.insert(END, "[Other's Message] : "+ sock.recv(1024)+"\n")


class Chat:
    def __init__(self):
        host = socket.gethostname()
        port = 12345
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((host, port))
        #监听端口
        self.s.listen(1)
        window = Tk()
        window.itle("Chat")
        self.text = Text(window)
        self.text.pack()
        frame1 = Frame(window)
        frame1.pack()
        label = Label(frame1,text="Enter your Message: ")
        self.Message = StringVar()
        entryMessage = Entry(frame1, textvariable=self.Message)
        btSend = Button(frame1, text='Send', command=self.processSendButton)
        label.grid(row=1, column=1)
        entryMessage.grid(row=1, column=2)
        btSend.grid(row=1, column=4)
        self.text.insert(END, "\t\t\t\t----------------\n\t\t\t\t\tme to Chat \n\t\t\t\tEnjoy yourself \n\t\t\t\t-------------------\n\n\n")
        self.text.insert(END, '[NO PERSON] Wait fro another one\n')
        t = threading.Thread(target=acceptMessage, args=(self.s, self.text, self))
        t.start()
        window.mainloop()

def porcessSendButton(self):
    self.sock.send(self.Message.get())
    self.text.insert(END,'[Your Message] :'+self.Message.get()+"\n")

Chat()



