### IMPORT LIBRARIES
import nltk
import os
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import gensim
from gensim import corpora


### CREATING STOP WORD LIST 
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very','can', 'will', 'just', "don't", 'should', "should've", 'now', 'more', 'ain', 'are', "aren't", 'could', "couldn't", 'did', "didn't", 'does', "doesn't", 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'is', "isn't", 'might', "mightn't", 'must', "mustn't", 'need', "needn't", 'shall', 'should', "shouldn't", 'was', "wasn't", 'were', "weren't", 'will', "won't", 'would', "wouldn't"]
#print(stop_words)

new_stop_words = ['article','chapter','number','section','provision','within', 'five','hundred', ',', "'", '[', ']', '(', ')', "on", "the", "of","shall","must","mean","made","paragraph","change","part","referred" ] #paragraphe, dans
stop_words.extend(new_stop_words)

#month_number = ['one','two','three','four','five','six','seven','eight','nine','ten','hundred','january','february','march','april','may','june','july','august','september','october','december']
month_number = ['first','five','hundred','december']
stop_words.extend(month_number)

countries = ['european', 'union', 'coe', 'uruguay', 'mauritius', 'senegal', 'tunisia', 'african', 'africa', 'asia-pacific', 'economic', 'switzerland', 'nations', 'abu', 'dhabi', 'albania', 'algeria', 'andorra', 'angola', 'barbuda', 'antigua', 'argentina', 'armenia', 'aruba', 'australia', 'austria', 'azerbaijan', 'bahamas', 'bahrain', 'india', 'barbados', 'belarus', 'belgium', 'benin', 'bermuda', 'estatius', 'sint', 'saba', 'bonaire', 'bes', 'islands', 'bhutan', 'bolivia', 'herzegovina', 'bosnia', 'botswana', 'brazil', 'bulgaria', 'burkina', 'faso', 'california', 'canada', 'cambodia', 'cameroon', 'cape', 'verde', 'cayman', 'islands', 'chad', 'chile', 'china', 'colombia', 'republic', 'congo', 'costa', 'rica', 'cote', "d'ivoire", 'croatia', 'curaâˆšãÿao', 'cyprus', 'czech', 'republic', 'democratic', 'republic', 'congo', 'denmark', 'dominican', 'dubai', 'timor', 'ecuador', 'el', 'salvador', 'estonia', 'eswatini', 'ethiopia', 'faroe', 'islands', 'finland', 'fiji', 'france', 'gabon', 'georgia', 'germany', 'ghana', 'gibraltar', 'greece', 'greenland', 'guernsey', 'guatemala', 'guyana', 'guinea', 'hong', 'kong', 'sar', 'hungary', 'honduras', 'iraq', 'iran', 'iceland', 'indonesia', 'ireland', 'isle', 'israel', 'italy', 'jamaica', 'japan', 'jersey', 'kazakhstan', 'kenya', 'korea','south', 'kosovo', 'kuwait', 'kyrgyz', 'republic', 'latvia', 'lebanon', 'lesotho', 'liechtenstein', 'lithuania', 'luxembourg', 'macao', 'macedonia',  'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 'mauritania', 'mexico', 'moldova', 'monaco', 'mongolia', 'montenegro', 'morocco', 'mozambique', 'myanmar', 'nepal', 'netherlands', 'new', 'zealand', 'nicaragua', 'niger', 'nigeria', 'norway', 'oman', 'pakistan', 'panama', 'paraguay', 'peru', 'phillippines', 'poland', 'portugal', 'qatar', 'qatar', 'financial', 'romania', 'russia', 'san', 'marino', 'sâˆšâ£o', 'tomâˆšâ©', 'saudi', 'arabia', 'serbia', 'seychelles', 'singapore', 'slovakia', 'slovenia', 'somalia', 'south', 'africa', 'spain', 'sri', 'lanka', 'st.', 'lucia', 'vincent', 'grenadines', 'sweden', 'taiwan', 'tajikistan', 'tanzania', 'thailand', 'togo', 'trinidad', 'tobago', 'turkey', 'turkmenistan', 'uganda', 'ukraine', 'arab', 'emirates', 'kingdom', 'uzbekistan', 'venezuela', 'vietnam', 'yemen', 'zambia', 'zimbabwe']
stop_words.extend(countries)


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


