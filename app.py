from flask import Flask,jsonify, render_template
import json

app = Flask(__name__)
jData = json.loads(open('./marvel.json').read())
data=jData["MarvelMovies"]

@app.route('/')
def marvel_main():
    return render_template("myadmin.html")

@app.route('/getmovies/')
def marvel_all():
    return jsonify(data)

@app.route('/getmovies/<string:Year>/')
def marvel(Year=''):
    myList=[]
    for element in data:
        if element["Year"] == Year:
            myList.append(element)
    return jsonify(myList)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
