#step-01
#importing required libraries 
import requests
from bs4 import BeautifulSoup
import nltk
import urllib.request 

#step-03
#Creating Beautifill soup 
url='https://www.flipkart.com/mobile-phones-store?otracker=nmenu_sub_Electronics_0_Mobiles'
respnse=requests.get(url)
page=respnse.text
html=BeautifulSoup(page, 'html.parser')

#select all div tags in web page 
span= html.select('div',{'class':'_2kSfQ4','style':'width: 195px;'})

#convert into string 
span=str(span)

#convert string into Words
span=nltk.word_tokenize(span)

#step-04

#function to collect the required information like mobile name,price,camera info like that  
def mobile_info(l):
    m_name=[]
    iUmrbN=0
    name_list=[]
    name_count=0
    M_qL_C=0
    price_list=[]
    p_list=[]
    L200Vs=0
    actual_list=[]
    a_list=[]
    s1=name_list
    new_list=''
    new_name_list=[]
    name_merge=[]
    common=[]
    c_list=[]
    BXlZdc=0
    for i in l:
        if i == 'iUmrbN':
            iUmrbN=iUmrbN+1
        if iUmrbN == 1:
            if i == '<':
                iUmrbN=0
                name_list.append(m_name[3:])
                m_name=[]
                for i in range(len(name_list)):
                    temp=name_list[i]
                    for j in range(len(temp)):
                        k=temp[j]
                        new_list=new_list+""+str(k)
                    common.append(new_list)
                    new_list=''   
                    name_list=[]
            else:
                m_name.append(i)
        if i == 'M_qL-C':
            M_qL_C=M_qL_C+1
        if M_qL_C == 1:
            if i == '/div':
                M_qL_C = 0
                common.append(p_list[9])
                p_list=[]
            else:
                p_list.append(i)
        
        if i == 'L200Vs':
            L200Vs = L200Vs+1
    
        if L200Vs == 1:
            if i == '/div':
                L200Vs = 0
                common.append(a_list[9])
                a_list=[]
            else:
                a_list.append(i)
        if i == 'BXlZdc':
            BXlZdc = BXlZdc+1
    
        if BXlZdc == 1:
            if i == '<':
                BXlZdc = 0
                common.append(c_list[3:9])
            else:
                c_list.append(i)
    return(common)


#step-05
#collect the required information using mobile_info() function 
Latest_Launches=[]
    

for i in range(len(span)):
    if span[i] == "Trending":
        #print(a[i])
        print(span[i])
        break
    else:
        #print(a[i])
        Latest_Launches.append(span[i])

Latest_Launches=mobile_info(Latest_Launches)

span_best=span[i:]
Best_selling_Phones=[]

for i in range(len(span_best)):
    if span_best[i] == "Front":
        #print(a[i])
        print(span_best[i])
        break
    else:
        #print(a[i])
        Best_selling_Phones.append(span_best[i])

Best_selling_Phones=mobile_info(Best_selling_Phones)

span_Selfie_camera_Phones=span_best[i:]

Selfie_camera_Phones=[]

for i in range(len(span_Selfie_camera_Phones)):
    if span_Selfie_camera_Phones[i] == "4000mAh":
        #print(a[i])
        print(span_Selfie_camera_Phones[i])
        break
    else:
        #print(a[i])
        Selfie_camera_Phones.append(span_Selfie_camera_Phones[i])

Selfie_camera_Phones=mobile_info(Selfie_camera_Phones)

span_Best_Battery_Phones=span_Selfie_camera_Phones[i:]
Best_Battery_Phones=[]

for i in range(len(span_Best_Battery_Phones)):
    if span_Selfie_camera_Phones[i] == "2.2":
        #print(a[i])
        print(span_Best_Battery_Phones[i])
        break
    else:
        #print(a[i])
        Best_Battery_Phones.append(span_Best_Battery_Phones[i])
 
    
Best_Battery_Phones=mobile_info(Best_Battery_Phones)

span_Fast_Processing_Phones=span_Best_Battery_Phones[i:]

Fast_Processing_Phones=[]

for i in range(len(span_Fast_Processing_Phones)):
    if span_Fast_Processing_Phones[i] == "Friendly":
        #print(a[i])
        print(span_Fast_Processing_Phones[i])
        break
    else:
        #print(a[i])
        Fast_Processing_Phones.append(span_Best_Battery_Phones[i])
 

Fast_Processing_Phones=mobile_info(Fast_Processing_Phones)


span_Best_Pocket_Friendly_Phones=span_Fast_Processing_Phones[i:]

Best_Pocket_Friendly_Phones=[]

for i in range(len(span_Best_Pocket_Friendly_Phones)):
    if span_Best_Pocket_Friendly_Phones[i] == "Other":
        #print(a[i])
        print(span_Best_Pocket_Friendly_Phones[i])
        break
    else:
        #print(a[i])
        Best_Pocket_Friendly_Phones.append(span_Best_Pocket_Friendly_Phones[i])
 


Best_Pocket_Friendly_Phones=mobile_info(Best_Pocket_Friendly_Phones)


span_High_RAM_Phones=span_Best_Pocket_Friendly_Phones[i:]

High_RAM_Phones=[]


for i in range(len(span_High_RAM_Phones)):
    if span_High_RAM_Phones[i] == "Best":
        #print(a[i])
        print(span_High_RAM_Phones[i])
        break
    else:
        #print(a[i])
        High_RAM_Phones.append(span_High_RAM_Phones[i])
     
        
        
High_RAM_Phones=mobile_info(High_RAM_Phones)        
        
span_Best_Camer_Smartphones=span_High_RAM_Phones[i:]

Best_Camer_Smartphones=[]
        
for i in range(len(span_Best_Camer_Smartphones)):
    if span_Best_Camer_Smartphones[i] == "Explore":
        #print(a[i])
        print(span_Best_Camer_Smartphones[i])
        break
    else:
        #print(a[i])
        Best_Camer_Smartphones.append(span_Best_Camer_Smartphones[i])
        
        

Best_Camer_Smartphones=mobile_info(Best_Camer_Smartphones)






