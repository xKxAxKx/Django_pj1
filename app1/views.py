from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from app1.models import Ipaddress
from app1.forms import IpaddressForm


def index(request):
    # データベース上のIPアドレス情報を配列型で取得
    ipaddresses = Ipaddress.objects.all().order_by('id')


    return render(request,
        'index.html', # テンプレート名を指定
        {'ipaddresses' : ipaddresses }, # 取得したIPアドレス情報をテンプレート内の変数に代入
    )


def edit(request, ipaddress_id=None):
    if ipaddress_id:
        ipaddress =  get_object_or_404(Ipaddress, pk=ipaddress_id)
        status = "change status"
    else:
        ipaddress = Ipaddress()
        status = "add IP"



    if request.method == 'POST':
        form = IpaddressForm(request.POST, instance=ipaddress)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('app1:index')
    else:
        form = IpaddressForm(instance=ipaddress)


    return render(request,
        'edit.html',
        dict(form=form, ipaddress_id=ipaddress_id, status=status)
    )

# def test(request):
#     ip_addr = request.META['REMOTE_ADDR']
#
#     return render(request,
#         'test.html',
#         {'ip_addr' : ip_addr}
#         )
