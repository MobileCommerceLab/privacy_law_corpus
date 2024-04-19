import nltk
import os
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize


## FILE PATH AND READING
docs =list()

### This code will take in the .txt corpus documents as inputs and will chunk them into tiny paragraphs and write them into multiple different .txt files.
### The text files having the chunked data is given as input to the NLTK Topic Modeling Code

'''
### Rules for Chunking ###
--------------------------
1.  Open each file in the corpus
2.  Split the text into paragraphs using the "\n\n" as a delimiter (if there are 2 line spaces between strings, then they are considered as different paragraphs)
3.  The maximum words in a pragraph can be between 9 and 1133.
    If less than 9, we will not include it and will remove it from final output
    If between 9 and 1133, we will check if its 10 sentences or less and will write it into a .txt file. 
    If greater than 1133 (or) greater than 10 sentences, we will chunk it again into smaller chunks and then will write into a .txt file
'''


### This p1 and p2 pair is for a set of documents in the same folder, if more sets of documents in different folders have to be chunked, then change the p1 and p2 path accordingly and re-run the code
p1 = "F:/native_english_text_files"  ## To change input folder path
p2="F:/Native_English_Split"    ## To change output folder path



h = 1 # GLOABL VARIABLE FOR APPENDING TO OUTPUT FILE NAME

dir_list_1 = os.listdir(p1)
len1 = len(dir_list_1)
for i in range(0,len1): #len1):
    path = p1 + "/" + dir_list_1[i]
    docs.append(str(path))

big_para = []
small_para = []
for i in docs:
    with open(i,"r",encoding="utf-8",errors="ignore") as file:
        data = file.read()
        paragraph1 = data.split("\n\n")
        
        for j in paragraph1:
            if len(str(j).split()) <= 9:
                continue
            else:
                if len(str(j).split()) > 1133:
                        temp_para1 = []

                        temp_para1.append(sent_tokenize(str(j)))
                        
                        count = 0
                        word_para = ""
                        for i in temp_para1:
                             if count == 10:
                                if len(str(j).split()) >= 9:
                                    small_para.append(word_para)

                             if count > 10:
                                  count = 0
                                  word_para = ""
                             
                             word_para = word_para + str(i)
                             count += 1
                else:
                    small_para.append(j)           


#print(len(small_para))
for k in small_para: 
    path2=p2+"/"+"para_"+str(h)+".txt"
    h += 1
    file = open(path2,"w",encoding="utf-8")
    file.write(str(k))
    file.close()

