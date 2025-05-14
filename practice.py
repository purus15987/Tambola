#!/usr/bin/env python
# coding: utf-8

# In[40]:


import tkinter as tk
window=tk.Tk()
window.title("TAMBOLA")

import random
import numpy as np
from collections import Counter


ticket=np.zeros((18,9),dtype=int)
total_boxes=[(i,j) for i in range(18) for j in range(9)]
selected_boxes=[]
d=0
t=0
for j in range(10):
    c=[x for x in range(9)]
    for k in range(9):
        t+=1
        if t%5==1:
            d+=1
        rand=random.sample(c,1)
        select=[(d-1,rand[0])]
        selected_boxes+=select
        c.remove(rand[0])
res=[ele for ele,count in Counter(selected_boxes).items() if count>1]
for x in res:
    selected_boxes.remove(x)

for x in res:
    rough1=[i for i in range(18)]
    rough2=[i for i in range(9)]
    rough3=[]
    temp1=x[0]
    temp2=x[1]
    rows=[0 for i in range(18)]
    for y in selected_boxes:
        if y[1]==temp2:
            for j in range(18):
                if y[1]==j:
                    rough1.remove(y[0])
        if y[0]==temp1:
            for i in range(9):
                if y[1]==i:
                    rough2.remove(i)
    r1=rough1[0]
    for y in selected_boxes:
        if y[0]==r1:
            for i in range(9):
                if y[1]==i:
                    rough3.append(i)
    r2=rough1[0]
    sam1=[(r1,temp2)]
    selected_boxes+=sam1
    
    for g in rough3:
        for f in rough2:
            if g==f:
                dog=g
    sam2=[(r1,dog)]
    selected_boxes.remove(sam2[0])
    sam3=[(temp1,dog)]
    selected_boxes+=(sam3)

t1=[]
t2=[i for i in range(18)]

for j in selected_boxes:
    if j[1]==0:
        t1.append(j[0])
    if j[1]==8:
        t2.remove(j[0])     
for j in t1:
    for k in t2:
        if j==k:
            w=j
selected_boxes.remove((w,0))
selected_boxes+=[(w,8)]        

total_numbers=[[] for i in range(9)]
for i in range(9):
    for j in range(10):
        total_numbers[i].append(j+(i*10))
total_numbers[0].remove(0)
total_numbers[8].append(90)

for i in selected_boxes:
    for j in range(9):
        if i[1]==j:
            number=random.choice(total_numbers[j])
            ticket[i]=number
            total_numbers[j].remove(number)
print(ticket)



numbers=[i for i in range(1,91)]
numbers1=[]
for i in range(90):
    num=random.sample(numbers,1)
    numbers1.append(num[0])
    numbers.remove(num[0])


print(numbers1)

royal1=[]
royal2=[]
for i in range(18):
    royal1.append([])
    for k in range(9):
        x=ticket[i][k]
        if x!=0:
            royal1[i].append(x)
    if i%3==2:
        royal=royal1[i]+royal1[i-1]+royal1[i-2]
        royal2.append((royal))


jaldhi=[]
housie=[]
                    
for i in numbers1:
    for j in range(6):
        for k in royal2[j]:
            if i==k:
                royal2[j].remove(i)
                if len(royal2[j])==10:
                    jaldhi.append(j)
                if len(royal2[j])==0:
                    housie.append(j)
print('jaldhi=',jaldhi)
print('housie=',housie)


lower_line=[]
middle_line=[]
upper_line=[]

for i in numbers1:
    for j in range(18):
        for k in royal1[j]:
            if i==k:
                royal1[j].remove(i)
                if len(royal1[j])==0:
                    line=j
                    if line%3==0:
                        upper_line.append(line)
                    if line%3==1:
                        middle_line.append(line)
                    if line%3==2:
                        lower_line.append(line)
print("lower line",lower_line)
print("middle line",middle_line)
print("upper line",upper_line)

display=tk.Label(text='lets play tambola',height='2',width='10')
display.grid(row=7,column=11)


extra=[]
i=0
def run_program():
    global i
    global numbers1
    global ticket
    global extra
    number=numbers1[i]
    extra.append(number)
    
    
    
    
    display=tk.Label(text='present number',height='2',width='10')
    display.grid(row=2,column=13)
    display=tk.Label(text=numbers1[i],height='2',width='10')
    display.grid(row=3,column=13)
    button=[]
    colour=['snow','orange','green','skyblue','pink','yellow']
    c=0
    
    
    
    for j in range(18):
        if j%3==0:
            c+=1
        for k in range(9):
            button.append([])
            integer=(j*(9)+k)
            num=ticket[j][k]
            if num in extra:
                if num==extra[-1]:
                    integer=(j*(9)+k)
                    def display():
                        button[integer]=tk.Button(text=num,height='2',width='2',fg='black')
                        button[integer].configure(bg='red')
                    button[integer]=tk.Button(text=num,height='2',width='2',fg='black',bg=colour[c-1],command=display)
                    button[integer].grid(row=j,column=k,sticky="nsew")
                elif num!=extra[-1]:
                    button[integer]=tk.Button(text=num,height='2',width='2',fg='black',bg='red')
                    button[integer].grid(row=j,column=k,sticky="nsew")
            elif num!=0:
                button[integer]=tk.Button(text=num,height='2',width='2',fg='black',bg=colour[c-1])
                button[integer].grid(row=j,column=k,sticky="nsew")
            elif num==0:
                button[integer]=tk.Button(text='',height='2',width='2',fg='black',bg=colour[c-1])
                button[integer].grid(row=j,column=k,sticky="nsew")
    i+=1
    if i>=2:
        display=tk.Label(text='previous number',height='2',width='10')
        display.grid(row=9,column=13)
        display=tk.Label(text=numbers1[i-2],height='2',width='10')
        display.grid(row=10,column=13)

buton=tk.Button(text="click me",height='2',width='10',command = run_program)
buton.grid(row=7,column=13,sticky="nsew")
window.mainloop()


# In[ ]:




