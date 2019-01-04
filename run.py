from flask import Flask
from spider_music_get import get_music_all_url

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route("/search_music/<name>",methods=['GET'])
def back_song_list(name):
    """
    返回 输入音乐名字的搜索结果 默认 0-19 默认 播放链接是第一个
    :param name:
    :return:
    """
    name=name
    p=get_music_all_url(music_name=name)
    return p.get_music_song()
@app.route("/index_hot_image",methods=['GET'])
def back_index_hot_image():
    """
    返回 hot image 滑动的图片list
    :return:
    """
    p=get_music_all_url()
    return p.get_hot_image()
if __name__ == '__main__':
    app.run()
