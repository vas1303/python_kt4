from flask import Flask, render_template, request, escapefrom DBcm import UseDatabase
import mysql.connector
def search4letters(phrase: str, letters: str='aeiou') -> set:    return set(letters).intersection(set(phrase))
app=Flask(__name__)
@app.route('/')def hello()-> str:
     return 'Hello world from Flask'
@app.route('/viewlog')def view_the_log() -> 'html':
    contents = []    with open('vsearch.log') as log:
        for line in log:            contents.append([])
            for item in line.split('|'):                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')    return render_template('viewlog.html',
                           the_title='Viev Log',                           the_row_titles=titles,
                           the_data=contents,)
@app.route('/test')
def test_page()->'html':    return render_template('test.html', the_title="Welcom")
@app.route('/test-result', methods=['POST'])
def testPost()->'html':    your_name=request.form['your_name']
    return render_template('test-result.html', your_name=your_name)
app.config['dbconfig'] = {'host': '127.0.0.1',                            'user': 'vsearch',
                          'password': 'vsearchpasswd',                          'database': 'vsearchlogDB',}
def log request(req: 'flask request', res: str) -> None:
"""Log details of the web request and the results """        with UseDatabase(app.config['dbconfig']) as cursor:
                SQL = """insert into log                (phrase, letters, ip, browser string, results) 
                values (ts, ts, ts, ts, ts)"""                cursor.execute(SQL, (req.form['phrase'],
                                     req.form['letters']                                    req.remote_addr,
                                    req. user agent.browser,                                    res, ))
@app.route('/search4', methods=['POST'])
def do_search()->'html':    phrase = request.form['phrase']
    letters = request.form['letters']    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))    log_request(request, results)
    return render_template('results.html',                            the_phrase=phrase,
                            the_letters=letters,                            the_title=title,
                            the_results=results)


@app.route('/entry')def entry_page()->'html':
    return render_template('entry.html', the_title="Welcom")
app.run()
