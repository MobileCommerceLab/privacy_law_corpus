import os
import re
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import re

## Storing the name of the Directory to traverse and identify files##
p1 = "F:/CODE/english_translated_text_files/" #directory 1
p2 = "F:/CODE/native_english_text_files/" #directory 2

path = "F:/Categories in Text Files/" ## Text files for 14 different categories are saved in this path ## They contain various terminologies grouped under specific categories

# File names of 14 categroies of terms 
category_files = ['finance.txt', 'work.txt', 'health.txt', 'biometric.txt', 'genetic.txt', 'bio-demographic.txt', 'race-ethinicity.txt', 'belief.txt', 'technology.txt', 'tracking_ID.txt', 'govt-personal-ID.txt', 'location.txt', 'contact.txt', 'misc.txt']

### There are 14 categories of PII data, and each category of terms is in a text file (14 .txt files in total)

### Appending .txt filename to the path 
category_files_1 = []
for i in category_files:
    category_files_1.append(str(path)+str(i))


multi_list = [[]]  ## Empty multidimensional list 


### opening each text file and storing the terms in a temporary list. Appending this list to the multi_list to create a Multi-dimensional list
for i in category_files_1:
    with open(i,"r") as file:
        lines = [" "+line.rstrip()+" " for line in file] 

    # print(lines)
    #print(len(lines))
    multi_list.append(lines)
    #print("######End of file######\n\n\n")
multi_list.pop(0)   ## Popping out the 1st sub-list of the multi_list as it is an empty list


#### Getting the count of the category with the maximum number of words
max_value = 0
for i in multi_list:
    temp = len(i)
    if temp > max_value:
        max_value = temp

#### Adding None Keyword to make all the sub-lists in multi_list equal in size
## Getting length of each sublist and finding difference between max_value and the length. Then the the "None" keyword is added until the difference

for i in range(14):
    length = len(multi_list[i])
    difference = max_value - length
    for j in range(difference):
        multi_list[i].append(None)

# for i in multi_list:
#     print(i)
#     print(len(i),"\n\n")



## Converting multi_list into an np array
keywords1 = np.array(multi_list)

## Getting names of all files present in the directories ##
dir_list_1=os.listdir(p1)
len1 = len(dir_list_1) 
#print(dir_list_1)
#print(len1)

dir_list_2=os.listdir(p2)
len2 = len(dir_list_2)
#print(dir_list_2)
#print(len2)

result = np.zeros((14,max_value), dtype= int)




## Converting the caetgory names into dictionary ## This will be used for storing the count values

category = ['finance', 'work', 'health', 'biometric', 'genetic', 'bio-demographic', 'race-ethinicity', 'belief', 'technology', 'tracking_ID', 'govt-personal-ID', 'location', 'contact', 'misc']
category_dict = dict()
for i in category:
    category_dict[str(i)] = 0
print(category_dict)




lemmatizer = WordNetLemmatizer()
def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower()) # lowercase and tokenize
    tokens = [token for token in tokens if re.match(r'^[a-zA-Z]+$', token)] #and token not in stop_words] # remove stopwords and non-alphabetic characters
    tokens = [lemmatizer.lemmatize(token) for token in tokens] # lemmatize words
    a = " ".join(tokens)
    return a

### Translated English Documents
for i in range(0,len1):
    path_1 = p1 + dir_list_1[i]
    #print(path_1)
    file_cont = None
    with open(path_1, "r",encoding="utf-8",errors="ignore") as file:
        data = file.read()
        data = data.lower()
        file_cont = preprocess_text(data)

    for j in range(0,14):
        for k in range(max_value):
            count = 0   
            word = keywords1[j][k]
            if word != None and word in file_cont:
                count = count + 1
            if count >= 1:
                result[j][k] = result[j][k] + 1 


### Native English Documents
for i in range(0,len2):
    path_1 = p1 + dir_list_1[i]
    #print(path_1)
    file_cont = None
    with open(path_1, "r",encoding="utf-8",errors="ignore") as file:
        data = file.read()
        data = data.lower()
        file_cont = preprocess_text(data)

    for j in range(0,14):
        for k in range(max_value):
            count = 0   
            word = keywords1[j][k]
            if word != None and word in file_cont:
                count = count + 1
            if count >= 1:
                result[j][k] = result[j][k] + 1 

# #### Code to print output and check  ## To comment this code
# for i in range(14):
#     sum = 0
#     print(category[i])
#     for j in range(max_value):
#         temp = result[i][j]
#         if temp != 0:
#             print(keywords1[i][j])
#             print(temp,"#")
#         sum = sum + temp
#     print("total sum is",sum)
#     print("######")




#### Graph Plotting Code
for i, category_name in enumerate(category):
    sum = 0
    for j in range(max_value):
        sum = result[i][j] + sum
    category_dict[category_name] = sum

finance = category_dict['finance']
work = category_dict['work']
health = category_dict['health']
biometric = category_dict['biometric']
genetic = category_dict['genetic']
bio = category_dict['bio-demographic']
race = category_dict['race-ethinicity']
belief = category_dict['belief']
tech = category_dict['technology']
tracking = category_dict['tracking_ID']
govt = category_dict['govt-personal-ID']
location = category_dict['location']
contact = category_dict['contact']
misc = category_dict['misc']

print("Total")
print("#######")
print("finance:",finance)
print("work:",work)
print("health:",health)
print("biomteric:",biometric)
print("genetic:",genetic)
print("bio-demographic:",bio)
print("race-ethinicity:",race)
print("belief",belief)
print("technology:",tech)
print("tracking-ID:",tracking)
print("Government-personal-ID:",govt)
print("location:",location)
print("contact",contact)
print("miscellaneous",misc)

total = len1/100
final_graph_list = [finance/total, work/total, health/total, biometric/total, genetic/total, bio/total, race/total, belief/total, tech/total, tracking/total, govt/total, location/total, contact/total, misc/total]

import matplotlib.pyplot as plt

plt.bar( x = ['finance', 'work', 'health', 'biometric', 'genetic', 'bio-demographic', 'race-ethinicity', 'belief', 'technology', 'tracking-ID', 'govt-personal-ID', 'location', 'contact', 'miscellaneous'], height = final_graph_list)
plt.ylabel('percentage of documents')
plt.show()
