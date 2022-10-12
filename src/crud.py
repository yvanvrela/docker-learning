from . import schema
from . import models
from sqlalchemy.orm import Session


def create_user(user: dict, db:Session):
    db_user = models.User(name=user['name'])
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return schema.UserOut(
        id=db_user.id,
        name=db_user.name,
    )


def users(db:Session):
    db_users = db.query(models.User).all()

    list_users = [
        schema.UserOut(
            id=user.id,
            name=user.name,
        )
        for user in db_users
    ]

    return list_users
