#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
from bs4 import BeautifulSoup

url = "https://www.op.gg/champion/statistics"
htmlText = requests.get(url).text
bsoup = BeautifulSoup(htmlText, "html.parser")
btab = bsoup.find("tbody", {"class" : "tabItem champion-trend-tier-TOP"})
btrs = btab.find_all("td",{"class" :"champion-index-table__cell champion-index-table__cell--champion"})
    
tops = []

for tr in btrs:
    dic = {}
    tds = tr.find_all("div")
    dic['champion'] = tds[0].text
    a = tds[1].text.replace("\t","")
    dic['position'] = a.replace("\n","")
    tops.append(dic)
        


# In[8]:


from tkinter import Tk,ttk,Label,Button,Text,END
import tkinter as tk #tkinter 라이브러리
from tkinter import ttk

window = Tk()
window.title("챔피언 분석")  # 이름
window.geometry("450x450") # 크기 조정
window.resizable(0,0) #고정

title = "포지션별 챔피언 랭킹" #헤더 느낌?
title_feature = Label(window,text = title, font = ("Noto Sans KR",20)) #라벨 , 폰트 조정
title_feature.pack(padx = 10, pady = 15) 

treeTable = ttk.Treeview(window)  #테이블 생성
treeTable["columns"] = ("champion","position")  # 테이블 아이템
treeTable.column("#0",width = 50)  # 이름 및 테이블 크기
treeTable.column("champion",width = 100)  
treeTable.column("position",width = 50)

# combobox = Tk.ttk.Combobox(window, height=15, values=values)

treeTable.heading("#0", text = "No.",anchor = "center") #heading열이름 / 중앙 정렬
treeTable.heading("champion", text = "챔피언", anchor = "center")  #테이블 아이템 이름 변경 / 중앙 정렬
treeTable.heading("position",text = "라인", anchor = "center")

OptionList = [
    "탑",
    "정글",
    "미드",
    "원딜",
    "서폿"
]

# window.geometry('200x200')
# window.title("라인")
variable = tk.StringVar(window)
variable.set(OptionList[0])

opt = ttk.Combobox(window, value = OptionList, state = "readonly")
opt.config(width=15, font=('Noto Sans KR', 12))
opt.place(x = 20, y = 50)


def setTableItem():
    treeTable.delete(*treeTable.get_children())
    for idx, report in enumerate(tops): #enumerate tops안에 리스트를 숫자화?
        champion = report['champion']
        position = report['position']
        treeTable.insert("",'end',iid = None, text = str(idx),values = [champion,position])

# def callback(*args):

#     variable.trace("w",callback)
    
# btn1 = Button(window, text = '검색') #command = 함수이름
# btn1.place(x=-100,y=300, relx = 0.5, width = 40, height = 40)
# btn1.pack()

        
setTableItem()       
treeTable.place(x=10,y=90,width=420,height=250)




#conda install pyinstaller 
# cd <= 경로 지정 (cd C:\)
#pyinstaller -w -F 0701_2.py


window.mainloop()


# In[ ]:




