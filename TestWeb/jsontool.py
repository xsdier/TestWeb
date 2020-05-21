#!/usr/bin/env python
# -*- coding:utf-8 -*-
# from tkinter import *
# root=Tk()
# Button(root,text='A').pack(side=LEFT,expand=YES,fill=Y)
# Button(root,text='B').pack(side=TOP,expand=YES,fill=BOTH)
# Button(root,text='C').pack(side=RIGHT,expand=YES,fill=NONE,anchor=NE)
# Button(root,text='D').pack(side=LEFT,expand=NO,fill=Y)
# Button(root,text='E').pack(side=TOP,expand=NO,fill=BOTH)
# Button(root,text='F').pack(side=BOTTOM,expand=YES)
# Button(root,text='G').pack(anchor=SE)
# root.mainloop()
import activity
import time
#a='1,2,3'
def tolist(a):
    b=[]
    c=''
    n=0
    for aa in a:
        n=n+1
        if aa==',':
            b.append(int(c))
            c=''
            #pass
        elif n==len(a):
            c=c+aa
            b.append(int(c))
            c=''
        else:
            c=c+aa
    return b
#print(tolist(a))
def listlist(a):
    c=''
    n=0
    b=[]
    for aa in a:
        n=n+1
        if aa=='[':
            c=''
        elif aa==']':
            c=tolist(c)
            b.append(c)
            c=''
        elif aa==',' and a[n-1]!=']':
            c=c+aa
        else:
            c=c+aa
    return b
#print(listlist(a))
def a31():
    text.delete('1.0','end')
    ac_id='活动id：31\n'
    ac_time1=ac_time.get()+'\n'
    type_str='活动类型：0\n'
    status_str='活动状态：0\n'
    pho_str='图片地址：31\n'
    ver_str='版本：1\n'
    show_str='显示：1\n'
    rewid=listlist(item_id.get())
    renum=listlist(item_num.get())
    costnum=tolist(item_price.get())
    #print(pricearray)
    c=ac_id+ac_time1+type_str+status_str+'活动细节：'+activity.a31(rewid,renum,costnum)
    d=c+'\n'+pho_str+ver_str+show_str
    return d
    
def a44():
    text.delete('1.0','end')
    gold_chapter=item_id.get().split(',')
    ac_id='活动id：44\n'
    ac_time1=ac_time.get()+'\n'
    type_str='活动类型：0\n'
    status_str='活动状态：0\n'
    #gold_chapter=tolist(gold_chapter)
    #print(gold_chapter)
    drop_chapter=item_num.get().split(',')
    total_json=ac_id+ac_time1+type_str+status_str+'活动细节：'+activity.a44(gold_chapter,drop_chapter)
    return total_json    
def login_gift():
    text.delete('1.0','end')
    #a=item_id.get().split(',')
    ac_id='活动id：\n'
    ac_time1=ac_time.get()+'\n'
    type_str='活动类型：0\n'
    status_str='活动状态：0\n'
    a=tolist(item_id.get())
    b=tolist(item_num.get())
    c=ac_id+ac_time1+type_str+status_str+'活动细节：'+activity.login_gift(a,b)
    return c
def a126():
    text.delete('1.0','end')
    clothearray=tolist(item_id.get())
    ac_id='活动id：126\n'
    ac_time1=ac_time.get()+'\n'
    type_str='活动类型：0\n'
    status_str='活动状态：0\n'
    pho_str='图片地址：126\n'
    ver_str='版本：1\n'
    show_str='显示：1\n'
    #print(clothearray)
    c=ac_id+ac_time1+type_str+status_str+'活动细节：'+activity.a126(clothearray)
    d=c+'\n'+pho_str+ver_str+show_str
    return d
def a121():
    text.delete('1.0','end')
    goodsid=tolist(item_id.get())
    goodsnum=tolist(item_num.get())
    ac_id='活动id：121\n'
    ac_time1=ac_time.get()+'\n'
    type_str='活动类型：0\n'
    status_str='活动状态：0\n'
    pho_str='图片地址：121\n'
    ver_str='版本：1\n'
    show_str='显示：1\n'
    ach_id1=int(ach_id.get())
    c=ac_id+ac_time1+type_str+status_str+'活动细节：'+activity.a121(goodsid,goodsnum,ach_id1)
    d=c+'\n'+pho_str+ver_str+show_str
    return d
def a171(): 
    text.delete('1.0','end')
    ac_id='活动id：171\n'
    ac_time1=ac_time.get()+'\n'
    type_str='活动类型：0\n'
    status_str='活动状态：0\n'
    pho_str='图片地址：171\n'
    ver_str='版本：1\n'
    show_str='显示：1\n'
    clotharray=listlist(item_id.get())
    pricearray=tolist(item_price.get())
    print(pricearray)
    c=ac_id+ac_time1+type_str+status_str+'活动细节：'+activity.a171(clotharray,pricearray)
    d=c+'\n'+pho_str+ver_str+show_str
    return d
def a1712():
    text.delete('1.0','end')
    ac_id='活动id：\n'
    ac_time1=ac_time.get()+'\n'
    type_str='活动类型：0\n'
    status_str='活动状态：0\n'
    pho_str='图片地址：126\n'
    ver_str='版本：1\n'
    show_str='显示：1\n'
    clotharray=listlist(item_id.get())
    numarray=listlist(item_num.get())
    pricearray=tolist(item_price.get())
    c=ac_id+ac_time1+type_str+status_str+'活动细节：'+activity.a1712(clotharray,numarray,pricearray)
    d=c+'\n'+pho_str+ver_str+show_str
    return d
def a237():
    text.delete('1.0','end')
    ac_id='活动id：237\n'
    ac_time1=ac_time.get()+'\n'
    type_str='活动类型：0\n'
    status_str='活动状态：0\n'
    pho_str='图片地址：237\n'
    ver_str='版本：1\n'
    show_str='显示：1\n'
    clotharray=tolist(item_id.get())
    pricearray=int(item_price.get())
    c=ac_id+ac_time1+type_str+status_str+'活动细节：'+activity.a237(clotharray,pricearray)
    d=c+'\n'+pho_str+ver_str+show_str
    return d
def getjson():
    text.delete('1.0','end')
    ac_id='活动id：'
    ac_time1=ac_time.get()+'\n'
    type_str='活动类型：0\n'
    status_str='活动状态：0\n'
    pho_str='图片地址：'
    ver_str='版本：'
    show_str='显示：2'
    aid=int(item_id.get())
    version=int(item_num.get())
    c=ac_id+str(aid)+'\n'+ac_time1+type_str+status_str+"活动细节：\n"+activity.get_json(aid,version)+'\n'+pho_str+str(aid)+'\n'+ver_str+str(version)+'\n'+show_str
    return d
def getname():
    text.delete('1.0','end')
    suitid=int(item_id.get())
    c=activity.get_suitname(suitid)
    text.insert(tkinter.INSERT, c)
# def docloth_en():
#     text.delete('1.0','end')
#     suitid=item_id.get()
#     activity.do_cloth_en()
#     text.insert(tkinter.INSERT, '导入成功')
# def docloth_fr():
#     text.delete('1.0','end')
#     suitid=item_id.get()
#     activity.do_cloth_fr()
#     text.insert(tkinter.INSERT, '导入成功')
# def doitem_en():
#     text.delete('1.0','end')
#     suitid=item_id.get()
#     activity.do_item_en()
#     text.insert(tkinter.INSERT, '导入成功')
# def doitem_fr():
#     text.delete('1.0','end')
#     suitid=item_id.get()
#     activity.do_item_fr()
#     text.insert(tkinter.INSERT, '导入成功')
# def doachi():
#     # text.delete('1.0','end')
#     # suitid=int(item_id.get())
#     # c=activity.get_suitname(suitid)
#     text.insert(tkinter.INSERT, '开发中')
