#Author:xue yi yang
import pymysql,re,datetime
conn = pymysql.connect(host='39.108.15.78', port=3306, user='root', passwd='Xueyiyang', db='yang_ying_jie_dai', charset='utf8')
cur = conn.cursor()
# info = "1818810885"
# x = [0,]
# str(x)
# #print(re.findall(r'\[(.*)\]',str(x))[0],"*********")
# cur.execute(
# "select * from yong_hu_tb where ID in{}"
# )
forme_data = {'jk_name': 'xue', 'jk_money': '100', 'back_date': '2019-6-1', 'jk_reason': 'qian', 'zhai_zhu_phone': '112', 'jie_kuan_ren_id': 'll'}

#cur.execute("insert into yong_hu_jie_tiao_tb(zhai_zhu_ren_id,jie_kuan_ren_name,jie_kuan_jing_e,jie_kuan_ri_qi,gui_huan_ri_qi,jie_kuan_yuan_yin,shi_fou_que_ren,jie_kuan_ren_id) values(%s,%s,%s,%s,%s,%s,%s,%s,)"%(forme_data["zhai_zhu_phone"],forme_data["jk_name"],forme_data["jk_money"],"2019-8-9",forme_data["back_date"],forme_data["jk_reason"],"NO",forme_data["jie_kuan_ren_id"]))
#cur.execute("insert into yong_hu_jie_tiao_tb(zhai_zhu_ren_id) values({})".format(forme_data["zhai_zhu_phone"]))
# #print("insert into yong_hu_jie_tiao_tb(zhai_zhu_ren_id,jie_kuan_ren_name) values({})".format(forme_data["zhai_zhu_phone"]+","+forme_data["jk_name"]))
#cur.execute("insert into yong_hu_jie_tiao_tb(zhai_zhu_ren_id,jie_kuan_ren_name) values({})".format(forme_data["zhai_zhu_phone"]+","+"'"+forme_data["jk_name"]+"'"))
jk_ri_qi = datetime.date.today()
key_excut="insert into yong_hu_jie_tiao_tb(zhai_zhu_ren_id,jie_kuan_ren_name,jie_kuan_jing_e,jie_kuan_ri_qi,gui_huan_ri_qi,jie_kuan_yuan_yin,shi_fou_que_ren,jie_kuan_ren_id) values(%s,%s,%s,%s,%s,%s,%s,%s)" % (
        "'" + forme_data["zhai_zhu_phone"] + "'", "'" + forme_data["jk_name"] + "'", "'" + forme_data["jk_money"] + "'",
        "'" + str(jk_ri_qi) + "'", "'" + forme_data["back_date"] + "'", "'" + forme_data["jk_reason"] + "'",
        "'" + "NO" + "'", "'" + forme_data["jie_kuan_ren_id"] + "'",)
cur.execute(key_excut)
conn.commit()
#print(cur.fetchall())

cur.close()
conn.close()
# #print(datetime.date.today())
#
# data = {'jk_name': 'xue', 'jk_money': '100', 'back_date': '2019-6-1', 'jk_reason': 'wo yao qian', 'zhai_zhu_phone': 'undefined', 'jie_kuan_ren_id': ''}
# for k in data:
#     if data[k] :
#         #print(data[k],"8989778")
#         data[k]==""
# #print(data)