from flask import Flask
from fetcher import culturecheznous, cataloguedonneesministereCulture, listefestivalfrance, basilic
import pandas as pd
import numpy as np
import sqlite3
import csv
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    resources1 = culturecheznous.fetch()
    resources2 = cataloguedonneesministereCulture.fetch()
    resources3 = listefestivalfrance.fetch()
    resources4 = basilic.fetch()

    #for resource in resources4:
    #    print(resource.fields)

  

    res1 = []
    for resource1 in resources1:
        #print(resource1.fields)
        if resource1.fields not in res1: # supprimer les doublons
            res1.append(resource1.fields)
        
    res2 = []    
    for resource2 in resources2:
        #print(resource2.fields)
        if resource2.fields not in res2:
            res2.append(resource2.fields)

    res3 = []
    for resource3 in resources3:
        #print(resource1.fields)
        if resource3.fields not in res3: # supprimer les doublons
            res3.append(resource3.fields)
     
    res4 = []
    for resource4 in resources4:
        #print(resource1.fields)
        if resource4.fields not in res4: # supprimer les doublons
            res4.append(resource4.fields)

    # convertir en dataframe
    df1 = pd.DataFrame(res1) 
    print(df1)  
    df2 = pd.DataFrame(res2)
    print(df2)  
    df3 = pd.DataFrame(res3)
    print(df3) 
    df4 = pd.DataFrame(res4)
    print(df4) 


    # concatener les 2 BDD
    frames = [df1, df2, df3,df4]
    result = pd.concat(frames)
    print(result)

    # créer un fichier csv des données
    result.to_csv('culture.csv', sep ='\t') 

    return 'Hello World!'


if __name__ == '__main__':
    app.run()