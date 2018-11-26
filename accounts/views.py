from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import sqlite3
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def home(request):

    return render(request,'home.html')

@csrf_exempt
def reviewsub(request):
  try:
    data = json.loads(request.body.decode("utf-8"))
    print(data["name"])
    conn=sqlite3.connect('SQL/Main.db')
    c=conn.cursor()
    c.execute("INSERT INTO ratings2 VALUES(:name,:channel_name,:rating)",{'name':data["name"],'channel_name':data["channel"],'rating':data["review"]})
    conn.close()
    return JsonResponse({'success': "true"})


  except Exception as e:
      # To be changed during production
      print(e)
      return JsonResponse({'Error': 'Something unexpected happened'}, status=500)



def reg(request):

    return render(request,'formpage.html')
def review(request):

    return render(request,'review.html')

@csrf_exempt
def out(request):
     try:
        data = json.loads(request.body.decode("utf-8"))
        print(data["channel1"])
        conn=sqlite3.connect('SQL/Main.db')
        c=conn.cursor()
	   # channel1rating=c.execute("SELECT avg(ratings) from ratings1 where channel_name=")
	    #channel2rating=c.execute("SELECT avg(ratings) from ratings1 where channel_name=")
        channel1subs=c.execute("SELECT no_subs from channel1 where channel_name='"+data["channel1"]+"'").fetchone()
        channel2subs=c.execute("SELECT no_subs from channel1 where channel_name='"+data["channel2"]+"'").fetchone()
        avg_view1=c.execute("SELECT avg_viewers from channel1 where channel_name='"+data["channel1"]+"'").fetchone()
        avg_view2=c.execute("SELECT avg_viewers from channel1 where channel_name='"+data["channel2"]+"'").fetchone()
        conn.close()
        print(channel1subs)
        return JsonResponse({'no_subs1': channel1subs[0],'no_subs2':channel2subs[0],'avg_view1':avg_view1[0],'avg_view2':avg_view2[0]})


     except Exception as e:
        # To be changed during production
        print(e)
        return JsonResponse({'Error': 'Something unexpected happened'}, status=500)

@csrf_exempt
def regsub(request):
     try:
        data = json.loads(request.body.decode("utf-8"))
        print(data["name"])
        conn=sqlite3.connect('SQL/Main.db')
        c=conn.cursor()
        c.execute("INSERT INTO customers1 VALUES(:name)",{'name':data["name"]})
        conn.close()
        print("success")
        return JsonResponse({'success': "true"})


     except Exception as e:
        # To be changed during production
        print(e)
        return JsonResponse({'Error': 'Something unexpected happened'}, status=500)
