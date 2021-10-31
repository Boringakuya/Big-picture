import re, requests
import hashlib
from hoshino import Service
from hoshino.typing import HoshinoBot, CQEvent
sv = Service(name='zhuanhuan')
path="D:/jqr2/Leize_bot-master/hoshino/modules/zhuanhuan/img"
name =path+"/1.gif"
def getdow(sss):
     img = requests.get(sss)
     f = open(name, mode="wb")
     f.write(img.content)
     f.close()
     pass
def getmd5():
     file = open(name, "rb")
     ff = file.read()
     m = hashlib.md5(ff)
     md5 = m.hexdigest()
     return md5
     pass
    
@sv.on_rex('转换大图(.*)')
async def sendXML(bot: HoshinoBot, ev: CQEvent):
     ret = re.match(r"\[CQ:image,file=(.*),url=(.*)\]", str(ev.message))
     s =str(ev.message)
     ss=re.findall(r"url=(.+?)]",s)
     sss=ss[0]
     getdow(sss)
     md5=getmd5()
     msg = f'''<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID="5" templateID="1" action="" brief="" sourceMsgId="0" url="" flag="0" adverSign="0" multiMsgFlag="0"><item layout="0" advertiser_id="0" aid="0"><image uuid="'''+md5+'''" md5="'''+md5+'''" GroupFiledid="0" filesize="142857" local_path="{path}/*" minWidth="500" minHeight="500" maxWidth="300" maxHeight="500" /></item><source name="" icon="" action="" appid="-1" /></msg>'''
     await bot.send(ev, f'[CQ:xml,data={msg}]')
