from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from app1.models import Ipaddress

def index(request):
    # データベース上のIPアドレス情報を配列型で取得
    ipaddresses = Ipaddress.objects.all().order_by('id')

    return render(request,
        'index.html', # テンプレート名を指定
        {'ipaddresses' : ipaddresses }, # 取得したIPアドレス情報をテンプレート内の変数に代入
        )

def test(request):
    ip_addr = request.META['REMOTE_ADDR']

    return render(request,
        'test.html',
        {'ip_addr' : ip_addr}
        )
