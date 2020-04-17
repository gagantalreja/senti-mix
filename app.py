import flask, json, requests, os, pandas as pd
from flask import request, redirect, url_for, jsonify, render_template
from flask import redirect
from werkzeug.utils import secure_filename


from flask import Flask, flash, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gagantalreja429824'
api_url = 'http://api-senti-mix.herokuapp.com/sentiment'

@app.route('/', methods = ['GET'])
@app.route('/input', methods = ['POST'])
def predictions_text():
    if request.method == 'POST':
        txt = request.form['text']
        value = 0
        json_inp = json.dumps([{'text': txt, 'value': value}])
        r = requests.post(api_url, data = json_inp, headers = {'Content-Type': 'application/json'})
        print(r.status_code)
        d = r.json()
        d = d['result'] 
        send = dict()
        for i in range(len(d)):
            print(d)
            f = d[i]
            f['text'] = txt
            f['value'] = value
            send[i+1] = d[i]  
        return render_template('index.html', data = send)
    return render_template('index.html', data = None)

@app.route('/file', methods = ['POST'])
def predictions_xlsx():
    print(request.files)
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
        print('OK')
        #filename = secure_filename(file.filename)
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        df = pd.read_excel(file)
        print(df.head())
        txt = df.tweet.tolist()
        vals = df.value.tolist()
        json_dict = []
        print(txt, vals)
        for i in range(len(txt)):
            print(txt[i], vals[i])
            json_dict.append({'text': txt[i], 'value': vals[i]})
        r = requests.post(api_url, data = json.dumps(json_dict), headers = {'Content-Type': 'application/json'})
        print(r.status_code)
        d = r.json()
        d = d['result']
        send = dict()
        for i in range(len(d)):
            print(d)
            f = d[i]
            f['text'] = txt[i]
            f['value'] = vals[i]
            send[i+1] = d[i]
        return render_template('index.html', data = send)
    
    else:
        flash('Wrong File Format'.upper())
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
