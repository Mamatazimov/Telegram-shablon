from tortoise import Tortoise


async def init_db():
    # Here we connect to a SQLite DB file.
    # also specify the app name of "models"
    # which contain models from "app.models
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['app.database.models']}
    )
    await Tortoise.generate_schemas()

