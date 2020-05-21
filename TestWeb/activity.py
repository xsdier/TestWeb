import logging
import pandas as pd
import numpy as np
import xlrd
import os
import sys
#from mysql_db import pool
import json
sys.path.append('/TestWeb/TestWeb/staticdata/')
#from staticdata import achievement
from TestWeb.staticdata import item_data_en
from TestWeb.staticdata import item_data_fr
from TestWeb.staticdata import cloth_data_en
from TestWeb.staticdata import cloth_data_fr
from TestWeb.staticdata import achievement

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


def login_gift(id,num):
	jsona='{"sender":"momo","title":"test","content":"test","template":"邮件模板，不用就去掉噢","rewards":['+item_display(id,num)+']}'
	return jsona

def a44(a,b):
	jsona=''
	jsonb=''
	jsonc=''

	for aa in a:
		c='{"chapter":'+str(aa)+','+'"difficulty":2,"type":3,"multiple":2},'
		jsona=jsona+c
	for bb in b:
		d='{"chapter":'+str(bb)+','+'"difficulty":2,"type":0,"multiple":3},'
		jsonb=jsonb+d
	jsonc=jsona+jsonb
	jsonc='['+jsonc.strip(',')+']'

	return jsonc

def a121(id,num,ac):
	jsonb='{"rewards":['+str(item_display(id,num))+'],'+'"clothes":'+str(get_clothes_new(ac))+','+'"name":'+'"'+str(get_suitname(ac))+'"'+'}'
	return jsonb
	
def a126(cloth_arry):
	a=1
	jsona=''
	cloth_arry.reverse()
	while cloth_arry:
		cloth_id=cloth_arry.pop()
		c='{"id":'+str(a)+',"reward":[{"id":'+str(cloth_id)+',"tpye":0,"num":1}]},'
		jsona=jsona+c
		a=a+1
	jsona='{"title":"MoMo","desc":"","rewards":['+jsona.strip(',')+']}'
	return jsona
def a171(cloth_array,price):
	n=0
	jsona=''
	jsonb=''
	for i in range(0,len(cloth_array)):
		num_array=[]
		for num in cloth_array[i]:
			num_array.append(1)
		if i==0:
			jsona='{"id":'+str(n)+','+'"charge":'+str(price[i])+','+'"namepic":"back_charge_name'+str(n+29)+'",'+'"rewards":['+item_display(cloth_array[i],num_array)+']},'
		else:
			if clothes_compare(cloth_array[i-1],cloth_array[i])==True:
				jsona='{"id":'+str(n)+','+'"charge":'+str(price[i])+','+'"rewards":['+item_display(cloth_array[i],num_array)+']},'
			else:
				jsona='{"id":'+str(n)+','+'"charge":'+str(price[i])+','+'"namepic":"back_charge_name'+str(n+29)+'",'+'"rewards":['+item_display(cloth_array[i],num_array)+']},'
		jsonb=jsonb+jsona
		n=n+1
	jsonc='{"levels":['+jsonb.strip(',')+']}'
	return jsonc
def a1712(cloth_array,num,price):
	n=0
	jsona=''
	jsonb=''
	for i in range(0,len(cloth_array)):
		num_array=[]
		if i==0:
			jsona='{"id":'+str(n)+','+'"charge":'+str(price[i])+','+'"namepic":"back_charge_name'+str(n+29)+'",'+'"rewards":['+item_display(cloth_array[i],num[i])+']},'
		else:
			if clothes_compare(cloth_array[i-1],cloth_array[i])==True:
				jsona='{"id":'+str(n)+','+'"charge":'+str(price[i])+','+'"rewards":['+item_display(cloth_array[i],num[i])+']},'
			else:
				jsona='{"id":'+str(n)+','+'"charge":'+str(price[i])+','+'"namepic":"back_charge_name'+str(n+29)+'",'+'"rewards":['+item_display(cloth_array[i],num[i])+']},'
		jsonb=jsonb+jsona
		n=n+1
	jsonc='{"levels":['+jsonb.strip(',')+']}'
	return jsonc
def a237(suit_id,vipexp):
	c4=''
	c3=''
	for i in range(0,len(suit_id)):
		c='{'+'"id":'+str(i)+','+'"achi_id":'+str(suit_id[i])+','+'"charge":'+str(vipexp)+','+'"rewards":['+item_display([suit_id[i]],[1])
		c3=c3+c+']},'
		c4=c3.strip(',')+'],'
	jsonc='['+c4.strip(',')
	return jsonc


def a31(id,num,costnum):
	b=[]
	jsonb=''
	n=0
	for i in range(0,len(id)):
		c='"rwdname":{"en":'
		c2=''
		c3=''
		i2=''
		i1='"rewards":['
		n=n+1
		c4=''
		i3=''
		c6='fr":"'
		for ii in range(0,len(id[i])):
			if id[i][ii]<1000:
				c1=item_data_en.Item_data.item_dic[str(id[i][ii])]+'*'+str(num[i][ii])+'+'
				c5=item_data_fr.Item_data.item_dic[str(id[i][ii])]+'*'+str(num[i][ii])+'+'
			else:
				c1=cloth_data_en.Cloth_data.cloth_dic[str(id[i][ii])]+'*'+str(num[i][ii])+'+'
				c5=cloth_data_fr.Cloth_data.cloth_dic[str(id[i][ii])]+'*'+str(num[i][ii])+'+'
			c2+=c1
			c6+=c5
			c3=c+'"'+c2.strip('+')+'"'+','+'"'+c6.strip('+')+'"'+'},'
			i2=item_display2(id[i],num[i])
			print(i2)
		i3+=i1+i2+'],'	
		c4+=c3
		jsona='{'+'"id":'+str(n)+','+c4+i3+'"spend_jewel":'+str(costnum[i])+'},'
	# print(i3)
	# print(c4)
		jsonb+=jsona
	jsonc='{"costtype":4,"drop":['+jsonb.strip(',')+']}'
	return jsonc
	print(jsonc)



# def get_clothes(suit_id):
# 	try:
# 		#suit=pd.read_excel('D:/nuannuan3_europe/多语言翻译比对表/表格/玩家_成就表.xlsx',sheet_name='Sheet2')
# 		suit=pd.read_excel('D:/nuannuan3_korea/表格/玩家_成就表.xlsx',sheet_name='Sheet2')
# 	except FileNotFoundError:
# 		print('未找到表格，请将成就表放在相同目录下并改名achievement')
# 	if str(suit_id)[0] in '0123456789':
# 		length=len(suit)
# 		row=suit.shape[1]
# 		suit=suit.fillna(0)
# 		cloth_show=[]
# 		for a in range(0,length):
# 			if suit_id==suit.iat[a,0]:
# 				cloth_id=suit.loc[a].values
# 				cloth_id=cloth_id.tolist()
# 				cloth_id.reverse()
# 				while 0 in cloth_id:
# 					cloth_id.remove(0)
# 				del cloth_id[-1]
# 				for clothes in cloth_id:
# 					cloth_show.append(int(clothes))
# 				return cloth_show    
def get_clothes_new(suit_id):
	if str(suit_id) in list(achievement.cloth_dic.keys()):
		print('yes')
		print(list(achievement.cloth_dic[str(suit_id)].values())[0])
		return list(achievement.cloth_dic[str(suit_id)].values())[0]

def get_suitname(suit_id):
    	return list(achievement.cloth_dic[str(suit_id)].keys())[0]

			
def item_display(itemid,itemnum):
	jsona=''
	for i in range(0,len(itemid)):
		if itemid[i]<200:
			c='{"id":0,'+'"type":'+str(itemid[i])+','+'"num":'+str(itemnum[i])+'},'
		elif itemid[i]>200 and itemid[i]<2000:
			c=''
			cloth_array=get_clothes_new(itemid[i])
			for cloth in cloth_array:
				d='{"id":'+str(cloth)+','+'"type":0,'+'"num":1'+'},'
				c=c+d
		elif itemid[i]>2000 and itemid[i]<10000:
			c=''
			d='{"id":'+str(itemid[i])+','+'"type":1,'+'"num":'+str(itemnum[i])+'},'
			c=c+d
		elif itemid[i]>10000:
			c=''
			d='{"id":'+str(itemid[i])+','+'"type":0,'+'"num":'+str(itemnum[i])+'},'
			c=c+d
		jsona=jsona+c
	return jsona.strip(',')
def item_display2(itemid,itemnum):
	jsona=''
	for i in range(0,len(itemid)):
		if itemid[i]<200:
			c='[{"id":0,'+'"type":'+str(itemid[i])+','+'"num":'+str(itemnum[i])+'}],'
		elif itemid[i]>200 and itemid[i]<2000:
			c=''
			cloth_array=get_clothes_new(itemid[i])
			for cloth in cloth_array:
				d='[{"id":'+str(cloth)+','+'"type":0,'+'"num":1'+'}],'
				c=c+d
		elif itemid[i]>2000 and itemid[i]<10000:
			c=''
			d='[{"id":'+str(itemid[i])+','+'"type":1,'+'"num":'+str(itemnum[i])+'}],'
			c=c+d
		elif itemid[i]>10000:
			c=''
			d='[{"id":'+str(itemid[i])+','+'"type":0,'+'"num":'+str(itemnum[i])+'}],'
			c=c+d
		jsona=jsona+c
	return jsona.strip(',')

def clothes_compare(suita,suitb):
	suit=pd.read_excel(r'D:/nuannuan3_europe/多语言翻译比对表/表格/玩家_成就表.xlsx',sheet_name='Sheet2')
	length=len(suit)
	row=suit.shape[1]
	suit=suit.fillna(0)
	cloth_show=[]
	for a in range(0,length):
		cloth_id=suit.loc[a].values
		cloth_id=cloth_id.tolist()
		if suita[0] in cloth_id:
			if suitb[0] in cloth_id:
				return True
			else:
				return False
