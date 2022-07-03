from peewee import *
import os
import datetime

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"), user=os.getenv("MYSQL_USER"),
                     password=os.getenv("MYSQL_PASSWORD"), host="178.128.229.22", port=3306)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb
