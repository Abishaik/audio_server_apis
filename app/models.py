from mongoengine import Document, StringField,IntField ,ListField ,FileField

class Song(Document):
    ID = IntField(required=True)
    name = StringField(max_length=100,required=True)
    duration = IntField(required=True,min_value=1)
    upload_date = StringField(required=True)
    audio_file = FileField(required=True)

class Podcast(Document):
    ID = IntField(required=True)
    name = StringField(max_length=100,required=True)
    duration = IntField(required=True,min_value=1)
    upload_date = StringField(required=True)
    host = StringField(max_length=100)
    participants = ListField(StringField(max_length=100),max_length=10)
    audio_file = FileField(required=True)

class Audiobook(Document):
    ID = IntField(required=True)
    title = StringField(max_length=100,required=True)
    author = StringField(max_length=100,required=True)
    narrator = StringField(required=True,max_length=100)
    duration = IntField(required=True,min_value=1)
    upload_date = StringField(required=True)
    audio_file = FileField(required=True)
