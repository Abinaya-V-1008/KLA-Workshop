import cv2
import pandas as pd
import sys
import collections
import csv
import numpy as np

#print(cv2.__version__)
import json
f=open('input.json')
data=json.load(f)
for i in data['die']:
    print(i)

#img = cv2.imread('wafer_image_1.png')
#print(img.shape)
#print(img)

#extracting single pixel
#print(img[0][1])

img1=cv2.imread('wafer_image_1.png',0)
img2=cv2.imread('wafer_image_2.png',0)
img3=cv2.imread('wafer_image_3.png',0)
img4=cv2.imread('wafer_image_4.png',0)
img5=cv2.imread('wafer_image_5.png',0)
images=[img1,img2,img3,img4,img5]

#cv2.imshow('GrayScale',img1)
print(img1.shape)
print(img1)
print(img2)
print(img1[1][0])


checkmatrix=[]
rows,cols=600,800
for i in range(rows):
	col = []
	for j in range(cols):
		col.append(0)
	checkmatrix.append(col)
#print(checkmatrix)

csvlist=[]

def findmin(frequency,l):
    if(len(frequency)!=1):
        temp=min(frequency.values())
        res=[key for key in frequency if frequency[key] == temp]
        #print(value)
        #print(len(l))
        return res[0]
        

def findfreq(l):
    frequency = collections.Counter(l)
    #print(len(l))
    frequency=dict(frequency)
    #print(frequency)

    return frequency


      
for i in range(0,600):
    l=[]
    for j in range(0,800):
        l.append(img1[i][j])
        l.append(img2[i][j])
        l.append(img3[i][j])
        l.append(img4[i][j])
        l.append(img5[i][j])
        #print(l)
        frequency=findfreq(l)
        if(len(frequency)==2):
            value=findmin(frequency,l)
            for k in range(0,len(l)):
                if(l[k]==value):
                    if(k==0):
                        csvlist.append([1,j,abs(i-599)])
                    if(k==1):
                        csvlist.append([2,j,abs(i-599)])
                    if(k==2):
                        csvlist.append([3,j,abs(i-599)])
                    if(k==3):
                        csvlist.append([4,j,abs(i-599)])
                    if(k==4):
                        csvlist.append([5,j,abs(i-599)])
        if(len(frequency)>=3):
            temp=max(frequency.values())
            res=[key for key in frequency if frequency[key] == temp]
            maxvalue=res[0]
            print(maxvalue)
            values=list(frequency.keys())
            values.remove(maxvalue)
            print(values)
            for ans in values:
                for k in range(0,len(l)):
                    if(l[k]==ans):
                        if(k==0):
                            csvlist.append([1,j,abs(i-599)])
                        if(k==1):
                            csvlist.append([2,j,abs(i-599)])
                        if(k==2):
                            csvlist.append([3,j,abs(i-599)])
                        if(k==3):
                            csvlist.append([4,j,abs(i-599)])
                        if(k==4):
                            csvlist.append([5,j,abs(i-599)])

             

       

        l=[]

#print(csvlist[0])

if(len(csvlist)!=0):
    with open ('defective3.csv','w',newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(csvlist)

    data=pd.read_csv('defective3.csv',header=None,index_col=None)
    print(data)