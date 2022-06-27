#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy # nlp
import pdfminer # pdf2txt
import re # regex
import os # file manipulation
import pandas as pd # csv - tabular


# In[2]:


import pdf2txt


# In[3]:


def convert_pdf(file_name):
    filename_txt = os.path.basename(os.path.splitext(file_name)[0]) + ".txt" # basename but with txt instead of pdf
    filepath_txt = os.path.join("output/txt/", filename_txt) # output path
    pdf2txt.main(args=[file_name, "--outfile", filepath_txt]) # pdf to txt and save it in the given location
    print(f"{filepath_txt} saved successfully!")
    with open(filepath_txt) as to_read:
        return to_read.read()
    # return open(filepath_txt).read()


# In[4]:


nlp = spacy.load("en_core_web_sm") # load the language model


# In[5]:


result_dict = {'name': [], 'phone': [], 'email': [], 'skills': []}
names = []
phones = []
emails = []
skills = []


# In[6]:


def parse_content(text):
    skillset = re.compile("python|java|sql|hadoop|tableau")
    phone_num = re.compile(
    "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
    )
    nlp_text = nlp(text)
    name = [entity.text for entity in nlp_text.ents if entity.label_ == "PERSON"][0]
    email = [word for word in nlp_text if word.like_email is True][0]
    print(f"Name: {name}, E-mail: {email}")
    phone = re.findall(phone_num, text.lower())
    skills_list = re.findall(skillset, text.lower())
    unique_skills_list = list(set(skills_list))
    
    names.append(name.strip())
    emails.append(email)
    phones.append(phone)
    skills.append(unique_skills_list)
    
    print("Extraction completed successfully!\n")


# In[7]:


def for_file_in_ls():
    for file_name in os.listdir('resumes/'):
        if file_name.endswith('.pdf'):
            print(f"Reading {file_name}")
            txt = convert_pdf(os.path.join('resumes/', file_name))
            parse_content(txt)


# In[8]:


for_file_in_ls()


# In[13]:


result_dict["name"] = names
result_dict["phone"] = phones
result_dict["email"] = emails
result_dict["skills"] = skills


# In[15]:


result_df = pd.DataFrame(result_dict)
result_df


# In[28]:


result_df.to_csv("output/csv/parsed_resumes.csv")

