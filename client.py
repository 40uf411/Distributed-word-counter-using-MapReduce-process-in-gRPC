import sys
import os
import grpc

import driver_pb2 as driver
import driver_pb2_grpc as driver_grpc

import worker_pb2 as worker
import worker_pb2_grpc as worker_grpc

import time


def run():
    pid = os.getpid()
    
    channel = grpc.insecure_channel('localhost:4000')

    try:
        print("[*] Connecting to the server...")
        grpc.channel_ready_future(channel).result(timeout=10)
    except grpc.FutureTimeoutError:
        sys.exit('[-] [ERROR] Could not connect to the server.')
    else:
        print("[!] Connection established.")
        arg = sys.argv
        
        # stub = worker_grpc.WorkerStub(channel)
        # req = stub.setDriverPort(worker.driverPort(port=50))
        ## Testing worker
        # req = stub.die(worker.empty())
        # r = worker.mapInput(path='./inputs/pg-dorian_gray.txt', mapID=1, m=5)
        # req = stub.map(r)
        # r = worker.rid(id=1)
        # req = stub.reduce(r)
        
        ## Testing driver
        stub = driver_grpc.DriverStub(channel)
        ports = '|'.join(arg[3:])
        req = driver.launchData(dirPath=arg[1], m=int(arg[2]), ports=ports)
        response = stub.launchDriver(req)
        print("[!] Operation terminated with code: %i and message: %s"%(response.code, response.msg))

if __name__ == "__main__":
    run()