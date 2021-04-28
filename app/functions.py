from flask import Flask ,request ,jsonify ,make_response
from app.models import Song ,Podcast ,Audiobook
from mongoengine import connect


connect(
    db="mp3",
    host="localhost",
    port=27017)

def create(type ,uid ):
    try:
        input_data = request.get_json()
        if type == "song":
            try:
                data = Song()
                data.ID =uid
                data.name = input_data["name"]
                data.duration = input_data["duration"]
                data.upload_date = input_data["upload_date"]
                f= open(input_data["audio_file"],'rb')
                data.audio_file.put(f,content_type='audio/mp3')
                data.save()
                upload = Song.objects().as_pymongo().to_json()
                return "Data Added to DB"
            except Exception as e:
                print(e)
                return e
            """
                Sample Input for Postman Body : {
                    "name":"test",
                    "duration":600,
                    "upload_date":"Mar2020",
                    "audio_file":"s1.mp3"
                }
            """

        elif type == "podcast":
            try:
                data = Podcast(ID=uid)
                data.name =input_data["name"]
                data.duration =input_data["duration"]
                data.upload_date =input_data["upload_date"]
                data.host = input_data["host"]
                data.participants = input_data["participants"]
                f= open(input_data["audio_file"],'rb')
                data.audio_file.put(f,content_type="audio/mp3")
                data.save()
                upload = Podcast.objects().as_pymongo().to_json()
                return "Data Added to DB"
            except Exception as e:
                print (e)
                return e
            """
                sample Input for Postman Body : {
                    "name":"test",
                    "duration":600,
                    "upload_date":"Mar2020",
                    "audio_file":"s1.mp3",
                    "host":"test host",
                    "participants":["abi","shaik"]
                }
            """
        elif type == "audiobook":
            try:
                data = Audiobook(ID=uid)
                data.title = input_data["title"]
                data.author = input_data["author"]
                data.narrator = input_data["narrator"]
                data.duration = input_data["duration"]
                data.upload_date = input_data["upload_date"]
                f= open(input_data["audio_file"],'rb')
                data.audio_file.put(f,content_type='audio/mp3')
                data.save()
                upload = Audiobook.objects().as_pymongo().to_json()
                return "Data Added to DB"
            except Exception as e:
                print (e)
                return e
            """
            Sample Input for Postman Body : {
                "title":"test",
                "duration":600,
                "upload_date":"Mar2020",
                "audio_file":"s1.mp3",
                "author" :"Abishik S",
                "narrator" :"Abishaik S"
                }
            """
        else:
            print ("Given Type is Miss matched")
            return "Given Type is Miss matched"
    except:
        print ("Invalid Process")


def read(type,uid):
    try:
        if type == "song":
            try:
                data = Song.objects(ID=uid).as_pymongo().to_json()
                print(data)
                return data ,200
            except Exception as e:
                print(e)
                return e
        elif type == "podcast":
            try:
                data = Podcast.objects(ID=uid).as_pymongo().to_json()
                return data ,200
            except Exception as e:
                print(e)
                return e    
        elif type == "audiobook":
            try:
                data =Audiobook.objects(ID=uid).as_pymongo().to_json()
                return data,200
            except Exception as e:
                print(e)
                return e    
        else:
            print ("Given Type is Miss matched")
            return "Given Type is Miss matched"
    except:
        print ("Invalid Process")

def update(type,uid):
    try:
        input_data = request.get_json()
        if type == "song":
            try:
                song =Song.objects(ID=uid)
                song.update(**input_data)
                output_data = Song.objects().as_pymongo().to_json()
                return output_data,200
            except Exception as e:
                return e
        """
            Sample Input for postman Body :{
                "name":"Abishaik Test",
                "duration":600,
                "upload_date":"Mar2020"
            }
        """
        if type == "podcast":
            try:
                podcast =Podcast.objects(ID=uid)
                podcast.update(**input_data)
                output_data =Podcast.objects().as_pymongo().to_json()
                return output_data,200
            except Exception as e:
                return e
        """
            Sample Input for Postman Body : {
                "name":"Abishaik Test",
                "duration":600,
                "upload_date":"Mar2020"
            }
        """
        if type == "audiobook":
            try:
                audiobook =Audiobook.objects(ID=uid)
                audiobook.update(**input_data)
                output_data =Audiobook.objects().as_pymongo().to_json()
                return output_data,200
            except Exception as e:
                return e
        """
            Sample Input for Postman Body : {
                "duration":800
            }
        """
        # else:
        #     print ("Given Type is Miss matched")
        #     return "Given Type is Miss matched"
    except:
        print("Invalid Process")
        
def delete(type,uid):
    try:
        if type == "song":
            try:
                song = Song.objects(ID=uid).delete()
                output = Song.objects().as_pymongo().to_json()
                return output,200
            except Exception as e:
                return e
        if type == "podcast":
            try:
                podcast =Podcast.objects(ID=uid).delete()
                output = Podcast.objects().as_pymongo().to_json()
                return output,200
            except Exception as e:
                return e
        if type == "audiobook":
            try:
                audiobook =Audiobook.objects(ID=uid).delete()
                output = Audiobook.objects().as_pymongo().to_json
                return output,200
            except Exception as e:
                return e
        # else:
        #     print ("Given Type is Miss matched")
        #     return "Given Type is Miss matched"

    except ValueError :
        return ("Invalid Process")
    