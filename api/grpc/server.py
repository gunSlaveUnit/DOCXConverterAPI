import asyncio
import logging
from concurrent import futures

import grpc

import merger_pb2
import merger_pb2_grpc
from merger import clear_files_directory, combine_documents


class GRPCDOCXMerger(merger_pb2_grpc.MergerServicer):
    def Merge(self, request, context):
        response = combine_documents(request.docs)
        clear_files_directory()
        return merger_pb2.MergeResponse(doc=response)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    merger_pb2_grpc.add_MergerServicer_to_server(GRPCDOCXMerger(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
