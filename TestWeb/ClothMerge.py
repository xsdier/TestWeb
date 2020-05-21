from TestWeb.staticdata import clothes_merge_data,clothes_elove_data,clothes_shop_data


merge_dic=clothes_merge_data.cloth_dic
elove_dic=clothes_elove_data.cloth_dic
shop_dic=clothes_shop_data.cloth_dic


def get_need_clothes(clothesarray,num):
    for i in range(0,len(clothesarray)):
        target_dic={}
        need_merge={}
        if int(clothesarray[i])<10000:
            pass
        elif str(clothesarray[i]) in merge_dic.keys():
            target_dic=merge_dic[str(clothesarray[i])].copy()
            # print('+++++++')
            # print(target_dic)
            # print('++++++')
            need_merge[clothesarray[i]]=num
        compare_dic={'a':1}
        while True:
            for key1 in list(target_dic.keys()):
                if key1 in merge_dic.keys():
                    mertrial_dic=merge_dic[key1].copy()
                    for key2 in list(mertrial_dic.keys()):
                        try:
                            mertrial_dic[key2]*=target_dic[key1]
                        except:
                            pass
                    need_merge[key1]= target_dic[key1]
                    del target_dic[key1]
                    #处理子材料和父材料有交集的情况
                    print(mertrial_dic)
                    for keys in list(mertrial_dic.keys()):
                        if keys in target_dic.keys():
                            target_dic[keys]+=mertrial_dic[keys]
                            del mertrial_dic[keys]
                            #target_dic.update(mertrial_dic)
                        else:
                            pass
                    target_dic.update(mertrial_dic)
            if compare_dic.keys()==target_dic.keys():
                print(compare_dic)
                print(need_merge)
                return compare_dic,need_merge
            else:
                compare_dic=target_dic.copy()