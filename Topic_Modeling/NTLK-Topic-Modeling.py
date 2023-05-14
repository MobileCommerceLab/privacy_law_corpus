### IMPORT LIBRARIES
import nltk
import os
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import gensim
from gensim import corpora


### CREATING STOP WORD LIST 
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very','can', 'will', 'just', "don't", 'should', "should've", 'now', 'more', 'ain', 'are', "aren't", 'could', "couldn't", 'did', "didn't", 'does', "doesn't", 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'is', "isn't", 'might', "mightn't", 'must', "mustn't", 'need', "needn't", 'shall', 'should', "shouldn't", 'was', "wasn't", 'were', "weren't", 'will', "won't", 'would', "wouldn't"]

new_stop_words = ['article','chapter','number','section','provision','within', 'five','hundred', ',', "'", '[', ']', '(', ')', "on", "the", "of","shall","must","mean","made","paragraph","change","part","referred" ] #paragraphe, dans
stop_words.extend(new_stop_words)

month_number = ['first','one','two','three','four','five','six','seven','eight','nine','ten','hundred','january','february','march','april','may','june','july','august','september','october','december','dated', 'lexuz','edition','mean',"datos"]
#month_number = ['first','five','hundred','december','april','dated', 'lexuz', 'june' , 'january', 'edition', 'march']
stop_words.extend(month_number)

countries = ['european', 'coe', 'uruguay', 'mauritius', 'senegal', 'tunisia', 'african', 'africa', 'asia-pacific', 'economic', 'switzerland', 'nations', 'abu', 'dhabi', 'albania', 'algeria', 'andorra', 'angola', 'barbuda', 'antigua', 'argentina', 'armenia', 'aruba', 'australia', 'austria', 'azerbaijan', 'bahamas', 'bahrain', 'india', 'barbados', 'belarus', 'belgium', 'benin', 'bermuda', 'estatius', 'sint', 'saba', 'bonaire', 'bes', 'islands', 'bhutan', 'bolivia', 'herzegovina', 'bosnia', 'botswana', 'brazil', 'bulgaria', 'burkina', 'faso', 'california', 'canada', 'cambodia', 'cameroon', 'cape', 'verde', 'cayman', 'islands', 'chad', 'chile', 'china', 'colombia', 'republic', 'congo', 'costa', 'rica', 'cote', "d'ivoire", 'croatia', 'curaâˆšãÿao', 'cyprus', 'czech', 'republic', 'democratic', 'republic', 'congo', 'denmark', 'dominican', 'dubai', 'timor', 'ecuador', 'el', 'salvador', 'estonia', 'eswatini', 'ethiopia', 'faroe', 'islands', 'finland', 'fiji', 'france', 'gabon', 'georgia', 'germany', 'ghana', 'gibraltar', 'greece', 'greenland', 'guernsey', 'guatemala', 'guyana', 'guinea', 'hong', 'kong', 'sar', 'hungary', 'honduras', 'iraq', 'iran', 'iceland', 'indonesia', 'ireland', 'isle', 'israel', 'italy', 'jamaica', 'japan', 'jersey', 'kazakhstan', 'kenya', 'korea','south', 'kosovo', 'kuwait', 'kyrgyz', 'republic', 'latvia', 'lebanon', 'lesotho', 'liechtenstein', 'lithuania', 'luxembourg', 'macao', 'macedonia',  'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 'mauritania', 'mexico', 'moldova', 'monaco', 'mongolia', 'montenegro', 'morocco', 'mozambique', 'myanmar', 'nepal', 'netherlands', 'new', 'zealand', 'nicaragua', 'niger', 'nigeria', 'norway', 'oman', 'pakistan', 'panama', 'paraguay', 'peru', 'phillippines', 'poland', 'portugal', 'qatar', 'qatar', 'financial', 'romania', 'russia', 'san', 'marino', 'sâˆšâ£o', 'tomâˆšâ©', 'saudi', 'arabia', 'serbia', 'seychelles', 'singapore', 'slovakia', 'slovenia', 'somalia', 'south', 'africa', 'spain', 'sri', 'lanka', 'st.', 'lucia', 'vincent', 'grenadines', 'sweden', 'taiwan', 'tajikistan', 'tanzania', 'thailand', 'togo', 'trinidad', 'tobago', 'turkey', 'turkmenistan', 'uganda', 'ukraine', 'arab', 'emirates', 'kingdom', 'uzbekistan', 'venezuela', 'vietnam', 'yemen', 'zambia', 'zimbabwe']
stop_words.extend(countries) 
# 'union' - removed on 30-th april


### CREATING FUNCTION TO TOKENIZE AND LEMATIZE
lemmatizer = WordNetLemmatizer()

# define function to preprocess text
def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower()) # lowercase and tokenize
    tokens = [token for token in tokens if token.isalpha() and token not in stop_words] # remove stopwords and non-alphabetic characters
    tokens = [lemmatizer.lemmatize(token) for token in tokens] # lemmatize words
        #len(tokens)
    tokens = [x for x in tokens if len(x)>3]  # To remove tokens with length less than 3 ## Reviewer said do not remove words less than 3, e.g. IP, MAC
    return tokens



### Read all the names of the text documents from the given path and stores the "path+filename.txt" values in doc
docs =list()
p1="F:/Native_English_Documents"  ## Change Path
dir_list_1 = os.listdir(p1)
len1 = len(dir_list_1)
for i in range(0,len1): #len1):
    path = p1 + "/" + dir_list_1[i]
    docs.append(str(path))

p2="F:/Translated_English_Documents"  ## Change Path
dir_list_2 = os.listdir(p2)
len2 = len(dir_list_2)
for i in range(0,len2): #len1):
    path = p2 + "/" + dir_list_2[i]
    docs.append(str(path)) 

    

#### LDA Topic Modeling
# preprocess documents
preprocessed_docs = [preprocess_text(open(doc,encoding="utf-8",errors="ignore").read()) for doc in docs]

# create dictionary and corpus
dictionary = corpora.Dictionary(preprocessed_docs)
corpus = [dictionary.doc2bow(doc) for doc in preprocessed_docs]

# run LDA on corpus
num_topics = 6 # number of topics to extract
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, passes=9, update_every=2)

# print out topics and write them into a file
file = open("6Topics9-Passes-update_every2.txt","w")
for topic in lda_model.print_topics():
    file.write(str(topic)+"\n\n")
    print(topic)
file.close()



### LDA Output Analysis -> Generates an interactive html report to do 1.)Intertopic Distance Map and 2.) Top-30 Most Relevant Terms for Topic number "i"
import pyLDAvis.gensim
import pickle 
import pyLDAvis

# Visualize the topics
pyLDAvis.enable_notebook()
LDAvis_data_filepath = os.path.join('F:/ldavis_report_'+str(num_topics))  ## Change path

## Statement must be true for the output report to be generated
if 1 == 1:
    LDAvis_prepared = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary)
    with open(LDAvis_data_filepath, 'wb') as f:
        pickle.dump(LDAvis_prepared, f)
# load the pre-prepared pyLDAvis data from disk
with open(LDAvis_data_filepath, 'rb') as f:
    LDAvis_prepared = pickle.load(f)
pyLDAvis.save_html(LDAvis_prepared, 'F:/ldavis_report_'+ str(num_topics) +'.html')  ## Change Path
LDAvis_prepared
