import socket
import random
from threading import Thread
import datetime

# from colorama import Fore, init, Back






name = input("Enter your name: ")


SERVER_HOST = "127.0.0.1" # you will need to change this to Felix`s macbook IP if you want to connect. 
SERVER_PORT = 30000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print(f"connecting to {SERVER_HOST} on port {SERVER_PORT}")
try:
    s.connect((SERVER_HOST, SERVER_PORT))
except Exception:
    print("server is not on try checking later")
print(f"connected to {SERVER_HOST}")





# thread_2c
# waits for messges from the sever, then prints them out for the user
def listen_for_messge():
    while True:
        messge = s.recv(1024).decode()
        print(f"{messge}\n")
# create a diffrent thread so listen_for_messge can run in the backround while the main messge loop continues to run

# thread_1
# this is where you will send your messges to the server
def main_loop():
    command = commands(name)
    while True:
    # input a messge you want to send to other ppl in the chat room or a command
        try:
            messge = str(input("\n"))
        except KeyboardInterrupt:
            command.resolve("/Quit")
        
        command.resolve(messge)




class commands():

    def __init__(self, name) -> None:
        self.name = name
        self.command_set = {"/List" : self.List, "/Quit" : self.Quit, "/Name" : self.Name, "/Help" : self.Help}

# find out if messge is command or a messge

    

    def resolve(self, messge) -> None:
        self.messge = messge
        try:
            if self.messge[0] == "/":
                
                    self.command_set[self.messge]()
                    # fix, need spisific exseption
                
                    print("that command does not exist")
            else:
                self.send_messge(self.messge)
        except IndexError:
            return None
    
    
    def Help(self) -> None:
        print("""
                \nonline chat room for sending messges to other ppl, have fun and keep conversations respectable.\n
                commands:\n
                    # /Help displays all commands.
                    # /Quit  quits the program
                    # /List lists all connected clients
                    # /Name prompts you to enter your name again\n
              """)
        
        
    def Quit(self) -> None:
        print("quiting program...")
        self.send_messge()
        exit()
        
    
    def List(self) -> None:
        self.send_messge()
    
    def Name(self) -> None:
        self.name = input("Enter new name: ")
        self.send_messge()
        



    def send_messge(self, messge) -> None: 
        messge = f"{self.name}<wep>{messge}"
        s.send(messge.encode())
        


# create a diffrent thread so listen_for_messge can run in the backround while the main messge loop continues to run
t = Thread(target=listen_for_messge, daemon=True)

t.start()



# start main_loop with main thread
main_loop()


