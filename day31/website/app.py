from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/season/')
def season():
    season = "겨울"
    seasons = ["봄","여름","가을","겨울"]
    return render_template('season.html',
                           season=season, seasons=seasons) #키의 값

@app.route('/loop_index/', methods = ['GET'])
def loop_index():
    items = ['a','b','c','d']
    return render_template('loop_index.html', items=items)

app.run()
