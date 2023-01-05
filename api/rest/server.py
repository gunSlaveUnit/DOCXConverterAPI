from typing import List

from fastapi import FastAPI, UploadFile

from utils.merger import combine_documents, clear_files_directory

app = FastAPI()


@app.post('/converter/merge')
async def merge(files: List[UploadFile]):
    response = await combine_documents(files)
    clear_files_directory()
    return response
