# calculators/calculators.py

import grpc
import calculator_pb2
import calculator_pb2_grpc
from concurrent import futures

class CalculatorServer(
    calculator_pb2_grpc.CalculatorServicer
):
    def add(self, request, context):
        op_1 = request.op_1
        op_2 = request.op_2
        ans = op_1 + op_2
        return calculator_pb2.AddResponse(ans = ans)

    def sub(self, request, context):
        op_1 = request.op_1
        op_2 = request.op_2
        ans = op_1 - op_2
        return calculator_pb2.SubResponse(ans = ans)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()