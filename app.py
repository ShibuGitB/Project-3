import cv2
import streamlit as st 
import tensorflow as tf 
import face_recognition 
import numpy as np 
import pytesseract 
import re 
import os 
import face_recognition 

details=cv2.imread(r"C:\Users\shibu\OneDrive\Documents\Deep learning projects\Email Generator through Face Recognition Open CV Project\Intern Students Details.jpg")
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
data=pytesseract.image_to_data(details,output_type=pytesseract.Output.DICT) 
n=len(data["text"]) 
name=[] 
email=[] 
place=[] 
qualification=[] 
phone=[] 
namere="[N][a][m][e]" 
emailre="[a-z0-9]+[@][g][m][a][i][l][.][c][o][m]" 
placere="[p][l][a][c][e]" 
qualire="[q][u][a][l][i][f][i][c][a][t][i][o][n]" 
phonere= "[9876][0-9]{9}" 
for i in range (n) : 
    
    if re.search(namere,data["text"][i]) : 
        
        name.append(data["text"][i]) 
        
print (name)
for i in range (n) : 
    
    if re.search(emailre,data["text"][i]) : 
        
        email.append(data["text"][i]) 
        
print (email)
for i in range (n) : 
    
    if re.search(placere,data["text"][i]) : 
        
        place.append(data["text"][i]) 
        
print (place)
for i in range (n) : 
    
    if re.search(qualire,data["text"][i]) : 
        
        qualification.append(data["text"][i]) 
        
print (qualification)
for i in range (n) : 
    
    if re.search(phonere,data["text"][i]) : 
        
        phone.append(data["text"][i]) 
        
print (phone)
categorydetails=[]
cd=[name,email,place,qualification,phone] 

for i in cd : 
    
    categorydetails.extend(i) 
LeoDas=[] 
Bilal=[]
Stephen=[] 
Vikram=[] 
DuraiSingham=[] 
Chakochi=[] 
MuthuvelPandiyan=[] 
ParamaSivam=[] 
Don=[] 
l="^[G][A]"
b="^[G][B]"
s="^[G][C]" 
v="^[G][D]" 
d="^[G][E]" 
c="^[G][F]" 
m="^[G][G]" 
p="^[G][H]" 
dn="^[G][J]"
for i in categorydetails : 
    
    if re.search (l,i) : 
        
        LeoDas.append(i) 
        
LeoDas
for i in categorydetails : 
    
    if re.search (b,i) : 
        
        Bilal.append(i) 
        
Bilal
for i in categorydetails : 
    
    if re.search (s,i) : 
        
        Stephen.append(i) 
        
Stephen
for i in categorydetails : 
    
    if re.search (v,i) : 
        
        Vikram.append(i) 
        
Vikram
for i in categorydetails : 
    
    if re.search (d,i) : 
        
        DuraiSingham.append(i) 
        
DuraiSingham
for i in categorydetails : 
    
    if re.search (c,i) : 
        
        Chakochi.append(i) 
        
Chakochi
for i in categorydetails : 
    
    if re.search (m,i) : 
        
        MuthuvelPandiyan.append(i) 
        
MuthuvelPandiyan
for i in categorydetails : 
    
    if re.search (p,i) : 
        
        ParamaSivam.append(i) 
        
ParamaSivam
for i in categorydetails : 
    
    if re.search (dn,i) : 
        
        Don.append(i) 
        
Don
folderpath=r"C:\Users\shibu\OneDrive\Documents\Deep learning projects\Email Generator through Face Recognition Open CV Project\Student Images"
studentimages=[] 
studentnames=[]
img=os.listdir(folderpath) 
for i in img : 
    
    imgpath=os.path.join(folderpath,i) 
    imgread=cv2.imread(imgpath) 
    studentimages.append(imgread) 
    studentnames.append(i[:-4]) 
def encodedlist (images) : 
    
    faceencoded=[] 
    
    for i in images : 
        
        rgb=cv2.cvtColor(i,cv2.COLOR_BGR2RGB) 
        face=face_recognition.face_locations(rgb) 
        encode=face_recognition.face_encodings(rgb,face)[0]
        faceencoded.append(encode) 
         
    return faceencoded 

knownfaces=encodedlist (studentimages)  
studentsdetailfiles=[Bilal,Chakochi,Don,DuraiSingham,LeoDas,MuthuvelPandiyan,ParamaSivam,Stephen,Vikram] 


st.title("Email generator through Face Recognition") 
st.text("upload image of the selected student for their Email......") 

def encoding (image) : 
    
    img=cv2.imread(image) 
    rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  
    face=face_recognition.face_landmarks(rgb) 
    encode=face_recognition.face_encodings(rgb,face) 
    
    return encode,face 

def prediction (image2) : 
    
    image3,face2=encoding(image2) 
    
    for encodevalue,face3 in zip(image3,face2) : 
        
        match=face_recognition.compare_faces(knownfaces,encodevalue) 
        distance=face_recognition.face_distance(knownfaces,encodevalue) 
        
    near=np.argmin(distance) 
    
    return(studentsdetailfiles[near]) 

def email (details) : 
    
    name=details[0][7:] 
    email=details[1][8:] 
    place=details[2][8:] 
    qualification=details[3][16:] 
    phone=details[4][8:] 
    return "This Mail is from GOOGLE india for the JOB selection information""\n""30/3/2024""\n",name,"\n",email,"\n",place,"\n""Dear",name,"\n""We are pleased to offer you employment at GOOGLE india . We feel that your skills and background will be valuable""\n""assets to our team.""\n""Per our discussion,the position is DATA-SCIENTIST. Your starting date will be 15-4-2024. The enclosed employee handbook""\n""outlines the medical and retirement benefits that our company offers.""\n""If you choose to accept this offer,please sign the second copy of this letter in the space provided and return it to us.""\n""And also mail a copy of your",qualification,"course completed certificate copy and a passport size photo of your self""\n""A stamped ,self-addressed envelope is enclosed for your convenience. And we will contact you on your phone -",phone,".""\n""We look forward to welcoming you as a new employee at GOOGLE.""\n""Sincerely""\n""\n""Prakash Kumar""\n""HR of GOOGLE""\n""enclosure"

uploadfile=st.file_uploader("choose an image :",type=["jpg","jpeg","png","webp"]) 

if uploadfile is not None : 
      
    step1=prediction(uploadfile) 
    email2=email(step1) 
    
    st.success(f"Email: {email2}")