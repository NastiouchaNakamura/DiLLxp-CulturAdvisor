from flask import Flask
from fetcher import culturecheznous

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    resources = culturecheznous.fetch()

    for resource in resources:
        print(resource.fields)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
