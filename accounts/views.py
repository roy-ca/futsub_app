from django.shortcuts import render,HttpResponse
import sqlite3
# Create your views here.

def home(request):
    conn=sqlite3.connect('SQL/Main.db')
    c=conn.cursor()
    channel1subs=c.execute('''SELECT no_subs from youtubers where channel_name="test"''').fetchone()
    channel2subs=c.execute('''SELECT no_subs from youtubers where channel_name="pewdiepie"''').fetchone()
    conn.close()
    return render(request,'home.html',{'no_subs1': channel1subs,'no_subs2':channel2subs})
