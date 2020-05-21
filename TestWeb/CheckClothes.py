from TestWeb.staticdata import clothes_elove_data,clothes_merge_data,clothes_shop_data,clothes_drop_data,clothes_data,clothes_pool_data

from  TestWeb.ClothMerge import get_need_clothes





def check_clothes(clothes_array):
    #while True:
        for i in clothes_array:
            if str(i) in clothes_data.cloth_dic.keys():
                clothes_array.append(clothes_data.cloth_dic[str(i)])
                clothes_array.remove(i)
                #print(clothes_array)
                check_clothes(clothes_array)
        #print(clothes_array)
        return clothes_array
#print(check_clothes(list(get_need_clothes([11278],1)[0].keys())))

def check_is_buy(clothes_array):
    target_array=check_clothes(clothes_array)
    copyarray=target_array.copy()
    buyarray=[]
    for i in target_array:
        if str(i) in list(clothes_shop_data.cloth_dic["shop_cloth"].keys()):
            buyarray.append(i)
            copyarray.remove(i)
        elif str(i) in list(clothes_shop_data.cloth_dic["contest_cloth"].keys()):
            buyarray.append(i)
            copyarray.remove(i)
        elif str(i) in list(clothes_shop_data.cloth_dic["race_cloth"].keys()):
            buyarray.append(i)
            copyarray.remove(i)
        elif str(i) in list(clothes_shop_data.cloth_dic["alien_cloth"].keys()):
            buyarray.append(i)
            copyarray.remove(i)
    print('需要买的衣服')
    print(buyarray)
    buy_array='需要买的衣服{}'.format(buyarray)
    return buy_array,copyarray


def check_is_drop(clothes_array):
    target_array=check_is_buy(clothes_array)[1]
    buystr=check_is_buy(clothes_array)[0]
    copy_array=target_array.copy()
    drop_array=[]
    for i in target_array:
        if str(i) in str(clothes_drop_data.cloth_dic.values()):
            #print('{}在关卡中'.format(i))
            drop_array.append(i)
            copy_array.remove(i)
            #print('{}buzai'.format(i))
    print('关卡掉落的衣服')
    print(drop_array)
    droparray='关卡掉落的衣服{}'.format(drop_array)+buystr
    return droparray,copy_array


def check_is_draw(clothes_array):
    target_array=check_is_drop(clothes_array)[1]
    dropstr=check_is_drop(clothes_array)[0]
    copy_array=target_array.copy()
    draw_array=[]
    for i in target_array:
        if i in clothes_pool_data.cloth_dic:
            draw_array.append(i)
            copy_array.remove(i)
    print('抽奖抽到的')
    print(draw_array)
    drawstr='抽奖抽到的{}'.format(draw_array)+dropstr
    return drawstr,copy_array

def check_not_open(clothes_array):
    target_array=check_is_draw(clothes_array)[1]
    drawstr=check_is_draw(clothes_array)[0]

    if len(target_array)>0:
        print('没途径的衣服：')
        print(target_array)
        totalstr=drawstr+'没途径的衣服：{}<br>'.format(target_array)
    else:
        totalstr=drawstr+'都开了<br>'
        print('都开了')
    return totalstr
# print('请输入你要检查的衣服')
# clothes_array=[]
# while True:
#     try:
#         clothes=int(input())
#         clothes_array.append(clothes)
#     except:
#         break 
# # a=int(input())
# # clothes_array.append(a)
# for i in clothes_array:
#     clothes_array1=[]
#     clothes_array1.append(i)
#     print('++++++++现在要检查{}+++++++'.format(i))
#     check_not_open(list(get_need_clothes(clothes_array1,1)[0].keys()))


