from typing import List

import grpc

import merger_pb2
import merger_pb2_grpc


def get_file_data(files: List[str]) -> bytes:
    for filename in files:
        with open(filename, 'rb') as file:
            yield file.read()


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = merger_pb2_grpc.MergerStub(channel)
        response = stub.Merge(
            merger_pb2.MergeRequest(
                docs=[get_file_data(['boo.docx', 'foo.docx'])]
            )
        )
        print("Client received: ", response.doc)


if __name__ == '__main__':
    run()
