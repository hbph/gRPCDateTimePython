import grpc
from concurrent import futures
from datetime import datetime
import time

import dateTime_pb2_grpc
import dateTime_pb2

class DateTimeServicer(dateTime_pb2_grpc.DateTimeServicer):

	def getCurrentDateTime(self, request, context):
		response = dateTime_pb2.DateTimeMsg()
		response.value = str(datetime.now())
		return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

dateTime_pb2_grpc.add_DateTimeServicer_to_server(DateTimeServicer(),server)

print('Starting server, Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
	while True:
		time.sleep(90000)
except KeyboardInterrupt:
	server.stop(0)
