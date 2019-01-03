from flask import Flask
from spider_music_get import get_music_all_url

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route("/search_music/<name>",methods=['GET'])
def back_song_list(name):
    name=name
    p=get_music_all_url(music_name=name)
    return p.get_music_song()


if __name__ == '__main__':
    app.run()
