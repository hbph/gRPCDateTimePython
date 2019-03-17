import grpc

import dateTime_pb2
import dateTime_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = dateTime_pb2_grpc.DateTimeStub(channel)

dt = dateTime_pb2.DateTimeMsg(value='')

response = stub.getCurrentDateTime(dt)

print(response.value)
