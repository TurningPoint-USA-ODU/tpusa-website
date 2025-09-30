from os import getenv


def get_secret(secret_id: str, backup: str | int | None = None) -> str | None:
    backup_id: str | None = str(backup) if backup else None
    if getenv(secret_id, backup_id):
        return getenv(secret_id, backup_id)
    return backup_id


if get_secret("PIPELINE") == "production":
    from .production import *

else:
    from .local import *
