from flask import Flask,render_template,request
import pickle
import numpy as np

popular_df = pickle.load(open('populars.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
tourismid = pickle.load(open('tourismid.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_places',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    print(similar_items)
    # for i in similar_items:
        # print(pt.index[i[0]])
        # similar_items[0][0] = pt.index[i[0]]
    return render_template('recommend.html',similar_items=similar_items,locations=pt.index)


if __name__ == '__main__':
    app.run(debug=True)