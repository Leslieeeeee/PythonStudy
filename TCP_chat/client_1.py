from Tkinter import *
import socket, threading

def acceptMessage(sock, text):
    while True:
        text.insert(END, "[Other's Message] : "+ sock.recv(1024)+"\n")
class Chat:
    def __init__(self):
        window = Tk()
        window.title("Chat")
        self.text = Text(window)
        self.text.pack()
        frame1 = Frame(window)
        frame1.pack()
        label = Label(frame1,text="Enter your Message: ")
        self.Message = StringVar()
        entryMessage = Entry(frame1, textvariable=self.Message)
        btSend = Button(frame1, text='Send', command=self.processSendButton)
        btLink = Button(window, text="Link", command=self.processLinkButton)
        btLink.pack()
        label.grid(row=1, column=1)
        entryMessage.grid(row=1, column=2)
        btSend.grid(row=1, column=4)
        self.text.insert(END, "\t\t\t\t----------------\n\t\t\t\t\tme to Chat \n\t\t\t\tEnjoy yourself \n\t\t\t\t-------------------\n\n\n")
        window.mainloop()


def porcessLinkButton(self):
    host = socket.gethostname()
    port = 12345
    self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    self.s.connect((host,port))
    self.text.insert(END,'Linked\n')
    t = threading.Thread(target=acceptMessage, args=(self.s, self.text))
    t.start()
#为什么这里不用
# if __init__ =="__main__":
Chat()