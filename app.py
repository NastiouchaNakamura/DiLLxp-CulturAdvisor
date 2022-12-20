from flask import Flask
from fetcher import culturecheznous, cataloguedonneesministereCulture
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    resources1 = culturecheznous.fetch()
    resources2 = cataloguedonneesministereCulture.fetch()

    for resource1 in resources1:
        print(resource1.fields)
    for resource2 in resources2:
        print(resource2.fields)

    return 'Hello World!'


if __name__ == '__main__':
    app.run()