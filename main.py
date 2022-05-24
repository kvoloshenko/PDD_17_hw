from flask import Flask, render_template, request
import hhru.all_data as ad

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/form.html")
def form():
    return render_template('form.html')

@app.route("/results.html")
def results():
    return render_template('results.html')

@app.route("/contacts.html")
def contacts():
    developer_name = 'Konstantin Voloshenko'
    return render_template('contacts.html', name=developer_name, creation_date='24.05.2022')

@app.route('/results.html', methods=['POST'])
def run_post():
    # Как получть данные формы
    query_s = request.form['query_string']
    print(type(query_s),f'query={query_s}')
    where_s = request.form['where']
    print(type(where_s),f'query={where_s}')
    if where_s == 'all':
        keywords_s = f'{query_s}'
    elif where_s == 'company':
        keywords_s = f'COMPANY_NAME:({query_s})'
    elif where_s == 'name':
        keywords_s = f'NAME:({query_s})'
    print(type(keywords_s), f'keywords_s={keywords_s}')
    result = ad.get_data(keywords_s)
    data = result[0]['requirements']
    keywords = result[0]['keywords']
    return render_template('results.html', data=data, keywords = keywords)

if __name__ == "__main__":
    app.run(debug=True)