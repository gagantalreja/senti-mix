import warnings
warnings.filterwarnings("ignore")
import nltk


class Result():
      def __init__(self,one,two,chck,profanity_,txt,all_text):
            self.scoreList=one
            self.score=two
            self.textblob=chck
            self.profanity=profanity_
            self.generatedText=txt
            self.completeText=all_text
            

#Install This Library
#!pip install googletrans
#nltk.download('punkt')

#stop word list
stop_word=['ourselves','hers','between','yourself','but','again','there','about','once','during','out','very','having','with','they','own','an','be','some','for','do','its','yours','such','into','of','most','itself','other','off','is','s','am','or','who','as','from','him','each','the','themselves','until','below','are','we','these','your','his','through','don','nor','me','were','her','more','himself','this','down','should','our','their','while','above','both','up','to','ours','had','she','all','no','when','at','any','before','them','same','and','been','have','in','will','on','does','yourselves','then','that','because','what','over','why','so','can','did','not','now','under','he','you','herself','has','just','where','too','only','myself','which','those','i','after','few','whom','t','being','if','theirs','my','against','a','by','doing','it','how','further','was','here','than']

import pandas as pd
import re
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import sent_tokenize
from textblob import TextBlob
import tests
import string
from tests import SchemeMap, SCHEMES, transliterate
from googletrans import Translator
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras import backend as K_
import profanity

translator = Translator()   

#Remove stopwords, do stemming.
def get_keywords(row):     
      tokens = row.split()
      re_punc = re.compile('[%s]' % re.escape(string.punctuation))
      tokens = [re_punc.sub('', w) for w in tokens]
      tokens = [word for word in tokens if word.isalpha()]
      stop_words =stop_word #set(stopwords.words('english'))
      tokens = [w for w in tokens if w not in stop_words]
      porter = PorterStemmer()
      stemmed = [porter.stem(word) for word in tokens]
      tokens = [word for word in tokens if len(word) > 1]
      return str(" ".join(tokens))

#sample=['Madarchod muslim se nafrat karta hai भोस्डिके','chod! ye sab chutiye hai!','well have a model for the rest of language','and start thinking about the long long line from b to e','then theyll live years longer”','in order to understand whether this is true','to why india is today growing','Come on girls, waqt hai shine karne ka!','Yeh Dil maange more','Kya aap Close Up karte hain?','Life ho to aisi','Pal banaye magical','What your bahana is?','Inka kaam hi hai, inhe paise hi is kaam ke milte hai','Ye banda jo kahta ha o jarur karta hai, aur jo nahi kahta hai o to definitely karta','Muslim personal law board ko khatam kiya jaye ya fir jitne bhi dharm india me he sabke apne apne personal law board khol do','Fake currency, aatankvad, corruption San khatam honai wala tha #notebandi sa? Kyo n hua? Sawal puchna ki himmat hai sir?','As per pappu @RahulGandhi India has come at the bottom of list']
sample=["rahul gandhi chor hai","Model ka output nhi ara randi ke bache","vipul jabardasti ka hua va baccha hai","ik gaand mein marunga sahi hojayega vipul"]   
##def run(temp=['madarchodo ko lagta hai ki apne baap se panga lega toh bhut accha hoga','Madarchod muslim se nafrat karta hai','chamko toh sirf hero ki tarah']):
##
##    
def run(temp=sample):   
    profanity_={}
    chck=[]

    for i in range(len(temp)):
        profanity_[i]=profanity.prof(temp[i])

    model = load_model('Fmodel.hdf5')


    #List of sentences
    

    '''
    Text Conversion start

    with the pattern -> translate to hindi -> transliterate to hindi -> translate to english

    '''

    df={"text":[]}
    all_text={"Given":[],"HindiTranslated":[],"HindiTransliterate":[]}
    
    for i in temp:
      try:
        i=i.strip()
        df['text'].append(i)
      except Exception as e:
        print(e,'error',i)


    for i in range(len(df['text'])):
      data = str(""+str(df['text'][i])+"")
      try:

            token = sent_tokenize(data)
            u=''
            nu=''
            for tt in token:
                  translatedText = translator.translate(tt, dest="hi")
                  u+=translatedText.text+" "
                  nu+=translatedText.text+" "
                  u=transliterate(u, tests.ITRANS, tests.DEVANAGARI)
                  #print(u)
            all_text['Given'].append(data); all_text['HindiTranslated'].append(nu);all_text['HindiTransliterate'].append(u)
            
            t=TextBlob(u).translate(from_lang='hi',to='en')
            chck.append(t.sentiment.polarity)
            #print(t)
            df['text'][i]=str(t)

      except Exception as e:
        print("Error",e)
        try:
            data = str(str(""+str(df['text'][i])+"").encode("ascii", "ignore"))
            token = sent_tokenize(data)
            u=''
            nu=''
            for tt in token:
                  translatedText = translator.translate(tt, dest="hi")
                  u+=translatedText.text+" "
                  nu+=translatedText.text+" "
                  u=transliterate(u, trans.ITRANS, trans.DEVANAGARI)
            all_text['Given'].append(data); all_text['HindiTranslated'].append(nu);all_text['HindiTransliterate'].append(u)
            t=TextBlob(u).translate(from_lang='hi',to='en')
            df['text'][i]=str(t)

        except:
            print(1)
            df['text'][i]=str(data)
            all_text['Given'].append(data); all_text['HindiTranslated'].append('');all_text['HindiTransliterate'].append('')

    #print(df)
    

    '''
    Text Conversion ends

    '''

    df=pd.DataFrame(df)
    #df['text'] = df.text.apply(lambda row: get_keywords(row))
    test=df.copy()


    for i in range(len(test)):
      test['text'][i]=str(test['text'][i])


    tokenizer = Tokenizer()
    full_text = list(test['text'].values)
    tokenizer.fit_on_texts(full_text)

    '''
    0-> Neutral
    1-> Positive
    2-> Negative
    '''

    X_test = tokenizer.texts_to_sequences(test['text'])
    X_test = sequence.pad_sequences(X_test, maxlen=85)
    tPredictions = model.predict(X_test)
    one=list(tPredictions)
    two = tPredictions.argmax(axis = 1)   
    #Print numpy array containing probabilities of all the classes
    
    K_.clear_session()

    # It return object with score of all the classes, output max score,textblob_score between (-1 to 1), profanity word list found through regex, converted english text, (Given Text, Translated Hindi Text, Transliterate Hindi Text) 
    # Refer Instruction file
    
    object= Result(one,two,chck,profanity_,list(test['text']),all_text)
    print('''    0-> Neutral
    1-> Positive
    2-> Negative''','\n')
    print("Converted Sentences", object.generatedText)
    print("Probabilities of all the classes",object.scoreList )

    #Take the max of probability
    print("ArgMax: ", object.score)
    print("TextBlob: ",object.textblob)
    print("Profanity List:",object.profanity)
    print("All Text", object.completeText)
    
    return object
                        
run()
