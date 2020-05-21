# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
from TestWeb import activity


#数据处理函数，将收到的信息转换成列表
# 接收请求数据
def jsonget(request): 
    ctx={}
    a={}
    if request.POST.get('button')=='公主级双倍':
        ctx['num'] = request.POST.get('num')
        ctx['id'] = request.POST.get('id')
        ctx['actime'] = request.POST.get('actime')
        ac_id='活动id：44<br>'
        ac_time1=ctx['actime']+'<br>'
        type_str='活动类型：0<br>'
        status_str='活动状态：0<br>'
        try:
            goldlist=activity.tolist(ctx['num'])
            droplist=activity.tolist(ctx['id'])
            total_json=ac_id+ac_time1+type_str+status_str+'活动细节：'+activity.a44(droplist,goldlist)
            print(total_json)
            a['rlt']=total_json
        except:
            pass
    elif request.POST.get('button')=='登陆送':
        ctx['num'] = request.POST.get('num')
        ctx['id'] = request.POST.get('id')
        ctx['actime'] = request.POST.get('actime')
        ac_id='活动id：[14,24],[33,42]<br>'
        ac_time1=ctx['actime']+'<br>'
        type_str='活动类型：0<br>'
        status_str='活动状态：0<br>'
        try:
            goodsnum=activity.tolist(ctx['num'])
            goodsid=activity.tolist(ctx['id'])
            total_json=ac_id+ac_time1+type_str+status_str+'活动细节：'+activity.login_gift(goodsid,goodsnum)
            print(total_json)
            a['rlt']=total_json
        except:
            pass
    elif request.POST.get('button')=='累充':
        ctx['price'] = request.POST.get('price')
        ctx['id'] = request.POST.get('id')
        ctx['actime'] = request.POST.get('actime')
        ac_id='活动id：171<br>'
        ac_time1=ctx['actime']+'<br>'
        type_str='活动类型：0<br>'
        status_str='活动状态：0<br>'
        pho_str='图片地址：171<br>'
        ver_str='版本：1<br>'
        show_str='显示：1<br>'
        try:
            price=activity.tolist(ctx['price'])
            clothesarray=activity.listlist(ctx['id'])
            total_json=ac_id+ac_time1+type_str+status_str+'活动细节：'+activity.a171(clothesarray,price)+'<br>'+pho_str+ver_str+show_str
            print(total_json)
            a['rlt']=total_json
        except:
            pass
    elif request.POST.get('button')=='大喵指引':
        ctx['num'] = request.POST.get('num')
        ctx['id'] = request.POST.get('id')
        ctx['actime'] = request.POST.get('actime')
        ctx['suit'] = request.POST.get('suitid')
        ac_id='活动id：121<br>'
        ac_time1=ctx['actime']+'<br>'
        type_str='活动类型：0<br>'
        status_str='活动状态：0<br>'
        try:
            num=activity.tolist(ctx['num'])
            print(num)
            cid=activity.tolist(ctx['id'])
            print(cid)
            suit=activity.tolist(ctx['suit'])
            print(suit)
            
            total_json=ac_id+ac_time1+type_str+status_str+'活动细节：'+activity.a121(cid,num,int(ctx['suit']))+'<br>'
            print(total_json)
            a['rlt']=total_json
        except:
            pass
    elif request.POST.get('button')=='大额复刻':
        ctx['num'] = request.POST.get('num')
        ctx['id'] = request.POST.get('id')
        ctx['actime'] = request.POST.get('actime')
        ctx['suit'] = request.POST.get('suitid')
        ac_id='活动id：237<br>'
        ac_time1=ctx['actime']+'<br>'
        type_str='活动类型：0<br>'
        status_str='活动状态：0<br>'
        try:
            clothesarray=activity.tolist(ctx['id'])
            print(clothesarray)
            total_json=ac_id+ac_time1+type_str+status_str+'活动细节：'+activity.a237(clothesarray,int(ctx['num']))+'<br>'
            print(total_json)
            a['rlt']=total_json
        except:
            pass
    elif request.POST.get('button')=='累计消耗':
        ctx['num'] = request.POST.get('num')
        ctx['id'] = request.POST.get('id')
        ctx['actime'] = request.POST.get('actime')
        ctx['price'] = request.POST.get('price')
        ac_id='活动id：31<br>'
        ac_time1=ctx['actime']+'<br>'
        type_str='活动类型：0<br>'
        status_str='活动状态：0<br>'
        try:
            num=activity.listlist(ctx['num'])
            print(num)
            cid=activity.listlist(ctx['id'])
            print(cid)
            price=activity.tolist(ctx['price'])
            print(price)
            
            total_json=ac_id+ac_time1+type_str+status_str+'活动细节：'+activity.a31(cid,num,price)+'<br>'
            print(total_json)
            a['rlt']=total_json
        except:
            pass
    elif request.POST.get('button')=='签到送':
        ctx['id'] = request.POST.get('id')
        ctx['actime'] = request.POST.get('actime')
        ac_id='活动id：126<br>'
        ac_time1=ctx['actime']+'<br>'
        type_str='活动类型：0<br>'
        status_str='活动状态：0<br>'
        try:
            cid=activity.tolist(ctx['id'])
            print(ctx['id'])
            print(cid)
            total_json=ac_id+ac_time1+type_str+status_str+'活动细节：'+activity.a126(cid)+'<br>'
            print(total_json)
            a['rlt']=total_json
        except:
            pass
    return render(request, "json_form.html", a)

# 接收POST请求数据


