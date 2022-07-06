import pandas as pd
import numpy as np
import os
import nltk
from nltk.corpus import stopwords
import fasttext
import warnings
warnings.filterwarnings("ignore")

model = fasttext.load_model("all_dataset\\logfiles_015af3c4-c801-4fdc-a0bf-cdf34b6aa694\\supervised_classifier_model_015af3c4-c801-4fdc-a0bf-cdf34b6aa694.bin")


def calsp(title,desc):
    title_desc= filter_df_single(title,desc)
    save_excel_single(title_desc)
    val = predict_sp(title_desc)
    return val
      
def filter_df_single(title,desc):
    htmltokens = ['{html}','<html>','<div>','<pre>','<p>', '</div>','</pre>','</p>']
    
    title=title.lower()
    desc=desc.lower()
    
    for w in htmltokens:
        title = title.replace(w, '')
    for w in htmltokens:
        desc = desc.replace(w, '') 
        
    title_words = title.split()
    desc_words = desc.split()    
    result_title  = [word for word in title_words if word not in stopwords.words('english')]
    result_desc  = [word for word in desc_words if word not in stopwords.words('english')]
    
    t1=''.join(result_title)
    d1=''.join(result_desc)
    
    title_desc = ( t1 + ' - ' + d1 )
    #df['label_title_desc'] = df['storypoint'].apply(lambda x: formatFastTextClassifier(x)) + df['title_desc'].apply(lambda x: cleanData(str(x)))
    #print(title_desc)
    return title_desc

'''def formatFastTextClassifier(label):
    return "__label__" + str(label) + " "'''
    
def save_excel_single(title_desc):
    head='title_desc'
    df=pd.DataFrame([title_desc],columns=[head])
    df.to_csv("Data_save.csv",index_label=head,mode='a',header=False,index=False)    
    
def predict_sp(title_desc):
    #model = fasttext.load_model("logfiles_78e5deaf-d348-473b-9809-0ec57a414131\\supervised_classifier_model_78e5deaf-d348-473b-9809-0ec57a414131.bin")
    if(len(title_desc)!=0):
        val=model.predict(title_desc)
        val1=val[0][0][-1]
        if(val1=="0"):
            val1=val1+"  "+"(Easy)"
        elif(val1=="1"):
            val1=val1+"  "+"(Medium)"
        else:
            val1=val1+" "+"(Complex)"
        return val1
    else:
        return "X"
    
    
def calsp_csv(path):
    df=pd.read_csv(path)
    if({'title', 'description'}.issubset(df.columns)):
        no_rows=df.shape[0]
        no_columns=df.shape[1]
        if(no_rows != 0 and no_columns==2):
            df1=filter_df_multi(df)
            save_excel_multiple(df1)
            predict_sp_multi(df1,df,path)
            return 1
            
        else:
            return 0
        
    else:
        return 0
    
def predict_sp_multi(df1,df2,path):
    head=['title','description','story_point']
    df=pd.DataFrame(columns=[head])
    df['title']=df2['title']
    df['description']=df2 ['description']
    df['story_point']=df1['title_desc'].apply(lambda x: predict_sp(str(x)))
    df.to_csv(path,index_label=head,header=True,index=False) 
    
    
def filter_df_multi(df):
    df['title_desc1'] = df['title'].str.lower() + ' - ' + df['description'].str.lower()
    df['title_desc'] =  df['title_desc1'].apply(lambda x: cleanData(str(x)))
    df.drop(['title_desc1'],axis=1)
    return df
        
        
def cleanData(text):
    #Define some known html tokens that appear in the data to be removed later
    htmltokens = ['{html}','<div>','<pre>','<p>', '</div>','</pre>','</p>']
    result = ''
    
    if(len(text)>1): 
        for w in htmltokens:
            text = text.replace(w, '')
    
        text_words = text.split()    
    
        resultwords  = [word for word in text_words if word not in stopwords.words('english')]
    
        if len(resultwords) > 0:
            result = ' '.join(resultwords)
        else:
            print('Empty transformation for: ' + text)
        
        return result
      
    else:
        return ""
    
    
def save_excel_multiple(df1):
    head=['title_desc']
    df=pd.DataFrame()
    df['title_desc']=df1['title_desc']
    df.to_csv("Data_save.csv",index_label=head,mode='a',header=False,index=False)