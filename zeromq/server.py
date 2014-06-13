
import zmq
import random
import sys
import time

port = "5556"
svr_context = zmq.Context()
svr_socket = svr_context.socket(zmq.PAIR)
svr_socket.connect("tcp://localhost:%s" % port)

while True:
    msg = svr_socket.recv()
    print msg
    svr_socket.send("client message to server1")
    svr_socket.send("client message to server2")
    time.sleep(1)