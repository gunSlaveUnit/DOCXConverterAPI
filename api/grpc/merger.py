import asyncio
import os
import shutil
import sys
from typing import List

from docxcompose.composer import Composer
from docx import Document
from fastapi import UploadFile
from fastapi.responses import FileResponse

ROOT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
FILES_DIRECTORY = os.path.join(ROOT_DIRECTORY, 'files')


def get_file_data(filename: str) -> bytes:
    with open(os.path.join(ROOT_DIRECTORY, filename), 'rb') as file:
        return file.read()


def combine_documents(files: List[bytes]):
    if len(files) == 0:
        return bytes()

    if len(files) == 1:
        return files[0]

    store_files(files)
    filenames = [
        os.path.join(FILES_DIRECTORY, ''.join(['filename', str(file_index)])) for file_index in range(len(files))
    ]

    combine(filenames[0], filenames[1:])

    return get_file_data('combined.docx')


def store_files(files: List[bytes]):
    if not os.path.exists(FILES_DIRECTORY):
        os.makedirs(FILES_DIRECTORY, exist_ok=True)

    for file_index, file_binary_data in enumerate(files):
        with open(os.path.join(FILES_DIRECTORY, ''.join(['filename', str(file_index)])), 'wb') as document:
            document.write(file_binary_data)


def combine(master_document: str, files: List[str]) -> None:
    master = Document(master_document)
    composer = Composer(master)

    for file in files:
        document = Document(file)
        composer.append(document)

    composer.save(os.path.join(ROOT_DIRECTORY, "combined.docx"))


def clear_files_directory():
    for filename in os.listdir(FILES_DIRECTORY):
        file_path = os.path.join(FILES_DIRECTORY, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


if __name__ == '__main__':
    combine_documents(sys.argv[1], sys.argv[2:])
