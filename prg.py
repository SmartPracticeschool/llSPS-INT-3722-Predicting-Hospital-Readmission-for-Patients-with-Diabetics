from flask import Flask, request, render_template
from joblib import load
app = Flask(__name__)
model= load('multi.save')
trans=load('xtransform')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[x for x in request.form.values()]]
    print(x_test)
    test=trans.transform(x_test)
    print(test)
    prediction = model.predict(test)
    print(prediction)
    if prediction[0]==1:
        output='Yes'
    else:
        output='No'
    
    return render_template('new.html', prediction_text='Patient Readmittion: {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)

