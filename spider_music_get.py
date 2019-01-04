# Author:xue yi yang
import requests
import json
# from lxml import etree
import lxml.html
class get_music_all_url():
    def __init__(self,music_name="",music_list_id=0):
        self.music_name = music_name
        self.music_list_id=music_list_id
        self.init_get_json()#获得 self.json_get 一个大大的字典
        # self.music_song_id=self.json_get["data"]["song"]["list"][self.music_list_id]["singer"][0]["mid"]
        self.music_song_id=self.json_get["data"]["song"]["list"][self.music_list_id]["mid"]#手机版的 song_id和歌词页一样
        self.music_mv_id=self.json_get["data"]["song"]["list"][self.music_list_id]["mv"]["vid"]
        self.music_lyrics_id=self.json_get["data"]["song"]["list"][self.music_list_id]["mid"]#歌词暂时先获取ID 在写函数

    # @classmethod
    def get_music_song(self,):
        cookies = {
        }
        header = {
            # "referer": "https://i.y.qq.com/v8/playsong.html?ADTAG=newyqq.song&songmid=003sYHuC3aBd4r"
            "user-agent": "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            # "upgrade-insecure-requests": "1",
            # "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            # "accept-encoding": "gzip, deflate, br",
            # "accept-language": "zh-CN,zh;q=0.9",
        }
        data = {
            # "ADTAG": "newyqq.song",
            # "songmid": "003sYHuC3aBd4r"
        }
        song_id = self.json_get["data"]["song"]["list"][self.music_list_id]["mid"]#对应的 歌曲id
        url = "https://i.y.qq.com/v8/playsong.html?ADTAG=newyqq.song&songmid={}#webchat_redirect".format(song_id)
        # ssrequest = requests.session()
        # requests.utils.add_dict_to_cookiejar(ssrequest.cookies)
        # respones = ssrequest.get(url=url,headers=header,data=data).text
        respones = requests.get(url=url, headers=header, data=data).text
        etree = lxml.html.etree
        selector = etree.HTML(respones)
        xx = selector.xpath("//audio[@id='h5audio_media']/@src")
        # xx=selector.xpath("//body")
        print(xx)
        # with open("ceshi.html","w") as f:
        #     f.write(respones)
        name=self.json_get["data"]["song"]["list"][self.music_list_id]["title"]
        author=self.json_get["data"]["song"]["list"][self.music_list_id]["singer"][0]["name"]
        poster= ""
        print({"src":xx,"name":name,"author":author,"poster":poster   })
        return json.dumps({"src":xx,"name":name,"author":author,"poster":poster,"list":self.json_get["data"]["song"]["list"] })

    def init_get_json(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
            # "user-agent": "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"

            , "Referer": "https://y.qq.com/",
        }
        url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=yqq.yqq.yqq&searchid=24984885683536913&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w={}&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0".format(self.music_name)
        respones = requests.get(url=url,headers=headers).content
        print(json.loads(respones)["data"]["song"]["list"][0]["singer"][0]["mid"])#歌曲mid
        print(json.loads(respones)["data"]["song"]["list"][0]["mv"]["vid"])#歌曲 mv mid
        print(json.loads(respones)["data"]["song"]["list"][0]["singer"][0]["name"])#歌曲作者
        print(json.loads(respones)["data"]["song"]["list"][0]["mid"])#歌曲歌词页mid
        print(json.loads(respones)["data"]["song"]["list"][0]["title"])#歌曲名字
        self.json_get = json.loads(respones)
        return self.json_get
#返回的是 搜索的结果列表 0-19
    def get_search_list(self):#返回一个列表 用于列出view 小程序的view
        return self.json_get["data"]["song"]["list"]
#返回的是 一个列表包含hot image [0]["picUrl"] 0-4
    def get_hot_image(self):
        url = "https://c.y.qq.com/musichall/fcgi-bin/fcg_yqqhomepagerecommend.fcg?g_tk=5381&uin=0&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&_=1546562309090"
        headers = {
            # "referer": "https://i.y.qq.com/v8/playsong.html?ADTAG=newyqq.song&songmid=003sYHuC3aBd4r"
            "user-agent": "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            # "upgrade-insecure-requests": "1",
            # "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            # "accept-encoding": "gzip, deflate, br",
            # "accept-language": "zh-CN,zh;q=0.9",
        }
        response = requests.get(headers=headers,url=url).text
        # response = requests.get(headers=headers,url=url).content
        # etree = lxml.html.etree
        # selector = etree.HTML(response)
        # xx = selector.xpath("//body")
        # with open("test.html","wb") as f:
        #     f.write(response)
        # print(json.loads(response)["data"]["slider"][0]["picUrl"])
        return json.loads(response)["data"]["slider"] #返回一个字典 loads 是加载json字符变成字典
if __name__ == '__main__':
    p=get_music_all_url(music_name="遥远的她")
    # p.get_music_song()
    p.get_hot_image()