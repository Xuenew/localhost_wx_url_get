from flask import Flask
from spider_music_get import get_music_all_url
from get_news_info import get_news
from get_listen_read import get_info_listen
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
    print(name,"***********************************")
    p=get_music_all_url(music_name=name[5:])
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
@app.route("/index_new_music_list")
def back_new_music_list():
    p=get_music_all_url()
    return p.get_mudic_new_song_list()
@app.route("/index_hot_key")
def back_hot_key():
    p=get_music_all_url()
    return p.get_hot_key()
@app.route("/music_read/<url>",methods=['GET',"POST"])
def music_read(url):
    print("right ")
    print(url)
    # url = url[4:]
    # xx=request.values.get("key")
    url_t =" https://view.inews.qq.com/w/"+url
    p = get_news(url=url_t)
    return json.dumps(p.get_main_con())
@app.route("/get_read_listen/<info>",methods=['GET',"POST"])
def get_read_listen(info):
    info = info[5:]
    print(info)
    p = get_info_listen(info)

    return p.get_listen()
if __name__ == '__main__':
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host='0.0.0.0',port=5000,debug=True)
    # app.run()