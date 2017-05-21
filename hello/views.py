from django.shortcuts import render
from .models import Greeting
import psycopg2
import requests
import sys
import pprint
import json
from django.http import HttpResponse, JsonResponse
conn_string = "host='ec2-23-21-224-106.compute-1.amazonaws.com' dbname='df4np0hds8r4s2' user='poztqmtwsusjtl' password='110b831a16b196e24c03785e1c3ad5b2c9e5f16b0fcc4cdec1391561c4920a2f'"
print "Connecting to database\n	->%s" % (conn_string)
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
cursor.execute("SELECT * FROM next_int")
rows = cursor.fetchall()

def index(request):

    return HttpResponse('Next INT')

def data(request):
    num = 0
    for row in rows:
       print "no", row[0]
       print "name = ", row[1]
       print "surname = ", row[2]
       print "year = ", row[3]
       print "department = ", row[4]
       print "gpa = ", row[5]
       print "future", row[6], "\n"
    return JsonResponse({'data': rows})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


