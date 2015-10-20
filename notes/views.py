from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
import pymysql


def f(request):
    conn=pymysql.connect(host="localhost", user='root', passwd="",
                 db='blog', port=3306,
                 charset='utf8')
    cursor=conn.cursor()
    sql='select * from `test`'
    cursor.execute(sql)
    a=cursor.fetchall()
    print(a)
    return render_to_response('notes/pages/page.html',{'item_list':[x[2] for x in a]})