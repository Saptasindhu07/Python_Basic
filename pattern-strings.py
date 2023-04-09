# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 03:49:17 2023

@author: Sapta Sindhu Palit
"""

string1=input("Enter 1st string ")
string2=input("Enter 2nd String ")
if(len(string1)>len(string2)):
    print(string2)
    a=0
    b=len(string1)
    print(len(string1))
    if(len(string1)%2==0):
        k=len(string1)
        c=0
        for i in range(0,int(len(string1)/2)):
            h="  "*c
            print(h,end="")
            st=string1[a]
            st2=string1[b-1]
            t="  "*(k-1)
            print(st,t,st2)
            a=a+1 
            b=b-1 
            k=k-2 
            c=c+1