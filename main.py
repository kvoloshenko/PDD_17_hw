from flask import Flask, render_template, request
import hhru.all_data as ad
import sqlite.database_access as db

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
    # print(type(keywords_s), f'keywords_s={keywords_s}')
    #  запись разультатотв в БД
    connect_string = 'sqlite/hh_db.sqlite'
    result = ad.get_data(connect_string, keywords_s)
    # data = result[0]['requirements']
    # keywords = result[0]['keywords']
    # Замена на чтение из БД
    last_request_id = db.read_last_request_id(connect_string)
    print(type(last_request_id), f'last_request_id={last_request_id}')
    keywords = db.read_keywords(connect_string, last_request_id)
    print(type(keywords), f'keywords={keywords}')
    requirements = db.read_skills(connect_string, last_request_id)
    print(type(requirements), f'requirements={requirements}')

    # TODO
    # print (type(data),f'data={data}')
    # print(type(keywords),f'keywords={keywords}')


    return render_template('results.html', data=requirements, keywords = keywords)

if __name__ == "__main__":
    app.run(debug=True)