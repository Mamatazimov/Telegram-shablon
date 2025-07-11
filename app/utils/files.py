from app.database.models import File


async def create_file(file_name:str,file_type:str):
    file = await File.create(file=file_name,file_type=file_type)
    return file

async def get_file(file_id:str):
    file = await File.get_or_none(id=file_id)
    if file is None:
        return None
    return file


