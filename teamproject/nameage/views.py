from django.http import HttpResponse
from pymongo import MongoClient
from pymongo.cursor import CursorType

def index(request):
    host = "54.180.148.164"
    port = "27017"
    client = MongoClient(host, int(port))
    db = client['baedalgeek_test']
    col = db['Users']

    data = col.find().sort({"idate":-1}).limit(1).toString()
    return HttpResponse(data, content_type="text/plain")
    

#     output = "{\n" + "\t\"name\": \"" + name + "\",\n\t\"age\": " + age + ",\n\t\"message\": " + message + "\n}"
