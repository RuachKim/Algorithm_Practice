# array = [1,2,3]

# a = [i+1 for i in array]
# print(a)

# from random import *

# customer = {}
# cnt = 0
# for i in range(1,51):
#     drive_t =  randrange(5,51)
#     if drive_t <= 15:
#         print(f"[o] {i}th customer is coming Time : {drive_t}")
#         cnt = cnt+1
#     else:
#         print(f"[x] {i}th customer is coming Time : {drive_t}")

# print(f"Matching customer: {cnt}")

# import sys

# source_file = open("score.txt","r",encoding= "utf8")

# line = source_file.readlines()

# print(line[3:6])

# source_file.close()


#Class - Inherit

#server definition
class Server:
    def __init__(self, perf, Mem):
        self.perf = perf
        self.Mem = Mem
        
#client definition
class Client(Server):
    def __init__(self, perf, Mem, Validity):
        Server.__init__(self,perf,Mem)
        self.Validity = Validity
        if self.Validity == True:
            print("Client is Valid, created now")
        else:
            print("Invalid client, so ends the client now")
    def request(self,target,source):
        input(f"Client {source} is now requesting to calculate, {target} is Valid!")

    def receive(self,target, source):
        if target != source:
            print(f"Client {source} received data from {target}")
            return 1
        else:
            print("Invalid address, please check the link")
            return 0
#usage

Master = Server("2GHz", "512MB")

Slave = Client("1.5GHz","128MB",True)

if Slave.receive("202.30.11.2","202.30.11.2"):
    print("Success!!")
else:
    print("Exit")


