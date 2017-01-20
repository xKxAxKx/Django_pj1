from django.http import HttpResponse
from django.shortcuts import render
from app1.models import Ipaddress

def index(request):
    # データベース上のIPアドレス情報を配列型で取得
    ipaddresses = Ipaddress.objects.all().order_by('id')

    return render(request,
        'index.html', # テンプレート名を指定
        {'ipaddresses' : ipaddresses }, # 取得したIPアドレス情報をテンプレート内の変数に代入
        )
