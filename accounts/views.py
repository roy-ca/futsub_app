from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import sqlite3
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def home(request):

    return render(request,'home.html')
def insertrating(request)
	
	conn=sqlite3.connect('SQL/Main.db')
        c=conn.cursor()
	c.execute("INSERT INTO ratings VALUES(:id,:name,:channel_name,:rating)",{'id':id,'name':name,'channel_name':channel_name,'rating':rating})
	conn.close()
def insertcust(request):
	conn=sqlite3.connect('SQL/Main.db')
        c=conn.cursor()
	c.execute("INSERT INTO customer VALUES(:id,:name)",{'id':id,'name':name})
	conn.close()

@csrf_exempt
def out(request):
     try:
        data = json.loads(request.body.decode("utf-8"))
        print(data["channel1"])
        conn=sqlite3.connect('SQL/Main.db')
        c=conn.cursor()
	channel1rating=c.execute("SELECT avg(ratings) from ratings where channel_name=")
	channel2rating=c.execute("SELECT avg(ratings) from ratings where channel_name=")
        channel1subs=c.execute("SELECT no_subs from channel where channel_name='"+data["channel1"]+"'").fetchone()
        channel2subs=c.execute("SELECT no_subs from channel where channel_name='"+data["channel2"]+"'").fetchone()
        avg_view1=c.execute("SELECT avg_viewers from channel where channel_name='"+data["channel1"]+"'").fetchone()
        avg_view2=c.execute("SELECT avg_viewers from channel where channel_name='"+data["channel2"]+"'").fetchone()
        conn.close()
        print(channel1subs)
        return JsonResponse({'no_subs1': channel1subs[0],'no_subs2':channel2subs[0],'avg_view1':avg_view1[0],'avg_view2':avg_view2[0]})


     except Exception as e:
        # To be changed during production
        print(e)
        return JsonResponse({'Error': 'Something unexpected happened'}, status=500)
