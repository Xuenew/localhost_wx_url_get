
#-*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64

URL = "http://api.xfyun.cn/v1/service/v1/tts"
AUE = "raw"
APPID = "5c3eaa76"
API_KEY = "7d523f299b1cac17073b78bf5cc42b95"

def getHeader():
        curTime = str(int(time.time()))
        #ttp=ssml
        param = "{\"aue\":\""+AUE+"\",\"auf\":\"audio/L16;rate=16000\",\"voice_name\":\"xiaoyan\",\"engine_type\":\"intp65\",\"text_type\":\"text\"}"
        #print("param:{}".format(param))
        
        paramBase64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8')
        #print("x_param:{}".format(paramBase64))
        
        m2 = hashlib.md5()
        m2.update((API_KEY + curTime + paramBase64).encode('utf-8'))
        
        checkSum = m2.hexdigest()
        #print('checkSum:{}'.format(checkSum))
        
        header ={
                'X-CurTime':curTime,
                'X-Param':paramBase64,
                'X-Appid':APPID,
                'X-CheckSum':checkSum,
                'X-Real-Ip':'36.110.111.61',
                'Content-Type':'application/x-www-form-urlencoded; charset=utf-8',
        }
        #print(header)
        return header

def getBody(text):
        data = {'text':text}
        return data

def writeFile(file, content):
    with open(file, 'wb') as f:
        f.write(content)
    f.close()
r = requests.post(URL,headers=getHeader(),data=getBody("你好，清帆科技，我是感知计算组的一员，我叫薛忆阳。今年是2019年的一月十六号"))

contentType = r.headers['Content-Type']
#print("r.headers['Content-Type']")
if contentType == "audio/mpeg":
    sid = r.headers['sid']
    if AUE == "raw":
        #print(r.content)
        writeFile("audio/"+sid+".wav", r.content)
    else :
        #print(r.content)
        writeFile("audio/"+"xiaoyan"+".mp3", r.content)
    # test
    with open("audio/tes_wb.text","wb") as k:
        k.write(r.content)
    with open("audio/tes_ab.text","ab") as k:
        k.write(r.content)
    with open("audio/tes_ab.text","ab") as k:
        k.write(r.content)
    # with open("audio/tst1.wav","ab") as g:
    #     g.write(r.content)
    # with open("audio/tst1.wav", "ab") as g:
    #     g.write(r.content)
    #print ("success, sid = " + sid)
else :
    #print (r.text)