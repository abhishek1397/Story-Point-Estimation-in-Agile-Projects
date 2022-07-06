import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from os import path
import uuid
from collections import Counter
import itertools
from sklearn.metrics import confusion_matrix
#from pandas_ml import ConfusionMatrix
import re
from nltk.corpus import stopwords
import nltk
from sklearn.metrics import precision_recall_fscore_support
import pickle
import warnings
warnings.filterwarnings("ignore")

class FastTextClassifier:
    
    folderName = ""
    trainFileName = ""
    testFileName = ""
    pretrainedModelName = ""
    outputModelName = ""
    outputFileName = ""
    logFolderName = ""
    
    
    def __init__(self):
        self.rand = str(uuid.uuid4())
        self.trainFileName = "issues_train_" + self.rand + ".txt"
        self.testFileName = "issues_test_" + self.rand + ".txt"
        self.pretrainedModelName = "pretrained_model" + ".vec"
        self.outputModelName = "supervised_classifier_model_" + self.rand
        self.outputFileName = "predicted_results_" + self.rand + ".txt"
        self.logFolderName = "logfiles_" + self.rand
        
        command = "mkdir " + self.logFolderName
        os.system(command)
        
    def re_log(self):
        return self.logFolderName
        
    def model_pretaining(self):
        root = '/PretrainData/'

        pretrain_files = ['apache_pretrain.csv', 
                  'jira_pretrain.csv', 
                  'spring_pretrain.csv', 
                  'talendforge_pretrain.csv', 
                  'moodle_pretrain.csv',
                  'appcelerator_pretrain.csv',
                  'duraspace_pretrain.csv',
                  'mulesoft_pretrain.csv',
                  'lsstcorp_pretrain.csv']

        pretrained = None

        for file in pretrain_files:
            f_pretrain = pd.read_csv(root + file, usecols=['issuekey', 'title', 'description'])
            if(pretrained is not None):
                pretrained = pd.concat([pretrained, df_pretrain])
            else:
                pretrained = df_pretrain

        pretrained = pretrained.dropna(how='any')
        
        with open('pretrained_df.pkl', "rb") as fh:
            pretrained = pickle.load(fh)
            
        outfile=open("issues_pretrain.txt", mode="w", encoding="utf-8")
        for line in pretrained.title_desc.values:
            outfile.write(line + '\n')
        outfile.close()
        
        command = "fasttext skipgram -input issues_pretrain.txt -output pretrained_model -epoch 100 -wordNgrams 4 -dim 300 -minn 4 -maxn 6 -lr 0.01"
        os.system(command)
        
        self.of=pretrain_outputfile+".vec"
        
        
    def fit(self, xtrain, ytrain):
        #log folder path
        trainFilePath = self.logFolderName + "/" +self.trainFileName
        outputModelPath = self.logFolderName + "/" +self.outputModelName
        
        outfile=open(trainFilePath, mode="w", encoding="utf-8")
        for i in range(len(xtrain)):
            #line = "__label__" + str(ytrain[i]) + " " + xtrain[i]
            line = xtrain[i]
            outfile.write(line + '\n')
        outfile.close()            
        
        #fit data to model and save it
        command = "fasttext supervised -input " + trainFilePath + " -output " + outputModelPath + " -epoch 500 -wordNgrams 4 -dim 300 -minn 4 -maxn 6 -pretrainedVectors " + self.pretrainedModelName
        os.system(command)
   
    def predict(self, xtest):
        #log folder path
        testFilePath = self.logFolderName + "/" +self.testFileName
        outputFilePath = self.logFolderName + "/" +self.outputFileName
        outputModelPath = self.logFolderName + "/" +self.outputModelName
        
        #save test file
        outfile=open(testFilePath, mode="w", encoding="utf-8")
        for i in range(len(xtest)):
            outfile.write(xtest[i] + '\n')
        outfile.close()
        
        #get predictions     
        command =  "fasttext predict " + outputModelPath + ".bin " + testFilePath + " > " + outputFilePath
        os.system(command)
        
        outfile=open(outputFilePath, mode="r")
        test_pred = [int(line.strip('_label\r\n')) for line in outfile.readlines()]
        outfile.close()
                
        return test_pred
        
    def predict_prob(self, xtest):
        #log folder path
        testFilePath = self.logFolderName + "/" +self.testFileName
        outputFilePath = self.logFolderName + "/" +self.outputFileName
        outputModelPath = self.logFolderName + "/" +self.outputModelName
        
        #save test file
        outfile=open(testFilePath, mode="w", encoding="utf-8")
        for i in range(len(xtest)):
            outfile.write(xtest[i] + '\n')
        outfile.close()
        
        #get predictions     
        command =  "fasttext predict-prob " + outputModelPath + ".bin " + testFilePath + " > " + outputFilePath
        os.system(command)
        
        outfile=open(outputFilePath, mode="r")
        test_pred = [(line.strip('_label\r\n')) for line in outfile.readlines()]
        outfile.close()
        
        y_pred=[]
        prob=[]
        length=len(test_pred)
        for i in range (length):
            split_val=test_pred[i].split()
            label1=int(split_val[0])
            y_pred.append(label1)
            prob1=float(split_val[1])
            prob.append(prob1)
        return y_pred,prob
        
        


def cleanData(text):
    #Remove all tags
    text = re.compile(r'<.*?>').sub('', text)
    #Remove web urls
    text = re.compile(r'http\S+').sub('', text)
    #Remove {html} tag
    text = text.replace('{html}', '')
    
    text_words = text.split()    
    
    resultwords  = [word for word in text_words if word not in stopwords.words('english')]
    
    if len(resultwords) > 0:
        result = ' '.join(resultwords)
    else:
        print('Empty transformation for: ' + text)
        
    return result
    
def formatFastTextClassifier(label):
    return "__label__" + str(label) + " "

def SimpleOverSample(_xtrain, _ytrain):
    xtrain = list(_xtrain)
    ytrain = list(_ytrain)

    samples_counter = Counter(ytrain)
    max_samples = sorted(samples_counter.values(), reverse=True)[0]
    for sc in samples_counter:
        init_samples = samples_counter[sc]
        samples_to_add = max_samples - init_samples
        if samples_to_add > 0:
            #collect indices to oversample for the current class
            index = list()
            for i in range(len(ytrain)):
                if(ytrain[i] == sc):
                    index.append(i)
            #select samples to copy for the current class    
            copy_from = [xtrain[i] for i in index]
            index_copy = 0
            for i in range(samples_to_add):
                xtrain.append(copy_from[index_copy % len(copy_from)])
                ytrain.append(sc)
                index_copy += 1
    return xtrain, ytrain
      
def rebuild_kfold_sets(folds, k, i):
    training_set = None
    testing_set = None

    for j in range(k):
        if(i==j):
            testing_set = folds[i]
        elif(training_set is not None):
            training_set = pd.concat([training_set, folds[j]])
        else:
            training_set = folds[j]
    
    return training_set, testing_set
    
    
def training_testing_fxn(value_k=2):

    # model pretraining 
    #model_pretaining()
    
    df = pd.read_csv("master_csv.csv")
    
    # Resetting the stroypoints 
    df.loc[df.storypoint <= 2, 'storypoint'] = 0 #small
    df.loc[(df.storypoint > 2) & (df.storypoint <= 5), 'storypoint'] = 1 #medium
    df.loc[df.storypoint > 5, 'storypoint'] = 2 #big
    
    
    # To combine title desc and storypoint for passing in fasttext algo
    df['title_desc'] = df['title'].str.lower() + ' - ' + df['description'].str.lower()
    df['label_title_desc'] = df['storypoint'].apply(lambda x: formatFastTextClassifier(x)) + df['title_desc'].apply(lambda x: cleanData(str(x)))
    print("phase1")
    
    # Reset the index
    df = df.reset_index(drop=True)
    
    # Make datafrane to save results
    results = pd.DataFrame(columns=['True_Classes', 'Predicted_Classes'])
    
    # Oversampling the dataset to improve the prediction
    df_oversampled = pd.DataFrame(df, columns=['label_title_desc','storypoint'])
    X_resampled, y_resampled =  SimpleOverSample(df_oversampled.label_title_desc.values.tolist(), df_oversampled.storypoint.values.tolist())
        
    k = value_k
    
    # Define the classes for the classifier
    classes = ['0','1','2']
    
    # Make Dataset random before start
    df_rand = df.sample(df.storypoint.count(), random_state=99)
    
    # Make datafrane to save results
    #results = pd.DataFrame(columns=['True_Classes', 'Predicted_Classes'])
    
    # Number of examples in each fold
    fsamples =  int(df_rand.storypoint.count() / k)
    
    # Fill folds (obs: last folder could contain less than fsamples datapoints)
    folds = list()
    for i in range(k):
        folds.append(df_rand.iloc[i * fsamples : (i + 1) * fsamples])
        
    # Init
    sum_overall_accuracy = 0
    total_predictions = 0
    log_folder_name=[]
    print("phase2")
    
    for i in range(k):
    
        #  Build new training and testing set for iteration i
        training_set, testing_set  = rebuild_kfold_sets(folds, k, i)
        y_true = testing_set.storypoint.tolist()
        
        print("phase 3 loop:",i)
        #  Oversample (ONLY TRAINING DATA)
        X_resampled, y_resampled =  SimpleOverSample(training_set.label_title_desc.values.tolist(), training_set.storypoint.values.tolist())
        
        # training 
        clf = FastTextClassifier()
        
        #if(i==0):
            #clf.model_pretaining()
            
        clf.fit(X_resampled, y_resampled)
        
        #  Predict
        #y_pred = clf.predict(testing_set.label_title_desc.values.tolist())
        y_pred,y_prob = clf.predict_prob(testing_set.label_title_desc.values.tolist())
        
        x=clf.re_log()
        log_folder_name.append(x)
        
        #  Update Overall Accuracy
        for num_pred in range(len(y_pred)):
            if(y_pred[num_pred] == y_true[num_pred]):
                sum_overall_accuracy += 1
            total_predictions += 1
            
        if (i==0):
            save_y_value(y_true,y_pred,y_prob)
        print("\n")
    
    

        # Plot Confusion Matrix and accuracy 
        #plot_confusion_matrix_with_accuracy(classes, y_true, y_pred, 'Confusion matrix (testing-set folder = ' + str(i) + ')', sum_overall_accuracy, total_predictions)
        
        # Save true and predicted labels in results dataframe
        results = results.append(pd.concat([pd.DataFrame({'True_Classes':y_true}), pd.DataFrame({'Predicted_Classes':y_pred})], axis=1)) 
        
    results.reset_index()
    
    with open('mosaic_results.pickle', 'wb') as f:
        pickle.dump(results, f)
    
    #del_log_file()
    
    #saving names of log files
    #print("ret_log_file:",log_folder_name)
    with open('log_file_name.pickle', 'wb') as f:
        pickle.dump(log_folder_name, f)
        
'''def ret_log_file(ret_log_file):
    print("ret_log_file:",ret_log_file)
    with open('log_file_name.pickle', 'wb') as f:
        pickle.dump(ret_log_file, f)'''
        
def del_log_file():
    with open('log_file_name.pickle', 'rb') as f:
        obj = pickle.load(f)
    x=obj[1:]
    
    for i in x:
        if(path.exists(i)):
            command = "rm -r " + i
            os.system(command)
    
        
def save_y_value(y_true,y_pred,y_prob):
    var=[y_true,y_pred,y_prob]
    #print("y_true:",y_true)
    with open('variable.pickle', 'wb') as f:
        pickle.dump(var, f)
       
def give_metrics_parameter():
        with open('variable.pickle', 'rb') as f:
            obj = pickle.load(f)
        
        y_true=obj[0]
        y_pred=obj[1]
        y_prob=obj[2]
        
        
        scores = precision_recall_fscore_support(y_true, y_pred)
        
        precision=scores[0]
        #print("precision:",precision)
        
        recall=scores[1]
        #print("recall:",recall)
        
        f_score=scores[2]
        #print("f_score:",f_score)
        
        return precision,recall,f_score,y_true,y_pred,y_prob

 


"""def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    
    #This function prints and plots the confusion matrix.
    #Normalization can be applied by setting `normalize=True`.
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]


    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
def plot_confusion_matrix_with_accuracy(classes, y_true, y_pred, title, sum_overall_accuracy, total_predictions):
    cm = ConfusionMatrix(y_true, y_pred)
    
    print('Current Overall accuracy: ' + str(cm.stats()['overall']['Accuracy']))
    if total_predictions != 0:
        print('Total Overall Accuracy: ' + str(sum_overall_accuracy/total_predictions))
    else:
        print('Total Overall Accuracy: ' + str(cm.stats()['overall']['Accuracy']))

    conf_matrix = confusion_matrix(y_true, y_pred)
    plt.figure()
    plot_confusion_matrix(conf_matrix, classes=classes, title=title)
    plt.show()""" 