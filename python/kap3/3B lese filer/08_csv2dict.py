import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.ttk as ttk
import csv
import json

file_path = "innvandring.csv"

heads = []
tabell = []
info = []
blank = []
heads = []
enc = "Windows 1252"
with open(file_path, encoding=enc) as csvf:
    all_rows = csv.reader(csvf, delimiter=";")
    info = next(all_rows)
    blank = next(all_rows)
    heads = next(all_rows)
    for row in all_rows:
        tabell.append(row)

csv_dic = []  

info1 = []
blank1 = []
heads1 = []

def csv2dict(skiprows, delimiter, enc):

    with open(file_path, encoding = enc) as csvf:

        for i in range(skiprows):
            next(csvf)
        all_rows = csv.DictReader(csvf,delimiter = delimiter)
        for row in all_rows:
            csv_dic.append(row)
        #print(csv_dic)

def table_like(tab):
    for row in tab:
        for element in row:
            print(f"{element[0:20]} ", end = "")
        print()

def table_like_dic(dic):
    for land in dic.keys():
        print(f"Land: {land}. Totalt akkumulert innvandring: {dic[land]["accum"]}")

def categorise():
    dic = {}

    for row in tabell:
        if row[0] not in dic.keys():
            dic[row[0]]={}
            dic[row[0]]["year"] = []
            dic[row[0]]["pop"] = []
            dic[row[0]]["accum"] = 0
        else:
            dic[row[0]]["year"].append(int(row[1]))
            dic[row[0]]["pop"].append(int(row[2]))
            dic[row[0]]["accum"] += int(row[2])
            
    return dic

def graph(x,y):
    fig, ax = plt.subplots(1,1)
    ax.plot(x, y)
    plt.show()

big_dic = categorise()
#print(big_dic)            

graph(big_dic["Afrika"]["year"],big_dic["Afrika"]["pop"])

#oppgave 1: Tabell-liknende struktur
table_like_dic(big_dic)


#Oppgave 2: Grafisk fremstilling av noen valgte verdensdeler
countries = {}
years = []