import random, re, requests,time,os,hashlib
from hoshino import Service
from hoshino.typing import HoshinoBot, CQEvent,MessageSegment
sv = Service(name='Big-picture')
path=os.path.join(os.path.dirname(__file__), "img\\")
path2=path+"image2.png"
def getimg():#网络获取 然后下载到本地
     time.sleep(2)
     url='https://iw233.cn/API/Ghs.php'
     resp=requests.get(url)
     f = open(path2, mode="wb")
     f.write(resp.content)
     f.close()
     pass
#def getpath():#本地图片使用 有问题
     #files = os.listdir(image_path)
     #rec = random.choice(files)
     #print(image_path+"/"+rec)
     #return image_path+"/"+rec
def getdow(sss,image):
     img = requests.get(sss)
     f = open(image, mode="wb")
     f.write(img.content)
     f.close()
     pass
def getmd5(image):
     file = open(image, "rb")
     ff = file.read()
     m = hashlib.md5(ff)
     md5 = m.hexdigest()
     return md5
     pass
     
def getmsg(md5):
    msg = f'''<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID="5" templateID="1" action="" brief="" sourceMsgId="0" url="" flag="0" adverSign="0" multiMsgFlag="0"><item layout="0" advertiser_id="0" aid="0"><image uuid="'''+md5+'''" md5="'''+md5+'''" GroupFiledid="0" filesize="999999" local_path="{path}/*" minWidth="500" minHeight="500" maxWidth="300" maxHeight="500" /></item><source name="" icon="" action="" appid="-1" /></msg>'''
    return msg
@sv.on_rex('转换大图(.*)')
async def sendXML(bot: HoshinoBot, ev: CQEvent):
     image=path+"image.gif"#发送图片下载位置
     ret = re.match(r"\[CQ:image,file=(.*),url=(.*)\]", str(ev.message))
     ss=re.findall(r"url=(.+?)]",str(ev.message))[0]
     getdow(ss,image)
     md5=getmd5(image)
     msg=getmsg(md5)
     await bot.send(ev, f'[CQ:xml,data={msg}]')
     
@sv.on_rex('来点超级好看的')
async def sendXML2(bot: HoshinoBot, ev: CQEvent):
     getimg()
     md5=getmd5(path2)
     msg=getmsg(md5)
     img=f"[CQ:image,file=file:///" + path2+ "]"#先发送一个小图 制造缓存 防止大图无法显示
     await bot.send(ev, img)
     await bot.send(ev, f'[CQ:xml,data={msg}]')
