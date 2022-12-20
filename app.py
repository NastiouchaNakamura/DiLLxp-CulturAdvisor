from flask import Flask
from fetcher import culturecheznous, cataloguedonneesministereCulture
import pandas as pd
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    resources1 = culturecheznous.fetch()
    resources2 = cataloguedonneesministereCulture.fetch()

    res1 = []
    for resource1 in resources1:
        print(resource1.fields)
        if resource1.fields not in res1: # supprimer les doublons
            res1.append(resource1.fields)
        
    res2 = []    
    for resource2 in resources2:
        print(resource2.fields)
        if resource2.fields not in res2:
            res2.append(resource2.fields)

    df1 = pd.DataFrame(res1) # convertir en dataframe
    print(df1)  
    df2 = pd.DataFrame(res2)
    print(df2)  

    frames = [df1, df2]
    result = pd.concat(frames)
    print(result)

    return 'Hello World!'


if __name__ == '__main__':
    app.run()