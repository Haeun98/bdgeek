from django.http import HttpResponse
from django.core import serializers
from pymongo import MongoClient
from pymongo.cursor import CursorType

def index(request):
    host = "54.180.148.164"
    port = "27017"
    client = MongoClient(host, int(port))
    db = client['baedalgeek_test']
    col = db['Users']

    data = col.find().sort({"idate":-1})
    jsonData = serializers.serialize('json',data)
    return HttpResponse(jsonData, content_type="text/json-comment-filtered")
