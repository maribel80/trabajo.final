#!/usr/bin/env python
# coding: utf-8

# In[12]:


import requests  
import re          
u2=requests.get("https://www.ncbi.nlm.nih.gov/gene/?term=ABCG2%C2%A0+bos+taurus") 
gen1=re.findall(r'(Chromosome.+3215.)',u1.text)
u4=requests.get("https://www.ncbi.nlm.nih.gov/gene/?term=ACO2%C2%A0+bos+taurus") 
gen3=re.findall(r'(Chromosome.+183.)',u4.text)
u6=requests.get("https://www.ncbi.nlm.nih.gov/gene/?term=ADAMTS12%C2%A0%C2%A0+bos+taurus") 
gen5=re.findall(r'(Chromosome.+8041.)',u6.text)
u7=requests.get("https://www.ncbi.nlm.nih.gov/gene/?term=ADGRB1%C2%A0%C2%A0+bos+taurus") 
gen6=re.findall(r'(Chromosome.+4927.............)',u7.text)
u11=requests.get("https://www.ncbi.nlm.nih.gov/gene/?term=AGBL4%C2%A0+bos+taurus") 
gen10=re.findall(r'(Chromosome.+3389.)',u11.text)
u12=requests.get("https://www.ncbi.nlm.nih.gov/gene/?term=AGO2+bos+taurus") 
gen11=re.findall(r'(Chromosome.+8228.)',u12.text)
u15=requests.get("https://www.ncbi.nlm.nih.gov/gene/?term=ANKRD17+bos+taurus") 
gen14=re.findall(r'(Chromosome.+5145.............)',u15.text)
u16=requests.get("https://www.ncbi.nlm.nih.gov/gene/?term=ANKRD52+bos+taurus") 
gen15=re.findall(r'(Chromosome.+6731.)',u16.text)
u17=requests.get("https://www.ncbi.nlm.nih.gov/gene/?term=ANO6+bos+taurus") 
gen16=re.findall(r'(Chromosome.+0394.............)',u17.text)
u18=requests.get("https://www.ncbi.nlm.nih.gov/gene/?term=ARFGEF1+bos+taurus") 
gen17=re.findall(r'(Chromosome.+6714.............)',u18.text)

print(gen1)
print(gen3)
print(gen5)
print(gen6)
print(gen10)
print(gen11)
print(gen14)
print(gen15)
print(gen16)
print(gen17)

