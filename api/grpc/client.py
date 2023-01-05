import os

import grpc

import merger_pb2
import merger_pb2_grpc

ROOT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def get_file_data(filename: str) -> bytes:
    with open(os.path.join(ROOT_DIRECTORY, filename), 'rb') as file:
        return file.read()


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = merger_pb2_grpc.MergerStub(channel)
        response = stub.Merge(
            merger_pb2.MergeRequest(
                docs=[data := get_file_data(filename) for filename in ['boo.docx', 'foo.docx']]
            )
        )
        print("Client received: ", response.doc)


if __name__ == '__main__':
    run()
