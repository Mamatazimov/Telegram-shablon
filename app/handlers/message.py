import os
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from app.keyboards.inline import choose_kb
from app.utils.files import create_file


async def document_converter(message: Message):
    try:
        from main import bot

        file = message.document

        file_name = file.file_name
        file_extension = os.path.splitext(file_name)[-1].lower()
        data={
            ".docx": [".pdf", ".txt",".odt",".rtf"],
            ".txt": [".pdf",".odt",".docx",".rtf"],
            ".html": [".pdf"],
            ".pdf": [".jpg", ".docx",".txt"],
            ".odt": [".pdf",".txt",".docx",".rtf"],
            ".rtf": [".txt",".docx",".odt"]
        }

        if file_extension in data.keys():
            f = await bot.get_file(file.file_id)
            file_path = f.file_path
            fn=f"{file.file_id}_{file_name}"

            db_file = await create_file(file_name=fn,file_type="docs")

            await bot.download_file(file_path=file_path,destination=f"app/files/docs/{fn}")
            await message.answer("Choose file!",reply_markup=choose_kb(typ="docs",ff=file_extension,files=data[file_extension],fn=db_file.id))
        else:
            await message.answer("Sorry but bot cannot convert this file!")
    except Exception as e:
        if "Bad Request: file is too big" in str(e):
            await message.answer(f"Your file size has exceeded the telegram bots limit!")



