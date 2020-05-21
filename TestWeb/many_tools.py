from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
from TestWeb import activity
from TestWeb import CheckClothes
from  TestWeb.ClothMerge import get_need_clothes


def many_tools(request):
    ctx={}
    a={}

    if request.POST.get('button')=='检查衣服合成情况':
        ctx['id'] = request.POST.get('id')
        try:
            clothesarray=activity.tolist(ctx['id'])
            print(clothesarray)
            totalstr=''
            for i in clothesarray:
                clothes_array1=[]
                clothes_array1.append(i)
                strtips='++++++++现在要检查{}+++++++<br>'.format(i)
                totalstr+=strtips+CheckClothes.check_not_open(list(get_need_clothes(clothes_array1,1)[0].keys()))
            a['rlt']=totalstr
            return render(request, "many_tools.html", a)
            # print(total_json)
            # a['rlt']=total_json
        except:
            a['rlt']='nothing input'
            return render(request, "many_tools.html", a)
            pass
    else:
        a['rlt']='nothing input'
        return render(request, "many_tools.html", a)
        pass

    