import flask, json, requests, os, pandas as pd
from flask import request, redirect, url_for, jsonify, render_template
from flask import redirect
from werkzeug.utils import secure_filename
from flask import Flask, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gagantalreja429824'
api_url = 'http://senti-mix-api.herokuapp.com/predict'

def generateHTML(output):
    inp = output['completeText']['Given']
    trans_inp = output['completeText']['HindiTranslated']
    translit_inp = output['completeText']['HindiTransliterate']
    senti = output['score']
    # txtblob = output['textblob']
    html = ''
    for i in range(len(senti)):
        html += '<tr>'
        html += f'<td>{inp[i]}</td>'
        html += f'<td>{trans_inp[i]}</td>'
        html += f'<td>{translit_inp[i]}</td>'
        if len(output['profanity'][f'{i}']) > 2:
            senti[i] = 2
        if senti[i]==0:
            html += f'<td class="neutral"><b>Neutral</b></td>'
        elif senti[i] == 1:
            html += f'<td class="positive"><b>Positive</b></td>'
        else:
            html += f'<td class="negative"><b>Negative</b></td>'
        html += '</tr>'
    return html

@app.route('/', methods = ['GET'])
@app.route('/input', methods = ['POST'])
def predictions_text():
    if request.method == 'POST':
        txt = request.form['text']
        value = 0
        json_inp = json.dumps({'input': [txt]})
        r = requests.post(api_url, data = json_inp, headers = {'Content-Type': 'application/json'})
        d = r.json()
        d = d['result'] 
        print(d)
        return render_template('index.html', html = generateHTML(d))
    return render_template('index.html', html = None)

@app.route('/file', methods = ['POST'])
def predictions_xlsx():
    if 'file' not in request.files:
        print('no file')
        flash('Error'.upper())
        return redirect('/')
    
    file = request.files['file']
    
    if file.filename == '':
        print('no selected')
        flash('No File Selected'.upper())
        return redirect('/')
    
    if file and '.xlsx' in file.filename:
        df = pd.read_excel(file)
        txt = df.tweet.tolist()
        json_dict = {'input': txt}
        r = requests.post(api_url, data = json.dumps(json_dict), headers = {'Content-Type': 'application/json'})
        d = r.json()
        d = d['result']
        print(d)
        return render_template('index.html', html = generateHTML(d))
    
    else:
        flash('Wrong File Format'.upper())
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

# ["rahul gandhi chor hai","Model ka output nhi ara randi ke bache","vipul jabardasti ka hua va baccha hai","ik gaand mein marunga sahi hojayega vipul"]
