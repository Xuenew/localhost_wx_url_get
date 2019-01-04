from flask import Flask
from spider_music_get import get_music_all_url
import json
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
@app.route("/index_hot_image")
def back_index_hot_image():
    """
    返回 hot image 滑动的图片list
    :return:
    """
    p=get_music_all_url()
    return json.dumps(p.get_hot_image())
    # return "HI"
@app.route("/get_song/<mid>",methods=['GET'])
def back_song_musicl(mid):
    mid = mid[4:]
    print(mid,"*******************",type(mid))
    # 测试用的 mid ：004AXFnZ33pU2z
    p=get_music_all_url()
    print(p.get_music_src(mid))
    return p.get_music_src(mid)
if __name__ == '__main__':
    app.run()
