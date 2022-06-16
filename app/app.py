import flask
from flask import render_template
import pickle
import sklearn
from sklearn.linear_model import LinearRegression

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST', 'GET'])

@app.route('/index', methods=['POST', 'GET'])
def get_params():
    if flask.request.method == 'GET':
        return render_template('main.html')

    if flask.request.method == 'POST':
        with open('lr_model.pkl', 'rb') as f:
            loaded_model = pickle.load(f)
        p_1 = float(flask.request.form['p_1'])
        p_2 = float(flask.request.form['p_2'])
        p_3 = float(flask.request.form['p_3'])
        p_4 = float(flask.request.form['p_4'])
        p_5 = float(flask.request.form['p_5'])
        p_6 = float(flask.request.form['p_6'])
        p_7 = float(flask.request.form['p_7'])
        p_8 = float(flask.request.form['p_8'])
        p_9 = float(flask.request.form['p_9'])
        p_10 = float(flask.request.form['p_10'])
        p_11 = float(flask.request.form['p_11'])
        y_pred = loaded_model.predict([[p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, p_11]])
       
        return render_template('main.html', result=y_pred)   

print('Hello')
if __name__ == '__main__':
    app.run()