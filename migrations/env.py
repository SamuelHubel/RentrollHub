from logging.config import fileConfig

from alembic import context

from hub.db import engine

if context.config.config_file_name:
    fileConfig(context.config.config_file_name)

# Raw T-SQL migrations, no ORM autogenerate, so no target_metadata.
if context.is_offline_mode():
    context.configure(url=engine.url, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()
else:
    with engine.connect() as connection:
        context.configure(connection=connection)
        with context.begin_transaction():
            context.run_migrations()
