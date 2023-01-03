from api.grpc.merger_pb2_grpc import MergerServicer


class GRPCDOCXMerger(MergerServicer):
    def merge(self, request, context):
        print(request)
        print(context)
