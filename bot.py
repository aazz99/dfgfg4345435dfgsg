print("⚠️کاربران گرامی شما حق ویرایش یا ادیت سورس پایتون آرین بات را ندارید درصورت مشاهده آپدیت های سورس بنده دراختیار شما قرار نمی گیرد⚠️")


from requests import get
from re import findall
import os
import glob
from rubika.client import Bot
import requests
from rubika.tools import Tools
from rubika.encryption import encryption
from gtts import gTTS
from mutagen.mp3 import MP3
import json
from json import loads , dumps
import time
from time import sleep
import random
import urllib
import io
from random import choice,randint
from PIL import Image


#شناسه اکانت
bot = Bot("xfdlyerjogwiysbyolwdaljdzadaavin")
#......
#شناسه گروه
target = "g0CX4C50c1f13d1305474e7676936ad3"
#......
#شناسه کانال
channell = "c09SvA08d043b492e2276dc94ee08b86"

# Upgraded by arian abbasi(Upgrade by Arian)(Name Arian Bot)(libs for arian abbasi)
#آرین بات توسط بنده توسعه و ارتقا یافته است نامگذاری بات به اسم خود قابل قبول نیست در صورت مشاهده نسخه های بروز سورس بنده در اختیار شما قرار نمی گیرد و رفع باگ نیز نمی شوند


#شناسه کانال شما



GAP = bot.getGroupInfo(target)["data"]["group"]["group_title"]
p = Image.open('now.png')
bot.sendPhoto(target, 'now.png', p.size,caption=  f"اکانت هوشمند با موفقیت در گروه {GAP} فعال شد 😍🕺")



#آدرسدهی برای تغیر عکس گروه

#profile ="/storage/emulated/0/Download/arian.jpg"

def hasAds(msg):
	links = ["http://","https://",".ir",".com",".org",".net",".me"]
	for i in links:
		if i in msg:
			return True

def hasInsult(msg):
	swData = [False,None]
	for i in open("dontReadMe.txt").read().split("\n"):
		if i in msg:
			swData = [True, i]
			break
		else: continue
	return swData


# static variable
answered, sleeped, retries = [], False, {}
alerts, blacklist, stars, alert_stickers, alert_Gif = [] , [] , [] , [] , []



def alert(guid,user,link=False):
	alerts.append(guid)
	coun = int(alerts.count(guid))
	haslink = ""
	if link : haslink = "گزاشتن لینک در گروه ممنوع میباشد .\n\n"
	if coun == 1:
		bot.sendMessage(target, "💢 اخطار [ @"+user+" ] \n"+haslink+" شما [1/3] اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .", message_id=mesagidhoshdar)
	elif coun == 2:
		bot.sendMessage(target, "💢 اخطار [ @"+user+" ] \n"+haslink+" شما [2/3] اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .", message_id=mesagidhoshdar)
	elif coun == 3:
		blacklist.append(guid)
		bot.sendMessage(target, "🚫 کاربر [ @"+user+" ] \n [3/3] اخطار دریافت کرد ، بنابراین اکنون اخراج میشود .", message_id=mesagidhoshdar)
		bot.banGroupMember(target, guid)
		bot.sendMessage(msg.get("author_object_guid"),"متاسفانه شما بدلیل تبلیغات از گروه حذف شدید\nباید قوانین گروه را مطالعه می کردید❗️")


def alert_sticker(guid_sti,user_sti):
	alert_stickers.append(guid_sti)
	coun = int(alert_stickers.count(guid_sti))
	hasgif = "گذاشتن استیکر در گروه ممنوع می باشد\n\n"
	if coun == 1:
		bot.sendMessage(target, "💢 اخطار [ @"+user_sti+" ] \n"+hasgif+" شما [1/3] اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .")
	elif coun == 2:
		bot.sendMessage(target, "💢 اخطار [ @"+user_sti+" ] \n"+hasgif+" شما [2/3] اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .")
	elif coun == 3:
		blacklist.append(guid_sti)
		bot.sendMessage(target, "🚫 کاربر [ @"+user_sti+" ] \n [3/3] اخطار دریافت کرد ، بنابراین اکنون اخراج میشود .")
		bot.banGroupMember(target, guid_sti)
		bot.sendMessage(msg.get("author_object_guid"),"متاسفانه شما بدلیل ارسال استیکر از گروه حذف شدید\nباید قوانین گروه را مطالعه می کردید❗️")


def alert_GIF(guid_GFS,user_GFS):
	alert_Gif.append(guid_GFS)
	coun = int(alert_Gif.count(guid_GFS))
	has_gif = "گذاشتن گیف در گروه ممنوع می باشد\n\n"
	if coun == 1:
		bot.sendMessage(target, "💢 اخطار [ @"+user_GFS+" ] \n"+has_gif+" شما [1/3] اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .")
	elif coun == 2:
		bot.sendMessage(target, "💢 اخطار [ @"+user_GFS+" ] \n"+has_gif+" شما [2/3] اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .")
	elif coun == 3:
		blacklist.append(guid_GFS)
		bot.sendMessage(target, "🚫 کاربر [ @"+user_GFS+" ] \n [3/3] اخطار دریافت کرد ، بنابراین اکنون اخراج میشود .")
		bot.banGroupMember(target, guid_GFS)
		bot.sendMessage(msg.get("author_object_guid"),"متاسفانه شما بدلیل ارسال گیف از گروه حذف شدید\nباید قوانین گروه را مطالعه می کردید❗️")



def star(guid,user):
	stars.append(guid)
	star_count = int(stars.count(guid))
	if star_count == 1:
		bot.sendMessage(target,  f"شما {guil} از طرف مدیر گرامی [1/3] امتیاز دریافت کردید بعد از دریافت 3 امتیاز آدمین گروه می شوید 😍🙌", message_id=mesagid)
	elif star_count == 2:
		bot.sendMessage(target,  f"شما {guil} از طرف مدیر گرامی [2/3] امتیاز دریافت کردید بعد از دریافت 3 امتیاز آدمین گروه می شوید 😍🙌", message_id=mesagid)
	elif star_count == 3:
		bot.sendMessage(target,  f"شما {guil} از طرف مدیر گرامی [3/3] امتیاز دریافت کردید اکنون آدمین گروه می شوید 🎉😱", message_id=mesagid)
		bot.setGroupAdmin(target,guid)



def remove_star(guid,user):
	stars.remove(guid)
	remove_count = int(stars.count(guid))
	if remove_count == 2:
		bot.sendMessage(target,   f"از طرف مدیر گرامی [1/3] امتیاز از شما {guil} کسر شد بعد از کسر 3 امتیاز از آدمین بودن برکنار می شوید 😔💔", message_id=mesagid)
	elif remove_count == 1:
		bot.sendMessage(target,   f"از طرف مدیر گرامی [2/3] امتیاز از شما {guil} کسر شد بعد از کسر 3 امتیاز از آدمین بودن برکنار می شوید 😔💔", message_id=mesagid)
	elif remove_count == 0:
		bot.sendMessage(target,   f"از طرف مدیر گرامی [3/3] امتیاز از شما {guil} کسر شد اکنون از آدمینی برکنار می شوید 😭🖤", message_id=mesagid)
		bot.deleteGroupAdmin(target,user)


while True:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]

		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue
        
		for msg in messages:
			try:
				if msg["type"]=="Text" and not msg.get("message_id") in answered:
					if not sleeped:
						if hasAds(msg.get("text")) and not msg.get("author_object_guid") in admins :
							mesagidhoshdar = msg.get("message_id")
							guid = msg.get("author_object_guid")
							user = bot.getUserInfo(guid)["data"]["user"]["username"]
							alert(guid,user,True)
							bot.deleteMessages(target, [msg.get("message_id")])


						elif msg.get("text") == "ریستارت" or msg.get("text") == "\restart":
							try:
								if msg.get("author_object_guid") in admins:
								   sleeped = True
								   start_restart = "در حال راه اندازی مجدد....⏳"
								   my_id = bot.sendMessage(target,start_restart, message_id=msg.get("message_id"))
								   get_id = my_id["data"]["message_update"]
								   get__ID = get_id["message_id"]
								   sleep(2)
								   sleeped = False
								   finish_restart = "✅ متشکرم از همراهی شما ربات دوباره فعال شد"
								   bot.editMessage(target,finish_restart,get__ID)
								else:
									bot.sendMessage(target, '❌ اجازه دسترسی به شما داده نشد',message_id=msg.get("message_id"))
							except:
								print('error restart bot')

						elif msg.get("text") == "خاموش" or msg.get("text") == "\stop":
							try:
								if msg.get("author_object_guid") in admins:
								   sleeped = True
								   bot.sendMessage(target, "✅ ربات اکنون خاموش است", message_id=msg.get("message_id"))
								   bot.deleteChatHistory(target,msg.get("message_id"))
								else:
									bot.sendMessage(target, '❌ اجازه دسترسی به شما داده نشد',message_id=msg.get("message_id"))
							except:
								print('error off bot')

						elif msg.get("text").startswith("حذف") or msg.get("text").startswith("حذف پیام") and msg.get("author_object_guid") in admins :
							try:
								number = int(msg.get("text").split(" ")[1])
								answered.reverse()
								bot.deleteMessages(target, answered[0:number])

								bot.sendMessage(target, "✅ "+ str(number) +" پیام اخیر با موفقیت حذف شد", message_id=msg.get("message_id"))
								answered.reverse()

							except IndexError:
								bot.deleteMessages(target, [msg.get("reply_to_message_id")])
								bot.sendMessage(target, "✅ پیام با موفقیت حذف شد", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text").startswith("اخراج") or msg.get("text").startswith("بن") and msg.get("author_object_guid") in admins :
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
								if not guid in admins :
									bot.banGroupMember(target, guid)
									# bot.sendMessage(target, "✅ کاربر با موفقیت از گروه اخراج شد", message_id=msg.get("message_id"))
								else :
									bot.sendMessage(target, "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))

							except IndexError:
								getguidkr = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
								user = bot.getUserInfo(getguidkr)["data"]["chat"]["abs_object"]["object_guid"]
								username = bot.getUserInfo(user)["data"]["user"]["first_name"]
								bot.forwardMessages(target,[msg.get("reply_to_message_id")],getguidkr)
								if msg.get('reply_to_message_id') != None:
									befrest = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if befrest['text'] != None:
										getmtns = befrest['text']
								bot.sendMessage(getguidkr,  f"کاربر {username} شما به دلیل << {getmtns} >> از گروه حذف و وارد لیست سیاه شدید🗑")
							except:
								bot.sendMessage(target, "❌ دستور اشتباه", message_id=msg.get("message_id"))


						elif msg.get("text").startswith("آزاد") or msg.get("text").startswith("ازاد") and msg.get("author_object_guid") in admins :
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
								if not guid in admins :
									bot.unbanGroupMember(target, guid)
									linkgroupp = bot.getGroupLink(target)
									usernamep = bot.getUserInfo(guid)["data"]["user"]["first_name"]
									bot.sendMessage(target,   f"کاربر {usernamep} با موفقیت آزاد شد", message_id=msg.get("message_id"))
									bot.sendMessage(guid,   f"کاربر {usernamep} شما با موفقیت از لیست سیاه خارج شدید\nروی لینک کلیک کنید😍❤️👇\n\n {linkgroupp}")
								else:
									bot.sendMessage(target, "❌ شما آدمین نمی باشید", message_id=msg.get("message_id"))

							except IndexError:
								linkgroup = bot.getGroupLink(target)
								gydea = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								bot.unbanGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
								user = bot.getUserInfo(gydea)["data"]["chat"]["abs_object"]["object_guid"]
								username = bot.getUserInfo(user)["data"]["user"]["first_name"]
								bot.sendMessage(target,   f"کاربر {username} با موفقیت آزاد شد", message_id=msg.get("message_id"))
								bot.sendMessage(user,   f"کاربر {username} شما با موفقیت از لیست سیاه خارج شدید\nروی لینک کلیک کنید😍❤️👇\n\n {linkgroup}")
							except:
								bot.sendMessage(target, "❌ دستور اشتباه", message_id=msg.get("message_id"))




						elif msg.get("text").startswith("افزودن") or msg.get("text").startswith("!addgap") :
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]
								if guid in blacklist:
									if msg.get("author_object_guid") in admins:
										alerts.remove(guid)
										alerts.remove(guid)
										alerts.remove(guid)
										blacklist.remove(guid)

										bot.invite(target, [guid])
									else:
										bot.sendMessage(target, "❌ کاربر محدود میباشد", message_id=msg.get("message_id"))
								else:
									bot.invite(target, [guid])
									# bot.sendMessage(target, "✅ کاربر اکنون عضو گروه است", message_id=msg.get("message_id"))

							except IndexError:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ دستور اشتباه", message_id=msg.get("message_id"))


						elif msg.get("text").startswith("اضافه") or msg.get("text").startswith("!addch") :
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]
								if guid in blacklist:
									if msg.get("author_object_guid") in admins:
										blacklist.remove(guid)
										bot.inviteChannel(channell, [guid])
										bot.sendMessage(target, "✅ کاربر مورد نظر با موفقیت به کانال افزوده شد", message_id=msg.get("message_id"))
									else:
										bot.sendMessage(target, "❌ کاربر محدود میباشد", message_id=msg.get("message_id"))
								else:
									bot.inviteChannel(channell, [guid])
									bot.sendMessage(target, "✅ کاربر مورد نظر با موفقیت به کانال افزوده شد", message_id=msg.get("message_id"))

							except IndexError:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ دستور اشتباه", message_id=msg.get("message_id"))



						elif msg.get("text") == "دستورات":
							try:
								G_U = msg.get("author_object_guid")
								ID_karbar = bot.getUserInfo(G_U)["data"]["user"]["username"]
								NAME_karbar = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
								if ID_karbar != None:
									ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,ID_karbar)["data"]["in_chat_members"]]
								else:
									if NAME_karbar != None:
										ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,NAME_karbar)["data"]["in_chat_members"]]
									else:pass
								G_UN = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
								if msg.get("author_object_guid") in ozv_ajbar:
									rules = open("helps_arianbot/cc.txt","r",encoding='utf-8').read()
									bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
								else:
									bot.sendMessage(target,f" کاربر  {G_UN} شما متاسفانه عضو کانال ما نیستید برای اجرای این\nدستور ابتدا عضو کانال ما شوید: \n@TEXSBOT", message_id=msg.get("message_id"))
							except:
								try:
									G_U = msg.get("author_object_guid")
									ID_karbar = bot.getUserInfo(G_U)["data"]["user"]["username"]
									NAME_karbar = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
									if ID_karbar != None:
										ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,ID_karbar)["data"]["in_chat_members"]]
									else:
										if NAME_karbar != None:
											ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,NAME_karbar)["data"]["in_chat_members"]]
										else:pass
									G_UN = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
									if msg.get("author_object_guid") in ozv_ajbar:
										rules = open("helps_arianbot/cc.txt","r",encoding='utf-8').read()
										bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
									else:
										bot.sendMessage(target,f" کاربر  {G_UN} شما متاسفانه عضو کانال ما نیستید برای اجرای این\nدستور ابتدا عضو کانال ما شوید: \n@TEXSBOT", message_id=msg.get("message_id"))
								except:
									print("err dastorat")

						elif msg.get("text") == "سرگرمی":
							try:
								rules = open("plays_arianbot/poer.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
								bot.pin(target, message_id=msg.get("message_id"))
								bot.sendMessage(target, "سوالات فرستاده شدند حالا بازی کنید😉☝️", message_id=msg.get("message_id"))
							except:
								print("err play")

						elif msg["text"].startswith("!number") or msg["text"].startswith("بشمار"):
							try:
								response = get(f"http://api.codebazan.ir/adad/?text={msg['text'].split()[1]}").json()
								bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:20])).text
								bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "متاسفانه نتیجه‌ای موجود نبود!", message_id=msg["message_id"])

						elif msg.get("text").startswith("زمان"):
							try:
								response = get("https://api.codebazan.ir/time-date/?td=all").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err answer time")

						elif msg.get("text") == "ساعت":
							try:
								bot.sendMessage(target, f"Time : {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}", message_id=msg.get("message_id"))
							except:
								print("err time answer")

						elif msg.get("text") == "!date":
							try:
								bot.sendMessage(target, f"Date: {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}", message_id=msg.get("message_id"))
							except:
								print("err date")

						elif msg.get("text") == "پاک" and msg.get("author_object_guid") in admins :
							try:
								bot.deleteMessages(target, [msg.get("reply_to_message_id")])
								bot.sendMessage(target, "پیام مورد نظر پاک شد...", message_id=msg.get("message_id"))
							except:
								print("err pak")

						elif msg.get("text").startswith("دانستنی عکس"):
								try:
									danestane = get("http://api.codebazan.ir/danestani/pic")
									with open("shot.jpg","wb") as shot:
										shot.write(danestane.content)
										p = Image.open('shot.jpg')
										bot.sendPhoto(target, "shot.jpg",p.size, caption="🤖آرین بات🤖", message_id=msg["message_id"])
										os.remove('screenshot.jpg')
								except:
									print("err  photo danestane")

						elif msg.get("text").startswith("اسکرین"):
								try:
									screenshot = get(f"http://api.codebazan.ir/webshot/?text=1000&domain={msg.get('text').split()[1]}")
									with open("screenshot.jpg","wb") as screen:
										screen.write(screenshot.content)
										p = Image.open('screenshot.jpg')
										bot.sendPhoto(target, "screenshot.jpg",p.size, caption="🤖آرین بات🤖", message_id=msg["message_id"])
										print("sended danestane")
										screen.close()
										os.remove('screenshot.jpg')
								except:
									print("err screenshot")



						elif msg.get("text").startswith("شات") or msg.get("text").startswith("!shot") or msg.get("text").startswith("shot"):
						            if msg.get('reply_to_message_id') != None:
							            msg_reply_info = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
							            if msg_reply_info['text'] != None:
								            text = msg_reply_info['text']
								            res = get('https://api.otherapi.tk/carbon?type=create&code=' + text + '&theme=vscode')
								            if res.status_code == 400 and res.content != b'':
									            b2 = res.content
									            print('get the image')
									            f = open('image.jpg','wb')
									            f.write(b2)
									            f.close()
									            p = Image.open('image.jpg')
									            bot.sendPhoto(target, 'image.jpg', p.size,message_id=msg["message_id"])
								            else:
									            bot.sendMessage(target, 'ارتباط با سرور ناموفق',message_id=msg["message_id"])
							            else:
								            bot.sendMessage(target, 'پیام شما متن یا کپشن ندارد',message_id=msg["message_id"])
						            else:
							            bot.sendMessage(target, 'لطفا روی یک پیام ریپلای بزنید',message_id=msg["message_id"])


						elif msg.get("text").startswith("!cal") or msg.get("text").startswith("حساب"):
							msd = msg.get("text")
							if plus == True:
								try:
									call = [msd.split(" ")[1], msd.split(" ")[2], msd.split(" ")[3]]
									if call[1] == "+":
										try:
											am = float(call[0]) + float(call[2])
											bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
											plus = False
										except:
											print("err answer +")

									elif call[1] == "-":
										try:
											am = float(call[0]) - float(call[2])
											bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
										except:
											print("err answer -")

									elif call[1] == "*":
										try:
											am = float(call[0]) * float(call[2])
											bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
										except:
											print("err answer *")

									elif call[1] == "/":
										try:
											am = float(call[0]) / float(call[2])
											bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
										except:
											print("err answer /")

								except IndexError:
									bot.sendMessage(target, "متاسفانه دستور شما اشتباه میباشد!" ,message_id=msg.get("message_id"))
									plus= True

						elif hasInsult(msg.get("text"))[0] and not msg.get("author_object_guid") in admins :
							try:
								print("yek ahmagh fohsh dad")
								bot.deleteMessages(target, [str(msg.get("message_id"))])
								print("fohsh pak shod")
							except:
								print("err del fohsh Bug")

						elif hasAds(msg.get("text")) and not msg.get("author_object_guid") in admins :
							try:
								mesagidhoshdar = msg.get("message_id")
								guid = msg.get("author_object_guid")
								user = bot.getUserInfo(guid)["data"]["user"]["username"]
								alert(guid,user,True)
								bot.deleteMessages(target, [msg.get("message_id")])
							except:
								print("err deletelinks_komake")

						elif msg.get("text").startswith("صلم") or msg.get("text").startswith("سلم") or msg.get("text").startswith("صلام") or msg.get("text").startswith("سلام") or msg.get("text").startswith("سیلام") or msg.get("text").startswith("صیلام") or msg.get("text").startswith("شلام") or msg.get("text").startswith("های") or msg.get("text").startswith("هلو"):
							try:
								bot.sendVoice(target,"pooldar/5.ogg",3000, message_id=msg.get("message_id"))
							except:
								try:
									guidr= msg.get("author_object_guid")
									textw = bot.getUserInfo(guidr)["data"]["user"]["first_name"]
									taf = ["آقا 😍 🌈","عشقم 🌚🌺","خان 🤓💋","جووووون🤩🍓","خشگلم🌛🍁","عسل بابا👳‍♂🙋‍♂","نفسکم🙇‍♀💖"," 🌷عزیزم",]
									ren= choice(taf)
									p = Image.open('hello.jpg')
									bot.sendPhoto(target, 'hello.jpg', p.size,caption=  f"علیک {textw} {ren}", message_id=msg.get("message_id"))
								except:
									print("err hello")

						elif msg.get("text").startswith("چه صدایی داری") or msg.get("text").startswith("خبی"):
							try:
								bot.sendVoice(target,"pooldar/23.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err answer hay")

						elif msg.get("text").startswith("gham"):
							try:
								bot.sendSticker(target)
							except:
								print("err answer hay")


						elif msg.get("text").startswith("شات") or msg.get("text").startswith("!shot") or msg.get("text").startswith("shot"):
						            if msg.get('reply_to_message_id') != None:
							            msg_reply_info = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
							            if msg_reply_info['text'] != None:
								            text = msg_reply_info['text']
								            res = get('https://api.otherapi.tk/carbon?type=create&code=' + text + '&theme=vscode')
								            if res.status_code == 200 and res.content != b'':
									            b2 = res.content
									            print('get the image')
									            f = open('image.jpg','wb')
									            f.write(b2)
									            f.close()
									            p = Image.open('image.jpg')
									            bot.sendPhoto(target, 'image.jpg', p.size,message_id=msg["message_id"])
								            else:
									            bot.sendMessage(target, 'ارتباط با سرور ناموفق',message_id=msg["message_id"])
							            else:
								            bot.sendMessage(target, 'پیام شما متن یا کپشن ندارد',message_id=msg["message_id"])
						            else:
							            bot.sendMessage(target, 'لطفا روی یک پیام ریپلای بزنید',message_id=msg["message_id"])


						elif msg.get("text").startswith("ایجاد کال"):
							try:
								bot.startVoiceChat(target)
								bot.sendMessage(target, "✅ با موفقیت ایجاد شد", message_id=msg.get("message_id"))
							except:
								print("err call voice")

						elif msg.get("text").startswith("قطع کال"):
							try:
								GAP = bot.getGroupInfo(target)["data"]["chat"]
								VOICE_CHAT = GAP["group_voice_chat_id"]
								bot.finishVoiceChat(target,VOICE_CHAT)
								bot.sendMessage(target, "✅ با موفقیت قطع شد", message_id=msg.get("message_id"))
							except:
								print("err call voice")

						elif msg.get("text").startswith("چرا ناراحتی"):
							try:
								bot.sendMessage(target, "به خاطر مامانم", message_id=msg.get("message_id"))
							except:
								print("err send_massage_be_id")

						elif msg.get("text").startswith("باهات حال نمیکنم") or msg.get("text").startswith("حال نمیکنم"):
							try:
								bot.sendVoice(target,"pooldar/25.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err CheKhabar")

						elif msg.get("text") == "اسکی" or msg.get("text").startswith("اصکی"):
							try:
								bot.sendVoice(target,"pooldar/67.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("error ersal start1")

						elif msg.get("text").startswith("بیا بازی") or msg.get("text").startswith("بازی کنیم"):
							try:
								bot.sendMessage(target,  "ِمن میرم پلاتو بازی کنم تو هم اگه دوست داری بزن بیوگرافیم بریم بازی کنیم قبلش یادت نره حتما بازی رو از گوگل پلی دانلود کنی")
							except:
								print("error sabt_link-tabligh")

						elif msg.get("text").startswith("یکتا اجی") or msg.get("text").startswith("یکتا"):
							try:
								bot.sendMessage(target, "جونم بگو", message_id=msg.get("message_id"))
							except:
								print("err save tabligh")

						elif msg.get("text").startswith("تبلیغ کن"):
							while True:
								sleep(5)
								matntabb = list(matntabligz)
								randomli = choice(matntabb)
								writelin = open("tabligh_arianbot/target.txt","w",encoding='utf-8').write(str(randomli))
								tabyligh = open("tabligh_arianbot/matnTABLIGH.txt","r",encoding='utf-8').read()
								tabgligh = open("tabligh_arianbot/target.txt","r",encoding='utf-8').read()
								tabeligh = bot.joinGroup(tabgligh)
								tabrligh = tabeligh['data']['group']['group_guid']
								bot.sendMessage(tabrligh,tabyligh)
								bot.leaveGroup(tabrligh)

						elif msg.get("text").startswith("ربات") or msg.get("text").startswith("بات") or msg.get("text").startswith("رباط") or msg.get("text").startswith("باط"):
							try:
								rew = ["⛑️\n😁\n👔🌻\n👖🖱 \n در خدمتم","🧢\n😆\n🥋🌷\n👖🖱\nجان ربات 😁","👒\n😍\n🧥🌼\n👖 \n جون ربات گفتن 😍","🎩\n😎\n🥋💐\n👖\n⚽️\n جان کاری داشتید","🎓\n🙂\n🧥\n👖\n⚽️ \nجونم ربات بفرمایید 😍","🪖\n🤓\n👔\n👖\nجونم بفرمایید 🤩","⛑️\n😁\n👔🌻\n👖🖱 \n امری داری آدمین من","⛑️\n🙄\n👔🌻\n👖🖱 \n هاچیه","⛑️\n😌\n👔🌻\n👖🖱 \n چیه عشقم؟","⛑️\n🤒\n👔🌻\n👖🖱 \n صدام کردی عمر من؟","⛑️\n😯\n👔🌻\n👖🖱 \n به به وجودم صدام کرده",]
								renn= choice(rew)
								bot.sendDocument(target,"ARIANBOT.mp4", caption= f"{renn}", message_id=msg.get("message_id"))
							except:
								try:
									rew = ["⛑️\n😁\n👔🌻\n👖🖱 \n در خدمتم","🧢\n😆\n🥋🌷\n👖🖱\nجان ربات 😁","👒\n😍\n🧥🌼\n👖 \n جون ربات گفتن 😍","🎩\n😎\n🥋💐\n👖\n⚽️\n جان کاری داشتید","🎓\n🙂\n🧥\n👖\n⚽️ \nجونم ربات بفرمایید 😍","🪖\n🤓\n👔\n👖\nجونم بفرمایید 🤩","⛑️\n😁\n👔🌻\n👖🖱 \n امری داری آدمین من","⛑️\n🙄\n👔🌻\n👖🖱 \n هاچیه","⛑️\n😌\n👔🌻\n👖🖱 \n چیه عشقم؟","⛑️\n🤒\n👔🌻\n👖🖱 \n صدام کردی عمر من؟","⛑️\n😯\n👔🌻\n👖🖱 \n به به وجودم صدام کرده",]
									renn= choice(rew)
									bot.sendDocument(target,"ARIANBOT.mp4", caption= f"{renn}", message_id=msg.get("message_id"))
								except:
									print("error robot")


						elif msg.get("text").startswith("مثل دخترا") or msg.get("text").startswith("مثل دخی ها"):
							try:
								bot.sendVoice(target,"pooldar/26.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err father")

						elif msg.get("text").startswith("امتیاز"):
							try:
								mesagid = msg.get("message_id")
								user = msg.get("text").split(" ")[1][1:]
								guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]
								guil = bot.getInfoByUsername(user)["data"]["user"]["first_name"]
								star(guid,user)
							except:
								try:
									mesagid = msg.get("reply_to_message_id")
									guid = bot.getMessagesInfo(target, [msg["reply_to_message_id"]])[0]["author_object_guid"]
									user = bot.getUserInfo(guid)["data"]["chat"]["abs_object"]["object_guid"]
									guil = bot.getUserInfo(guid)["data"]["user"]["first_name"]
									star(guid,user)
								except:
									bot.sendMessage(target, "خطا در امتیازدهی❌", message_id=msg.get("message_id"))


						elif msg.get("text").startswith("کسر امتیاز"):
							try:
								mesagid = msg.get("message_id")
								user = msg.get("text").split(" ")[2][2:]
								guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]
								guil = bot.getInfoByUsername(user)["data"]["user"]["first_name"]
								remove_star(guid,user)
							except:
								try:
									mesagid = msg.get("reply_to_message_id")
									guid = bot.getMessagesInfo(target, [msg["reply_to_message_id"]])[0]["author_object_guid"]
									user = bot.getUserInfo(guid)["data"]["chat"]["abs_object"]["object_guid"]
									guil = bot.getUserInfo(guid)["data"]["user"]["first_name"]
									remove_star(guid,user)
								except:
									bot.sendMessage(target, " خطا در کسر امتیازدهی❌", message_id=msg.get("message_id"))


						elif msg.get("text").startswith("تعداد امتیاز"):
							try:
								getusername = msg.get("text").split(" ")[1][1:]
								getguid = bot.getInfoByUsername(getusername)["data"]["chat"]["abs_object"]["object_guid"]
								getyourname = bot.getInfoByUsername(getguid)["data"]["user"]["first_name"]
								numberstar = int(stars.count(getguid))
								bot.sendMessage(target,   f"مقدار امتیاز کاربر {getyourname} است به [{numberstar}] امتیاز مبارکش باشه😅💋", message_id=msg.get("message_id"))
							except:
								try:
									getusername = bot.getMessagesInfo(target, [msg["reply_to_message_id"]])[0]["author_object_guid"]
									getguid = bot.getUserInfo(getusername)["data"]["chat"]["abs_object"]["object_guid"]
									getyourname = bot.getUserInfo(getguid)["data"]["user"]["first_name"]
									numberstar = int(stars.count(getguid))
									bot.sendMessage(target,   f"مقدار امتیاز کاربر {getyourname} است به [{numberstar}] امتیاز مبارکش باشه😅💋", message_id=msg.get("message_id"))
								except:
									bot.sendMessage(target, " خطا در بررسی امتیاز های کاربر مورد نظر ئد❌", message_id=msg.get("message_id"))


						elif msg.get("text").startswith("این رباته") or msg.get("text").startswith("رباطی؟") or msg.get("text").startswith("رباطی") or msg.get("text").startswith("رباتی؟") or msg.get("text").startswith("ربات هستی؟") or msg.get("text").startswith("باتی") or msg.get("text").startswith("باتی؟"):
							try:
								bot.sendVoice(target,"pooldar/29.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err asl")


						elif msg.get("text").startswith("بپرس"):
							try:
								file = open("plays_arianbot/bepors.txt").read().split("\n")
								read = list(file)
								bot.sendMessage(target,choice(read), message_id=msg.get("message_id"))
							except:
								print("err bepors")


						elif msg.get("text").startswith("دارم قلیون میکشم") or msg.get("text").startswith("یکتا دارم قلیون میکشم") or msg.get("text").startswith("یکتا قلیون نمیکشی؟"):
							try:
								bot.sendVoice(target,"pooldar/27.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err bose")

						elif msg.get("text") == "!speak" or msg.get("text") == "speak" or msg.get("text") == "Speak" or msg.get("text") == "صوت":
							try:
								if msg.get('reply_to_message_id') != None:
									msg_reply_info = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if msg_reply_info['text'] != None:
										text = msg_reply_info['text']
										speech = gTTS(text)
										changed_voice = io.BytesIO()
										speech.write_to_fp(changed_voice)
										b2 = changed_voice.getvalue()
										changed_voice.seek(0)
										audio = MP3(changed_voice)
										dur = audio.info.length
										dur = dur * 1000
										f = open('sound.ogg','wb')
										f.write(b2)
										f.close()
										bot.sendVoice(target , 'sound.ogg', dur,message_id=msg["message_id"])
										os.remove('sound.ogg')
										print('sended voice')
								else:
									bot.sendMessage(target, 'رو پیام انگلیسی که نوشتید ریپ بزنید❌',message_id=msg["message_id"])
							except:
								print('server gtts bug')

						elif msg.get("text").startswith("حرومزاده") or msg.get("text").startswith("حرومی") :
							try:
								bot.sendVoice(target,"pooldar/31.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err moharefe")

						elif msg.get("text").startswith("مردم از خنده"):
							try:
								bot.sendVoice(target,"pooldar/32.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("error ersal start1")

						elif msg.get("text").startswith("دوست دارم"):
							try:
								bot.sendMessage(target,  "منم خیلی دوست دارم عزیزم")
							except:
								print("error sabt_link-sinzan")

						elif msg.get("text").startswith("سین بزن"):
							while True:
								sleep(5)
								matntabb = list(matnsingz)
								randomli = choice(matntabb)
								writelin = open("sinzan_arianbot/TARGET_SINZAN.txt","w",encoding='utf-8').write(str(randomli))
								tabgligh = open("sinzan_arianbot/TARGET_SINZAN.txt","r",encoding='utf-8').read()
								tabeligh = bot.joinGroup(tabgligh)
								tabrligh = tabeligh['data']['group']['group_guid']
								bot.forwardMessages(target,[msg.get("reply_to_message_id")],tabrligh)
								bot.leaveGroup(tabrligh)


						elif msg.get("text") == "نمیدونم":
							try:
								bot.sendMessage(target,  "پس تو چی میدونی؟")
							except:
								print('hiper karbar')

						elif msg.get("text").startswith("!Mono") or msg.get("text").startswith("مونو"):
							try:
								bot.sendMessage(target,textMono, metadata=[{"from_index": 0,"length": len(metn),"type":"Mono"}], message_id=msg.get("message_id"))
							except:
								print("err Mono font")

						elif msg.get("text").startswith("منگولی") or msg.get("text").startswith("جنده") or msg.get("text").startswith("کونی")  or msg.get("text").startswith("نوب")  or msg.get("text").startswith("کثیف") and msg.get("author_object_guid") in admins:
							try:
								bot.sendVoice(target,"pooldar/33.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err on Unmute")


						elif msg.get("text").startswith("visit") or msg.get("text").startswith("پیام اشکار") and msg.get("author_object_guid") in admins:
							try:
								bot.chatGroupvisit(target,["chat_history_for_new_members"])
								bot.sendMessage(target, "پیام های گروه با موفقیت اشکار شدند ✅", message_id=msg.get("message_id"))
							except:
								print("err visit msg")

						elif msg.get("text").startswith("اصل بدین") or msg.get("text").startswith("همه اصل") and msg.get("author_object_guid") in admins:
							try:
								bot.sendMessage(target, "اصل بدین", message_id=msg.get("message_id"))
							except:
								print("err hidden msg")

						elif msg.get("text").startswith("خوبم") or msg.get("text").startswith("خبم") and msg.get("author_object_guid") in admins:
							try:
								bot.sendMessage(target, "ایشاالاه همیشه سلامت باشی", message_id=msg.get("message_id"))
							except:
								print("err off Mute")

						elif msg.get("text").startswith("صیک") and msg.get("author_object_guid") in admins:
							try:
								bot.sendMessage(target, "احمق اصلا میدونی صیک یعنی چی؟😅 \n صیک یه واژه انگلیسی که به معنی مریض هست بعد افتاده سر زبون یه سری لمر و جوجه شاخ مثل تو فرزندم برو مشقامو بنویس👋", message_id=msg.get("message_id"))
							except:
								print("err join Channel")

						elif msg.get("text").startswith("خودتو معرفی کن") or msg.get("text").startswith("معرفی کن") and msg.get("author_object_guid") in admins:
							try:
								bot.sendMessage(target, "حوصله ندارم خودت از شاهرخ بپرس کامل بهت میگه", message_id=msg.get("message_id"))
							except:
								print("err lock Sticker")

						elif msg.get("text").startswith("رل میخوام") and msg.get("author_object_guid") in admins:
							try:
								bot.sendMessage(target, "منم ی کیف پر از پول میخوام😇دلار باشه بهتره.", message_id=msg.get("message_id"))
							except:
								print("err unlock Sticker")


						elif msg.get("text").startswith("بحی") and msg.get("author_object_guid") in admins:
							try:
								bot.sendMessage(target, "نرو سمیع😞💔", message_id=msg.get("message_id"))
							except:
								print("err lock Gif")

						elif msg.get("text").startswith("شاهرخ") or msg.get("text").startswith("ابوالفضل") or msg.get("text").startswith("@TEXCODER") and msg.get("author_object_guid") in admins:
							try:
								lock_GIF = False
								bot.sendMessage(target, "این سازنده منه😻این بابای منه🙀قربونش بشید😌", message_id=msg.get("message_id"))
							except:
								print("err unlock Gif")

						elif msg.get("text").startswith("رباتو دوست دارم") or msg.get("text").startswith("رباطو دوست دارم"):
							try:
								bot.sendVoice(target,"pooldar/34.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err answer ghobe")

						elif msg.get("text").startswith("اهنگ بخون"):
							try:
								bot.sendVoice(target,"pooldar/35.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err moharefe")

						elif msg.get("text").startswith("داشتم میخوندم") or msg.get("text").startswith("میخواستم بخونم"):
							try:
								bot.sendVoice(target,"pooldar/36.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err roz")

						elif msg.get("text").startswith("بای") and msg.get("text").startswith("خداحافظ") and msg.get("author_object_guid") in admins:
							try:
								bot.sendVoice(target,"pooldar/37.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err sendPoll")

						elif msg.get("text").startswith("تست"):
							try:
								matn_r = ["hello","arianbot","robot"]
								galb = ["💜","💙","💚"]
								my_id = bot.sendMessage(target,choice(matn_r), message_id=msg.get("message_id"))
								get_id = my_id["data"]["message_update"]
								get__ID = get_id["message_id"]
								sleep(5)
								bot.editMessage(target,choice(galb),get__ID)
							except:
								print("err edit")

						elif msg.get("text").startswith("دیروز"):
							try:
								bot.sendVoice(target,"pooldar/4.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err esteghlal")

						elif msg.get("text").startswith("بیا"):
							try:
								bot.sendVoice(target,"pooldar/2.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("ejab error perspolis")

						elif msg.get("text").startswith("ویس نده"):
							try:
								bot.sendVoice(target,"pooldar/17.ogg",5000, message_id=msg.get("message_id"))
							except:
								print("ejab error")

						elif msg.get("text").startswith("خجالت بکش"):
							try:
								bot.sendVoice(target,"pooldar/1.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("ejab error")

						elif msg.get("text").startswith("حالم بده") or msg.get("text").startswith("بده حالم"):
							try:
								bot.sendVoice(target,"pooldar/6.ogg",5000, message_id=msg.get("message_id"))
							except:
								print("err he")

						elif msg.get("text").startswith("دارم میمیرم") or msg.get("text").startswith("الان میمیرم") or msg.get("text").startswith("درحال مردن"):
							try:
								bot.sendVoice(target,"pooldar/7.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err lef")

						elif msg.get("text").startswith("من برم") or msg.get("text").startswith("برم من") or msg.get("text").startswith("من برم؟") or msg.get("text").startswith("برم من؟"):
							try:
								bot.sendVoice(target,"pooldar/8.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err he")

						elif msg.get("text").startswith("ازت ناراحتم") or msg.get("text").startswith("دلخورم"):
							try:
								bot.sendVoice(target,"pooldar/9.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err answer hay")

						elif msg.get("text") == "کجا" or msg.get("text") == "کجا؟" or msg.get("text") == "کجه؟":
							try:
								bot.sendVoice(target,"pooldar/10.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err link gap")

						elif msg.get("text") == "بیا پی" or msg.get("text") == "میای پی" or msg.get("text") == "بیا پیویم" :
							try:
								bot.sendVoice(target,"pooldar/12.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err link t")

						elif msg.get("text").startswith("خب بگو"):
							try:
								bot.sendVoice(target,"pooldar/13.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err answer zabon")

						elif msg.get("text").startswith("پی چک") or msg.get("text").startswith("لطفا پی چک"):
							try:
								bot.sendVoice(target,"pooldar/14.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err khahesh")

						elif msg.get("text").startswith("وا"):
							try:
								bot.sendVoice(target,"pooldar/15.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err akhm")

						elif msg.get("text").startswith("لف بده"):
							try:
								bot.sendVoice(target,"pooldar/21.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err ghalb")

						elif msg.get("text").startswith("سلام بچه ها") or msg.get("text").startswith("سلام بروبچ"):
							try:
								bot.sendVoice(target,"pooldar/38.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err ghoge")

						elif msg.get("text").startswith("مال تویه") or msg.get("text").startswith("تقدیم بهت"):
							try:
								bot.sendVoice(target,"pooldar/39.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err memnone")

						elif msg.get("text").startswith("خدا شفات بده") or msg.get("text").startswith("شفا پیدا کنی") or msg.get("text").startswith("انشالله شفا پیدا کنی") or msg.get("text").startswith("شفا پیدا میکنی") :
							try:
								bot.sendVoice(target,"pooldar/41.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err  arr")

						elif msg.get("text").startswith("چه باحاله") or msg.get("text").startswith("باحاله"):
							try:
								bot.sendVoice(target,"pooldar/40.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err pe")

						elif msg.get("text").startswith("خاموش شو") or msg.get("text").startswith("خاموشش کن") or msg.get("text").startswith("ربات خاموش شو"):
							try:
								bot.sendVoice(target,"pooldar/43.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err bone")

						elif msg.get("text").startswith("گمشو لاشی") or msg.get("text").startswith("لاشی هستی") or msg.get("text").startswith("لوش کثیف") :
							try:
								bot.sendVoice(target,"pooldar/44.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err adab")

						elif msg.get("text").startswith("ربات نیست") or msg.get("text").startswith("رباط نیست") or msg.get("text").startswith("بات نیستی") or msg.get("text").startswith("ربات نیستی"):
							try:
								bot.sendVoice(target,"pooldar/45.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err DOSAT")

						elif msg.get("text").startswith("اعتماد به سقف") or msg.get("text").startswith("اعتماد به نفس"):
							try:
								bot.sendVoice(target,"pooldar/46.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err kega")

						elif msg.get("text").startswith("چقدر لینک میدن") or msg.get("text").startswith("لینکدونیه") or msg.get("text").startswith("لینکدونیه؟") or msg.get("text").startswith("اوه چه لینکی") or msg.get("text").startswith("چه لینکی"):
							try:
								bot.sendVoice(target,"pooldar/47.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err fadat")

						elif msg.get("text").startswith("ادمینشون نکن") or msg.get("text").startswith("از ادمینی در بیارشون") or msg.get("text").startswith("دیگه کسیو ادمین نکن"):
							try:
								bot.sendVoice(target,"pooldar/48.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err aghd")

						elif msg.get("text").startswith("کی منو دوست داره؟"):
							try:
								bot.sendVoice(target,"pooldar/49.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err gholasl")

						elif msg.get("text") == "سلام کن":
							try:
								bot.sendVoice(target,"pooldar/50.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("error")


						elif msg.get("text") == "نه":
							try:
								bot.sendMessage(target, "نکمه ، درد بگیری ایشالا", message_id=msg.get("message_id"))
							except:
								print("error no")

						elif msg.get("text") == "چرا میخندی؟" or msg.get("text") == "چرا میخندی" or msg.get("text") == "خنده داشت" or msg.get("text") == "خنده داشت؟" :
							try:
								bot.sendVoice(target,"pooldar/51.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("error remove amozesh")

						elif msg.get("text") == "زرنگی":
							try:
								bot.sendVoice(target,"pooldar/54.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("error timer")

						elif msg.get("text") == "حال کردی ":
							try:
								bot.sendVoice(target,"pooldar/53.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("error khosh1")

						elif msg.get("text").startswith("پروفایلت") or msg.get("text").startswith("پروفت") or msg.get("text").startswith("پروفتو باز کن") or msg.get("text").startswith("چرا نمیشه پروفتو ببینم؟") or msg.get("text").startswith("عکس پروفت"):
							try:
								bot.sendVoice(target,"pooldar/52.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err yes")

						elif msg.get("text") == "من آمدم":
							try:
								bot.sendMessage(target, "کاستو بیار ماست بگیر🐥", message_id=msg.get("message_id"))
							except:
								print("error khosh2")

						elif msg.get("text") == "راست میگی":
							try:
								bot.sendMessage(target, "کاستو بیار ماست بگیر🐥", message_id=msg.get("message_id"))
							except:
								print("error rast")

						elif msg.get("text") == "کس میگی" or msg.get("text") == "کص میگی" or msg.get("text") == "کص نگو" or msg.get("text") == "کس نگو" :
							try:
								bot.sendVoice(target,"pooldar/55.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("khar")

						elif msg.get("text") == "برسی":
							try:
								GAPE = bot.getGroupInfo(target)["data"]["group"]["group_title"]
								guidu = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								useru = bot.getUserInfo(guidu)["data"]["user"]["first_name"]
								caption =  f"{useru}"
								if not guidu in admins:
								    bot.sendMessage(target,f"کاربر {caption} یک شخص عادی در گروه {GAPE} می باشد" , metadata=[{"from_index": 6,"length": len(caption),"type":"MentionText","mention_text_object_guid":guidu}], message_id=msg.get("message_id"))
								else:
									bot.sendMessage(target, f"کاربر {caption} در گروه {GAPE} آدمین می باشد", metadata=[{"from_index": 6,"length": len(caption),"type":"MentionText","mention_text_object_guid":guidu}], message_id=msg.get("message_id"))
							except:
								print('analiz user')

						elif msg.get("text") == "رل" or msg.get("text") == "رلی یا سین" or msg.get("text") == "سینگلی" or msg.get("text") == "رل یا سینگل" or msg.get("text") == "گاییدم" or msg.get("text") == "رل داری" or msg.get("text") == "رلت" or msg.get("text") == "رلت رو میاری" or msg.get("text") == "کو رلت":
							try:
								bot.sendVoice(target,"pooldar/56.ogg",7000, message_id=msg.get("message_id"))
							except:
								print("err delete fesh")

						elif msg.get("text") == "زید میخوام" or msg.get("text") == "میخوامت" or msg.get("text") == "زیدم میشی؟" or msg.get("text") == "با من زید میشی" or msg.get("text") == "برلیم؟" or msg.get("text") == "رل بزنیم؟":
							try:
								bot.sendVoice(target,"pooldar/57.ogg",6000, message_id=msg.get("message_id"))
								print('sended voice')
							except:
								print("error")

						elif msg.get("text") == "میشناسی":
							try:
								bot.sendVoice(target,"pooldar/58.ogg",6000, message_id=msg.get("message_id"))
							except:

								print("error net")

						elif msg.get("text") == "نوچ":
							try:
								bot.sendVoice(target,"pooldar/59.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("error labkhand")

						elif msg.get("text") == "خسته شدم":
							try:
								bot.sendVoice(target,"pooldar/60.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("error")

						elif msg.get("text") == "خونه خالیه" or msg.get("text") == "میای خونمون" or msg.get("text") == "خونمون خالیه" or msg.get("text") == "ببرمت خونمون" or msg.get("text") == "خونمون یه لاکشپت داریم سوت میزنه" or msg.get("text") == "شام بیارمت خونمون" or msg.get("text") == "شب بیا خونمون":
							try:
								bot.sendVoice(target,"pooldar/61.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("error sigar")

						elif msg.get("text") == "سرم درد میکنه" or msg.get("text") == "سرد درد دارم" or msg.get("text") == "سرم درده" or msg.get("text") == "سرم واقعا درد میکنه":
							try:
								bot.sendVoice(target,"pooldar/62.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("error khosh2")

						elif msg.get("text").startswith("میخوام برم حموم") or msg.get("text") == "میای حموم" or msg.get("text") == "میری حموم" or msg.get("text") == "برو حموم" or msg.get("text") == "حموم" or msg.get("text") == "خواستم برم حموم":
							try:
								bot.sendVoice(target,"pooldar/63.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err luagh")

						elif msg.get("text").startswith("عکستو میدی؟") or msg.get("text") == "عکستو بده پی" or msg.get("text") == "از خودت بگو" or msg.get("text") == "سایز چنده" or msg.get("text") == "سایزت چنده" or msg.get("text") == "ممه هات" or msg.get("text") == "می می هات چند":
							try:
								bot.sendVoice(target,"pooldar/63.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err eshgh")

						#elif msg.get("text").startswith("test"):
							#try:
								#f = open('/storage/emulated/0/Download/arianbot/arianbot/arian.png')
								#p = Image.open('arian.png')
								#bot.sendPhoto(target, 'arian.png', p.size,message_id=msg["message_id"])
							#except:
								#print("err send image")

						elif msg.get("text").startswith("تغیر نام گروه") and msg.get("author_object_guid") in admins:
							try:
								if msg.get('reply_to_message_id') != None:
									bego2 = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if bego2['text'] != None:
										textss= bego2['text']
										BIO = bot.getGroupInfo(target)["data"]["group"]["description"]
										bot.editnameGroup(target,textss,B)
										bot.sendMessage(target,"با موفقیت نام گروه تغیر یافت ✅", message_id=msg.get("message_id"))
							except:
								print("err edit name group")

						elif msg.get("text").startswith("تغیر بیو گروه") and msg.get("author_object_guid") in admins:
							try:
								if msg.get('reply_to_message_id') != None:
									bego2 = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if bego2['text'] != None:
										textss= bego2['text']
										GAP = bot.getGroupInfo(target)["data"]["group"]["group_title"]
										bot.editbioGroup(target,textss,GAP)
										bot.sendMessage(target,"با موفقیت بیوگرافی گروه تغیر یافت ✅", message_id=msg.get("message_id"))
							except:
								print("err edit bio group")

						elif msg.get("text").startswith("ارتقا") and msg.get("author_object_guid") in admins:
							try:
								setadminf = msg.get("text").split(" ")[1][1:]
								setadmind = bot.getInfoByUsername(setadminf)["data"]["chat"]["abs_object"]["object_guid"]
								textwaa = bot.getInfoByUsername(setadminf)["data"]["user"]["first_name"]
								if not setadmind in admins:
									bot.setGroupAdmin(target,setadmind)
									bot.sendMessage(target, f"کاربر {textwaa} با موفقیت آدمین شد", message_id=msg.get("message_id"))

								else:
									bot.sendMessage(target, "❌ کاربر گرامی متاسفانه خطایی رخ داده است", message_id=msg.get("message_id"))

							except IndexError:
								guidzz = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								userz = bot.getUserInfo(guidzz)["data"]["chat"]["abs_object"]["object_guid"]
								textwaa = bot.getUserInfo(userz)["data"]["user"]["first_name"]
								if not userz in admins:
									bot.setGroupAdmin(target,userz)
									bot.sendMessage(target, f"کاربر {textwaa} با موفقیت آدمین شد", message_id=msg.get("message_id"))

								else:
									bot.sendMessage(target, "❌ کاربر گرامی متاسفانه خطایی رخ داده است", message_id=msg.get("message_id"))
							except:
								print('error setadmin')



						elif msg.get("text").startswith("تنزیل") and msg.get("author_object_guid") in admins:
							try:
								deletadminS = msg.get("text").split(" ")[1][1:]
								setdeletadminS = bot.getInfoByUsername(deletadminS)["data"]["chat"]["abs_object"]["object_guid"]
								textwaa = bot.getInfoByUsername(deletadminS)["data"]["user"]["first_name"]
								if setdeletadminS in admins:
									bot.deleteGroupAdmin(target,setdeletadminS)
									bot.sendMessage(target, f"کاربر {textwaa} با موفقیت از آدمین بودن برکنار شد", message_id=msg.get("message_id"))

								else:
									bot.sendMessage(target, "❌ کاربر گرامی متاسفانه خطایی رخ داده است", message_id=msg.get("message_id"))

							except IndexError:
								guidzVz = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								userVz = bot.getUserInfo(guidzVz)["data"]["chat"]["abs_object"]["object_guid"]
								textwaa = bot.getUserInfo(userVz)["data"]["user"]["first_name"]
								if  userVz in admins:
									bot.deleteGroupAdmin(target,userVz)
									bot.sendMessage(target, f"کاربر {textwaa} با موفقیت از آدمین بودن برکنار شد", message_id=msg.get("message_id"))

								else:
									bot.sendMessage(target, "❌ کاربر گرامی متاسفانه خطایی رخ داده است", message_id=msg.get("message_id"))
							except:
								print('error setdeletadmin')


						elif msg.get("text").startswith("بفرست") and msg.get("author_object_guid") in admins:
							try:
								if msg.get('reply_to_message_id') != None:
									bego2 = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if bego2['text'] != None:
										textss= bego2['text']
										kanal = textss
										mine = bot.getChannelInfo(channell)
										test = mine["data"]["channel"]["channel_title"]
										bot.sendMessage(channell, kanal)
										bot.sendMessage(target, f"✅ با موفقیت ارسال شد به کانال {test}", message_id=msg.get("message_id"))
										print('error Channel')
								else:
									bot.sendMessage(target, 'رو پیامی که میخواهید به کانالتان ارسال شود ریپ زنید❌',message_id=msg["message_id"])
							except:
								print('error Channel')


						elif msg.get("text").startswith("info"):
							try:
								users = msg.get("text").split(" ")[1][1:]
								guids = bot.getInfoByUsername(users)["data"]["user"]["first_name"]
								guid1 = bot.getInfoByUsername(users)["data"]["user"]["username"]
								guid2 = bot.getInfoByUsername(users)["data"]["user"]["bio"]
								guid3 = bot.getInfoByUsername(users)["data"]["user"]["user_guid"]
								if not guids in admins:
									bot.sendMessage(target, f"نام شما: || {guids} || \n آیدی شما: || {guid1} || \n بیوی شما: || {guid2} || \n گوید شما: || {guid3} || ", message_id=msg.get("message_id"))

								else:
									bot.sendMessage(target, f"نام شما: || {guids} || \n آیدی شما: || {guid1} || \n بیوی شما: || {guid2} || \n گوید شما: || {guid3} || ", message_id=msg.get("message_id"))

							except IndexError:
								guidZZ = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								user1 = bot.getUserInfo(guidZZ)["data"]["user"]["first_name"]
								user2 = bot.getUserInfo(guidZZ)["data"]["user"]["username"]
								user3 = bot.getUserInfo(guidZZ)["data"]["user"]["bio"]
								user4 = bot.getUserInfo(guidZZ)["data"]["user"]["user_guid"]
								if not guidZZ in admins:
									bot.sendMessage(target, f"نام شما: || {user1} || \n آیدی شما: || {user2} || \n بیوی شما: || {user3} || \n گوید شما: || {user4} || ", message_id=msg.get("message_id"))
								else:
									bot.sendMessage(target, f"نام شما: || {user1} || \n آیدی شما: || {user2} || \n بیوی شما: || {user3} || \n گوید شما: || {user4} || ", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))



						elif msg.get("text").startswith("تغیر پروفایل"):
							try:
								if msg.get("author_object_guid") in admins:
								   profile = ["pic/p1.jpg","pic/p2.jpg","pic/p3.jpg","pic/p4.jpg","pic/p5.jpg","pic/p6.jpg","pic/p7.jpg","pic/p8.jpg","pic/p9.jpg","pic/p10.jpg","pic/p11.jpg","pic/p12.jpg","pic/p13.jpg","pic/p14.jpg","pic/p15.jpg","pic/p16.jpg","pic/p17.jpg"]
								   photo = choice(profile)
								   bot.uploadAvatar(target,photo)
								else:
									bot.sendMessage(target, '❌ شما اجازه تغیر پرفایل گروه را ندارید',message_id=msg.get("message_id"))
							except:
								try:
									if msg.get("author_object_guid") in admins:
										profile = ["pic/p1.jpg","pic/p2.jpg","pic/p3.jpg","pic/p4.jpg","pic/p5.jpg","pic/p6.jpg","pic/p7.jpg","pic/p8.jpg","pic/p9.jpg","pic/p10.jpg","pic/p11.jpg","pic/p12.jpg","pic/p13.jpg","pic/p14.jpg","pic/p15.jpg","pic/p16.jpg","pic/p17.jpg"]
										photo = choice(profile)
										bot.uploadAvatar(target,photo)
									else:
										bot.sendMessage(target, '❌ شما اجازه تغیر پرفایل گروه را ندارید',message_id=msg.get("message_id"))
								except:
									print("err change profile group")


						elif msg.get("text").startswith("بگو"):
							try:
								if msg.get('reply_to_message_id') != None:
									bego1 = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if bego1['text'] != None:
										texts= bego1['text']
										bot.sendMessage(target,texts, message_id=msg.get("message_id"))
										print(' sended begho')
								else:
									bot.sendMessage(target, 'رو متن مورد نظر ریپ نزدید❌',message_id=msg["message_id"])
							except:
								print('error begho')

						elif msg.get("text").startswith("آپدیت لینک") and msg.get("author_object_guid") in admins:
							try:
								rules = open("linkgap_arianbot/linker.txt","w",encoding='utf-8').write(str(msg.get("text").strip("آپدیت لینک")))
								bot.sendMessage(target,  "✅آپدیت شد ", message_id=msg.get("message_id"))
								# link.close()
							except:
								bot.sendMessage(target, "مشکلی پیش اومد مجددا تلاش کنید!", message_id=msg.get("message_id"))

						elif msg.get("text") == "سنجاق" and msg.get("author_object_guid") in admins :
							try:
								bot.pin(target, msg["reply_to_message_id"])
								bot.sendMessage(target, "پیام مورد نظر با موفقیت سنجاق شد!", message_id=msg.get("message_id"))
							except:
								print("err pin")

						elif msg.get("text") == "برداشتن سنجاق" and msg.get("author_object_guid") in admins :
							try:
								bot.unpin(target, msg["reply_to_message_id"])
								bot.sendMessage(target, "پیام مورد نظر از سنجاق برداشته شد!", message_id=msg.get("message_id"))
							except:
								print("err unpin")

						elif msg.get("text").startswith("!trans"):
							try:
								responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
								al = [responser["result"]]
								bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
								bot.sendMessage(target, "نتیجه رو برات ارسال کردم😘", message_id=msg["message_id"])
							except:
								pass


						elif msg.get("text").startswith("!font"):
							try:
								response = get(f"http://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
								bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
								sleep(1)
								bot.sendMessage(target, "نتیجه رو برات ارسال کردم😘", message_id=msg["message_id"])
							except:
								print("error font")

						elif msg.get("text").startswith("حروف"):
							try:
								responser = get(f"https://api.codebazan.ir/num/?num={msg.get('text').split()[1]}").json()
								al = [responser["result"]["num"]]
								bot.sendMessage(target, "عدد شما به حروف:\n\n\n"+"".join(al)).text
								bot.sendMessage(target, "نتیجه رو برات ارسال کردم😘", message_id=msg["message_id"])
							except:
								pass


						elif msg.get("text").startswith("واژه"):
							try:
								responser = get(f"https://api.codebazan.ir/vajehyab/?text={msg.get('text').split()[1]}").json()
								aww = responser["result"]["mani"]
								awd = responser["result"]["fa"]
								awv = responser["result"]["Fdehkhoda"]
								bot.sendMessage(target, f"کلمه مورد نظر شما: {awd}\n\nمعنی کلمه: {aww}\n\nمعنی کلمه در دهخدا: {awv}").text
							except:
								pass


						elif msg.get("text").startswith("عید"):
							try:
								responser = get(f"https://api.codebazan.ir/new-year/").json()
								al = [responser["day"]]
								bot.sendMessage(target, "روز های مانده به عید 🌺\n"+"day: "+"".join(al)).text
							except:
								pass


						elif msg.get("text").startswith("اخبار"):
							try:
								responser = get(f"https://api.codebazan.ir/khabar/?kind={msg.get('text').split()[1]}").json()
								aww = responser["result"]["title"]
								bot.sendMessage(target, f"کلمه مورد نظر شما: {aww}").text
							except:
								pass


						elif msg.get("text").startswith("جوک") or msg.get("text").startswith("jok") or msg.get("text").startswith("!jok"):
							try:
								response = get("https://api.codebazan.ir/jok/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg["text"].startswith("arz"):
							try:
								response = get(f"http://api.codebazan.ir/arz/?type={msg['text'].split()[1]}").json()
								bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:50])).text
								bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
							except:
								pass

						elif msg["text"].startswith("tala"):
							try:
								response = get(f"http://api.codebazan.ir/arz/?type={msg['text'].split()[1]}").json()
								bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:50])).text
								bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
							except:
								pass

						elif msg.get("text").startswith("پسورد"):
							try:
								response = get(f"http://api.codebazan.ir/password/?length={msg['text'].split()[1]}").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("ویکی"):
							try:
								response = get(f"http://api.codebazan.ir/wiki/?search={msg['text'].split()[1]}").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass


						elif msg.get("text").startswith("ذکر") or msg.get("text").startswith("zekr") or msg.get("text").startswith("!zekr"):
							try:
								response = get("http://api.codebazan.ir/zekr/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("نام شاخ"):
							try:
								response = get("https://api.codebazan.ir/name/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("!chistan"):
							try:
								response = get("https://api.codebazan.ir/chistan/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("حدیث") or msg.get("text").startswith("hadis") or msg.get("text").startswith("!hadis"):
							try:
								response = get("http://api.codebazan.ir/hadis/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("بیو") or msg.get("text").startswith("bio") or msg.get("text").startswith("!bio"):
							try:
								response = get("https://api.codebazan.ir/bio/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg["text"].startswith("!weather"):
							try:
								response = get(f"https://api.codebazan.ir/weather/?city={msg['text'].split()[1]}").json()
								bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:20])).text
								bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
							except:
								pass

						elif msg.get("text").startswith("دیالوگ"):
							try:
								response = get("http://api.codebazan.ir/dialog/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("دانستنی متن"):
							try:
								response = get("http://api.codebazan.ir/danestani/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("پ ن پ") or msg.get("text").startswith("!pa-na-pa") or msg.get("text").startswith("په نه په"):
							try:
								response = get("http://api.codebazan.ir/jok/pa-na-pa/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("الکی مثلا") or msg.get("text").startswith("!alaki-masalan"):
							try:
								response = get("http://api.codebazan.ir/jok/alaki-masalan/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("داستان") or msg.get("text").startswith("!dastan"):
							try:
								response = get("http://api.codebazan.ir/dastan/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("!ping"):
							try:
								responser = get(f"https://api.codebazan.ir/ping/?url={msg.get('text').split()[1]}").text
								bot.sendMessage(target, responser,message_id=msg["message_id"])
							except:
								pass

						elif "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
							try:
								print("Yek ahmagh forwared Zad")
								bot.deleteMessages(target, [str(msg.get("message_id"))])
								print("tabligh forearedi pak shod")
							except:
								print("err delete forwared")

						elif msg.get("text") == "قوانین":
							try:
								rules = open("rules_arianbot/rules.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
								bot.sendMessage(msg.get("author_object_guid"),str(rules))
							except:
								print("err ghanon")

						elif msg.get("text") == "راهنما":
							try:
								G_U = msg.get("author_object_guid")
								ID_karbar = bot.getUserInfo(G_U)["data"]["user"]["username"]
								NAME_karbar = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
								if ID_karbar != None:
									ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,ID_karbar)["data"]["in_chat_members"]]
								else:
									if NAME_karbar != None:
										ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,NAME_karbar)["data"]["in_chat_members"]]
									else:pass
								G_UN = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
								if msg.get("author_object_guid") in ozv_ajbar:
									rules = open("helps_arianbot/cc.txt","r",encoding='utf-8').read()
									bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
								else:
									bot.sendMessage(target,f" کاربر  {G_UN} شما متاسفانه عضو کانال ما نیستید برای اجرای این\nدستور ابتدا عضو کانال ما شوید: \n@arian____bot", message_id=msg.get("message_id"))
							except:
								try:
									G_U = msg.get("author_object_guid")
									ID_karbar = bot.getUserInfo(G_U)["data"]["user"]["username"]
									NAME_karbar = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
									if ID_karbar != None:
										ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,ID_karbar)["data"]["in_chat_members"]]
									else:
										if NAME_karbar != None:
											ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,NAME_karbar)["data"]["in_chat_members"]]
										else:pass
									G_UN = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
									if msg.get("author_object_guid") in ozv_ajbar:
										rules = open("helps_arianbot/cc.txt","r",encoding='utf-8').read()
										bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
									else:
										bot.sendMessage(target,f" کاربر  {G_UN} شما متاسفانه عضو کانال ما نیستید برای اجرای این\nدستور ابتدا عضو کانال ما شوید: \n@arian____bot", message_id=msg.get("message_id"))
								except:
									print("err rahnama")



						elif msg.get("text") == "خوبی" or msg.get("text") == "خبی" or msg.get("text") == "چطوری":
							try:
								bot.sendVoice(target,"pooldar/3.ogg",6000, message_id=msg.get("message_id"))
							except:
								print("err building bot")

						elif msg.get("text").startswith("آپدیت قوانین") and msg.get("author_object_guid") in admins:
							try:
								rules = open("rules_arianbot/rules.txt","w",encoding='utf-8').write(str(msg.get("text").strip("آپدیت قوانین")))
								bot.sendMessage(target, "✅  قوانین بروزرسانی شد", message_id=msg.get("message_id"))
								# rules.close()
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت آرام 10" or msg.get("text") == "حالت ارام 10" and msg.get("author_object_guid") in admins:
							try:
								number = 10
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت آرام 30" or msg.get("text") == "حالت ارام 30" and msg.get("author_object_guid") in admins:
							try:
								number1 = 30
								bot.setGroupTimer(target,number1)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number1)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت آرام 60" or msg.get("text") == "حالت ارام 60" and msg.get("author_object_guid") in admins:
							try:
								number2 = 60
								bot.setGroupTimer(target,number2)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number2)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت آرام 80" or msg.get("text") == "حالت ارام 80" and msg.get("author_object_guid") in admins:
							try:
								number3 = 80
								bot.setGroupTimer(target,number3)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number3)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت ارام 100" or msg.get("text") == "حالت آرام 100" and msg.get("author_object_guid") in admins:
							try:
								number4 = 100
								bot.setGroupTimer(target,number4)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number4)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت آرام 3600" or msg.get("text") == "حالت ارام 3600" and msg.get("author_object_guid") in admins:
							try:
								number5 = 3600
								bot.setGroupTimer(target,number5)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number5)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت آرام 300" or msg.get("text") == "حالت ارام 300" and msg.get("author_object_guid") in admins:
							try:
								number6 = 300
								bot.setGroupTimer(target,number6)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number6)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت آرام 7200" or msg.get("text") == "حالت ارام 7200" and msg.get("author_object_guid") in admins:
							try:
								number7 = 7200
								bot.setGroupTimer(target,number7)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number7)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت آرام 18000" or msg.get("text") == "حالت ارام 1800" and msg.get("author_object_guid") in admins:
							try:
								number8 = 18000
								bot.setGroupTimer(target,number8)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number8)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))


						#test send image

						#image

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number = 0
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number1 = 0
								bot.setGroupTimer(target,number1)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))
                        
						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number2 = 0
								bot.setGroupTimer(target,number2)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number3 = 0
								bot.setGroupTimer(target,number3)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number4 = 0
								bot.setGroupTimer(target,number4)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number5 = 0
								bot.setGroupTimer(target,number5)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number6 = 0
								bot.setGroupTimer(target,number6)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number7 = 0
								bot.setGroupTimer(target,number7)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number8 = 0
								bot.setGroupTimer(target,number8)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))


						elif msg.get("text").startswith("اخطار") and msg.get("author_object_guid") in admins:
							try:
								mesagidhoshdar = msg.get("message_id")
								user = msg.get("text").split(" ")[1][1:]
								guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]
								if not guid in admins :
									alert(guid,user)

								else :
									bot.sendMessage(target, "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))

							except IndexError:
								mesagidhoshdar = msg.get("reply_to_message_id")
								guid = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								user = bot.getUserInfo(guid)["data"]["user"]["username"]
								if not guid in admins:
									alert(guid,user)
								else:
									bot.sendMessage(target, "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))



						elif msg.get("text") == "قفل گروه" or msg.get("text") == "قفل کردن گپ" or msg.get("text") == "قفل"  and msg.get("author_object_guid") in admins :
							try:
								bot.setMembersAccess(target, ["AddMember"])
								bot.sendMessage(target, "🔒 گروه قفل شد", message_id=msg.get("message_id"))
							except:
								print("err lock GP")

						elif msg.get("text") == "بازکردن گروه" or msg.get("text") == "باز کردن گپ" or msg.get("text") == "باز" and msg.get("author_object_guid") in admins :
							try:
								bot.setMembersAccess(target, ["SendMessages","AddMember"])
								bot.sendMessage(target, "🔓 گروه اکنون باز است", message_id=msg.get("message_id"))
							except:
								print("err unlock GP")

					else:
						if msg.get("text") == "روشن" or msg.get("text") == "\start":
							try:
								if msg.get("author_object_guid") in admins:
								   sleeped = False
								   bot.sendMessage(target, "ربا‌ت با موفقیت روشن شد!", message_id=msg.get("message_id"))
								else:
									bot.sendMessage(target, '❌ اجازه دسترسی به شما داده نشد',message_id=msg.get("message_id"))
							except:
								print('error one bot')

				elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
					name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
					data = msg['event_data']
					if data["type"]=="RemoveGroupMembers":
						try:
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							bot.sendMessage(target, f"‼️ کاربر {user} با موفقیت از گروه حذف شد .\nساعت حذف کاربر: {time.localtime().tm_sec} : {time.localtime().tm_min} : {time.localtime().tm_hour}", message_id=msg["message_id"])
							# bot.deleteMessages(target, [msg["message_id"]])
						except:
							print("err rm member answer")

					elif data["type"]=="AddedGroupMembers":
						try:
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							p = Image.open('R.png')
							bot.sendPhoto(target, 'R.png', p.size,caption=  f"هــای {user} عزیز 😘🌹 \n • به گـروه {name} خیـلی خوش اومدی 😍❤️ \nلطفا قوانین رو رعایت کن .\n\nساعت ورود کاربر: {time.localtime().tm_sec} : {time.localtime().tm_min} : {time.localtime().tm_hour}\n\n 💎 برای مشاهده قوانین کافیه کلمه (قوانین) رو ارسال کنی!\nدوست داری ربات بسازی؟ بیا اینجا😍👇\nسازنده:\narianBOT\nآرین عباسی" , message_id=msg["message_id"])
							# bot.deleteMessages(target, [msg["message_id"]])
						except:
							try:
								user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
								p = Image.open('R.png')
								bot.sendPhoto(target, 'R.png', p.size,caption=  f"هــای {user} عزیز 😘🌹 \n • به گـروه {name} خیـلی خوش اومدی 😍❤️ \nلطفا قوانین رو رعایت کن .\n\nساعت ورود کاربر: {time.localtime().tm_sec} : {time.localtime().tm_min} : {time.localtime().tm_hour}\n\n 💎 برای مشاهده قوانین کافیه کلمه (قوانین) رو ارسال کنی!\nدوست داری ربات بسازی؟ بیا اینجا😍👇\nسازنده:\narianBOT\nآرین عباسی" , message_id=msg["message_id"])
							except:
								print("err add group member")

					elif data["type"]=="LeaveGroup":
						try:
							user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
							bot.sendMessage(target, f"خدانگهدار {user} 👋 ", message_id=msg["message_id"])
							# bot.deleteMessages(target, [msg["message_id"]])
						except:
							try:
								user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
								bot.sendMessage(target, f"خدانگهدار {user} 👋 ", message_id=msg["message_id"])
							except:
								print("err lef")


					elif data["type"]=="JoinedGroupByLink":
						try:
							user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
							p = Image.open('R.png')
							bot.sendPhoto(target, 'R.png', p.size,caption=  f"هــای {user} عزیز 😘🌹 \n • به گـروه {name} خیـلی خوش اومدی 😍❤️ \nلطفا قوانین رو رعایت کن .\n\nساعت ورود کاربر: {time.localtime().tm_sec} : {time.localtime().tm_min} : {time.localtime().tm_hour}\n\n 💎 برای مشاهده قوانین کافیه کلمه (قوانین) رو ارسال کنی!\nدوست داری ربات بسازی؟ بیا اینجا😍👇\nسازنده:\narianBOT\nآرین عباسی" , message_id=msg["message_id"])
							# bot.deleteMessages(target, [msg["message_id"]])
						except:
							try:
								user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
								p = Image.open('R.png')
								bot.sendPhoto(target, 'R.png', p.size,caption=  f"هــای {user} عزیز 😘🌹 \n • به گـروه {name} خیـلی خوش اومدی 😍❤️ \nلطفا قوانین رو رعایت کن .\n\nساعت ورود کاربر: {time.localtime().tm_sec} : {time.localtime().tm_min} : {time.localtime().tm_hour}\n\n 💎 برای مشاهده قوانین کافیه کلمه (قوانین) رو ارسال کنی!\nدوست داری ربات بسازی؟ بیا اینجا😍👇\nسازنده:\narianBOT\nآرین عباسی" , message_id=msg["message_id"])
							except:
								print("err answer join By link")

				else:
					if "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("message_id")])
						guid = msg.get("author_object_guid")
						user = bot.getUserInfo(guid)["data"]["user"]["username"]
						alert(guid,user,True)
						bot.deleteMessages(target, [msg.get("message_id")])

					else:
						if msg["type"] =="Sticker" and not msg.get("author_object_guid") in admins:
							if lock_Sticker == True:
								guid_st = msg.get("author_object_guid")
								user_st = bot.getUserInfo(guid_st)["data"]["user"]["username"]
								alert_sticker(guid_st,user_st)
								sleep(1)
								bot.deleteMessages(target, [msg.get("message_id")])
							else:
								if msg["type"] == "FileInline" and not msg.get("author_object_guid") in admins:
									if msg["file_inline"]["type"] =="Gif":
										print("true")
										if lock_GIF == True:
											guid_GF = msg.get("author_object_guid")
											user_GF = bot.getUserInfo(guid_GF)["data"]["user"]["username"]
											alert_GIF(guid_GF,user_GF)
											sleep(1)
											bot.deleteMessages(target, [msg.get("message_id")])
										else:pass

					continue
			except:
				continue

			answered.append(msg.get("message_id"))
			print("Group:" +"[" + msg.get("message_id") + "] >>> " + msg["type"] + ">>>" + " " + msg.get("text") + "\n")


	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue
