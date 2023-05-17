from src import app, Form, File, UploadFile
from src import BaseModel, List
from src import Optional

#creating file
@app.post('/files_create')
async def files_create(file:Optional[bytes] = File(None, description="File will be read in bytes")):
    if not file:
        return "file not found"
    return {file:len(file)}


#uploading a file
@app.post('/file_upload')
async def file_create(file: Optional[UploadFile] = File(None, description= "File not Uploaded")):
    if not file:
        return "file not found"
    return {'filename':file.filename}


#Creating Multiple files
@app.post('/create_multiple_files')
async def create_multiple_files(files: List[bytes] = File(None, description="File will be read in bytes")):
   
    return {"filesize":[len(file) for file in files]}

#upload multiple files
@app.post('/upload_multiple_files')
async def upload_muliple_fies(files: List[UploadFile] = File(..., description= "Uploaded Mulitiple files")):
    
    return {"filenames":[file.filename for file in files]}




