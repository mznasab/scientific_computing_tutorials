from mpi4py import MPI
import os
import socket

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print rank, size, socket.gethostname(), os.getpid()
