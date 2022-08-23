from peewee import *

db = SqliteDatabase('utils/misc/anketa.db')


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    user_id = IntegerField(unique=True)

    @classmethod
    def user_exists(cls, user_id):
        query = cls().select().where(cls.user_id == user_id)
        return query.exists()

    @classmethod
    def create_user(cls, user_id):
        user, created = cls.get_or_create(user_id=user_id)
        user.save()

class Blocked(BaseModel):
    user_id = IntegerField(unique=True)

    @classmethod
    def user_exists(cls, user_id):
        query = cls().select().where(cls.user_id == user_id)
        return query.exists()

    @classmethod
    def create_user(cls, user_id):
        blocked, created = cls.get_or_create(user_id=user_id)
        blocked.save()
        
    @classmethod
    def delete_user(cls, user_id):
        qry=Blocked.delete().where(Blocked.user_id==user_id)
        qry.execute()        
        
        
db.create_tables([Users, Blocked])
