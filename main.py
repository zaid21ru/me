import requests 
import telebot 
from telebot import types
import requests
from uuid import uuid4
import random
import os
import json
from user_agent import generate_user_agent
import sys
from datetime import datetime
from bs4 import BeautifulSoup
import datetime
key = types.InlineKeyboardMarkup()

zzk=0
id = '5000568348'
tok = '6370336437:AAG32-nIXIguOOh4MoYgx793doR1zZMXMTU'
import datetime
zxu = datetime.datetime.now()
bot = telebot.TeleBot(tok)
@bot.message_handler(commands=['start'])
def start(message):
 global zzk
 zzk+=1
 nm = message.from_user.first_name
 id2 = message.from_user.id
 userk = message.from_user.username
 zxu = datetime.datetime.now()
 tt=f'''
عضو يستخدم البوت…
ـــــــــــــــــــــــــــــــــــــــ
اسم المستخدم : {nm}
يوزر المستخدم : @{userk}
ايدي المستخدم : {id2}
رقم المستخدم  : {zzk}
الوقت : {zxu}
ـــــــــــــــــــــــــــــــــــــــ
ـ @P_W_7'''

 key = types.InlineKeyboardMarkup()
 bot.send_message(id, f"<strong>{tt}</strong>",parse_mode="html",reply_markup=key)
 

 
 zek = types.InlineKeyboardButton(text ="صيـد نوع | x_x_x |", callback_data = 'oq')
 zed = types.InlineKeyboardButton(text ="صيـد نوع | x_x.x |", callback_data = 'om')

 ze = types.InlineKeyboardButton(text ="صيـد نوع | x.x_x |", callback_data = 'og')
  
 zn = types.InlineKeyboardButton(text ="صيـد نوع شبه رباعي", callback_data = 'oh')
  
 fr = message.from_user.first_name
 maac = types.InlineKeyboardMarkup()
 maac.row_width=1
 maac.add(zek,zed,ze,zn)
 bot.send_message(message.chat.id,f"<strong>اهلا بك : | {fr} | في بـوت صيـد يوزرات انستكـرام للحصول على معلوماتك [ /info ]</strong>",parse_mode="html",reply_markup=maac)
@bot.callback_query_handler(func=lambda call:True)
def st(call):
 
 
 if call.data== 'oq':
            nc1 = types.InlineKeyboardMarkup(row_width=2)
            message= bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='ارسـل عدد محاولات الفـحص',reply_markup=nc1)
            bot.register_next_step_handler(message,k1,message.id)

 elif call.data== 'om':
            nc1 = types.InlineKeyboardMarkup(row_width=2)
            message= bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='ارسـل عدد محاولات الفـحص',reply_markup=nc1)
            bot.register_next_step_handler(message,k2,message.id)

 elif call.data== 'og':
            nc1 = types.InlineKeyboardMarkup(row_width=2)
            message= bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='ارسـل عدد محاولات الفـحص',reply_markup=nc1)
            bot.register_next_step_handler(message,k3,message.id)

 elif call.data== 'oh':
            nc1 = types.InlineKeyboardMarkup(row_width=2)
            message= bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='ارسـل عدد محاولات الفـحص',reply_markup=nc1)
            bot.register_next_step_handler(message,k4,message.id)
      
                      
def k1(message,id):
	z=0
	bad=0
	good=0
	try:
		add = int(message.text)
		if add < 5000:
			while True:
				z+=1
				u = "".join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm')for i in range(1))
				d = "".join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm')for i in range(1))
				s = "".join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm')for i in range(1))
				user = u+'_'+d+'_'+s
				url = "https://i.instagram.com/api/v1/accounts/create/"
				he = {
	'Content-Length': '437',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Host': 'i.instagram.com',
	'Connection': 'Keep-Alive',
	'User-Agent': 'Instagram 113.0.0.39.122 Android (30/11; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; en_IQ)',
	'Cookie': 'mid=Y16iBgABAAFggfUYwajggkGFz-hs',
	'Cookie2': '$Version=1',
	'Accept-Language': 'en-IQ, en-US',
	'X-IG-Connection-Type': 'WIFI',
	'X-IG-Capabilities': 'AQ==',
	'Accept-Encoding': 'gzip',}
				da = {
"email":"zodhok@gmail.com",
"username":f"{user}",
"password":"zxcvbm1@"+user,
"device_id":"android-"+str(uuid4()),
"guid":str(uuid4()),
	 	}
				rr = requests.post(url,headers=he,data=da).text
				if "username" in rr:
					bad+=1
				elif 'email_is_taken' in rr:
					good+=1
					tt = f"""
Done get User successfully
═══════════════════
Username : {user}
	═══════════════════
Programmer  : @P_W_7
	"""
					bot.send_message(message.chat.id, f"<strong>{tt}</strong>",parse_mode="html",reply_markup=key)					
				else:
					bad+=1
					
				mees = types.InlineKeyboardMarkup(row_width=1)
				ba12=types.InlineKeyboardButton(f" 📜 Check User Instagram",callback_data='b12')
				ba8=types.InlineKeyboardButton(f" ⏱️ Add : {add} > {z}",callback_data='b8')
				ba11=types.InlineKeyboardButton(f" ✅ Good Username : {good}",callback_data='b11')
				ba10=types.InlineKeyboardButton(f" ❌ Good Username : {bad}",callback_data='b10')
				ba9=types.InlineKeyboardButton(f" 🔍 check Username : {user}",callback_data='b9')
				mees.add(ba12,ba8,ba11,ba10,ba9)
				bot.edit_message_text(chat_id=message.chat.id,message_id=id,text="بدأ صيـد يوزرات انستكرام",parse_mode='markdown',reply_markup=mees)
				
				if z == add:
					bot.send_message(message.chat.id, f"<strong>لقـد انتهاء عدد محاولات الفحـض</strong>",parse_mode="html",reply_markup=key)
					return
					
		else:
			bot.send_message(message.chat.id, f"<strong>لا يمكن فحص اكثـر من 5000 😒</strong>",parse_mode="html",reply_markup=key)				
	except:
		bot.send_message(message.chat.id, f"<strong>هنـاك خطـأ ما </strong>",parse_mode="html",reply_markup=key)

def k2(message,id):
	z=0
	bad=0
	good=0
	try:
		add = int(message.text)
		if add < 5000:
			while True:
				z+=1
				u = "".join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm')for i in range(1))
				d = "".join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm')for i in range(1))
				s = "".join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm')for i in range(1))
				user = u+'_'+d+'.'+s
				url = "https://i.instagram.com/api/v1/accounts/create/"
				he = {
	'Content-Length': '437',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Host': 'i.instagram.com',
	'Connection': 'Keep-Alive',
	'User-Agent': 'Instagram 113.0.0.39.122 Android (30/11; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; en_IQ)',
	'Cookie': 'mid=Y16iBgABAAFggfUYwajggkGFz-hs',
	'Cookie2': '$Version=1',
	'Accept-Language': 'en-IQ, en-US',
	'X-IG-Connection-Type': 'WIFI',
	'X-IG-Capabilities': 'AQ==',
	'Accept-Encoding': 'gzip',}
				da = {
"email":"zodhok@gmail.com",
"username":f"{user}",
"password":"zxcvbm1@"+user,
"device_id":"android-"+str(uuid4()),
"guid":str(uuid4()),
	 	}
				rr = requests.post(url,headers=he,data=da).text
				if "username" in rr:
					bad+=1
				elif 'email_is_taken' in rr:
					good+=1
					tt = f"""
Done get User successfully
═══════════════════
Username : {user}
	═══════════════════
Programmer  : @P_W_7
	"""
					bot.send_message(message.chat.id, f"<strong>{tt}</strong>",parse_mode="html",reply_markup=key)					
				else:
					bad+=1
					
				mees = types.InlineKeyboardMarkup(row_width=1)
				ba12=types.InlineKeyboardButton(f" 📜 Check User Instagram",callback_data='b12')
				ba8=types.InlineKeyboardButton(f" ⏱️ Add : {add} > {z}",callback_data='b8')
				ba11=types.InlineKeyboardButton(f" ✅ Good Username : {good}",callback_data='b11')
				ba10=types.InlineKeyboardButton(f" ❌ Good Username : {bad}",callback_data='b10')
				ba9=types.InlineKeyboardButton(f" 🔍 check Username : {user}",callback_data='b9')
				mees.add(ba12,ba8,ba11,ba10,ba9)
				bot.edit_message_text(chat_id=message.chat.id,message_id=id,text="بدأ صيـد يوزرات انستكرام",parse_mode='markdown',reply_markup=mees)
				
				if z == add:
					bot.send_message(message.chat.id, f"<strong>لقـد انتهاء عدد محاولات الفحـض</strong>",parse_mode="html",reply_markup=key)
					return
					
		else:
			bot.send_message(message.chat.id, f"<strong>لا يمكن فحص اكثـر من 5000 😒</strong>",parse_mode="html",reply_markup=key)				
	except:
		bot.send_message(message.chat.id, f"<strong>هنـاك خطـأ ما </strong>",parse_mode="html",reply_markup=key)
		

def k3(message,id):
	z=0
	bad=0
	good=0
	try:
		add = int(message.text)
		if add < 5000:
			while True:
				z+=1
				u = "".join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm')for i in range(1))
				d = "".join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm')for i in range(1))
				s = "".join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm')for i in range(1))
				user = u+'.'+d+'_'+s
				url = "https://i.instagram.com/api/v1/accounts/create/"
				he = {
	'Content-Length': '437',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Host': 'i.instagram.com',
	'Connection': 'Keep-Alive',
	'User-Agent': 'Instagram 113.0.0.39.122 Android (30/11; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; en_IQ)',
	'Cookie': 'mid=Y16iBgABAAFggfUYwajggkGFz-hs',
	'Cookie2': '$Version=1',
	'Accept-Language': 'en-IQ, en-US',
	'X-IG-Connection-Type': 'WIFI',
	'X-IG-Capabilities': 'AQ==',
	'Accept-Encoding': 'gzip',}
				da = {
"email":"zodhok@gmail.com",
"username":f"{user}",
"password":"zxcvbm1@"+user,
"device_id":"android-"+str(uuid4()),
"guid":str(uuid4()),
	 	}
				rr = requests.post(url,headers=he,data=da).text
				if "username" in rr:
					bad+=1
				elif 'email_is_taken' in rr:
					good+=1
					tt = f"""
Done get User successfully
═══════════════════
Username : {user}
	═══════════════════
Programmer  : @P_W_7
	"""
					bot.send_message(message.chat.id, f"<strong>{tt}</strong>",parse_mode="html",reply_markup=key)					
				else:
					bad+=1
					
				mees = types.InlineKeyboardMarkup(row_width=1)
				ba12=types.InlineKeyboardButton(f" 📜 Check User Instagram",callback_data='b12')
				ba8=types.InlineKeyboardButton(f" ⏱️ Add : {add} > {z}",callback_data='b8')
				ba11=types.InlineKeyboardButton(f" ✅ Good Username : {good}",callback_data='b11')
				ba10=types.InlineKeyboardButton(f" ❌ Good Username : {bad}",callback_data='b10')
				ba9=types.InlineKeyboardButton(f" 🔍 check Username : {user}",callback_data='b9')
				mees.add(ba12,ba8,ba11,ba10,ba9)
				bot.edit_message_text(chat_id=message.chat.id,message_id=id,text="بدأ صيـد يوزرات انستكرام",parse_mode='markdown',reply_markup=mees)
				
				if z == add:
					bot.send_message(message.chat.id, f"<strong>لقـد انتهاء عدد محاولات الفحـض</strong>",parse_mode="html",reply_markup=key)
					return
					
		else:
			bot.send_message(message.chat.id, f"<strong>لا يمكن فحص اكثـر من 5000 😒</strong>",parse_mode="html",reply_markup=key)				
	except:
		bot.send_message(message.chat.id, f"<strong>هنـاك خطـأ ما </strong>",parse_mode="html",reply_markup=key)
		
			
def k4(message,id):
	z=0
	bad=0
	good=0
	try:
		add = int(message.text)
		if add < 5000:
			while True:
				z+=1
				user = "".join(random.choice('123456_78_90q_wert_yu_iop_asdfghjklz_xcvb.nm')for i in range(5))
				url = "https://i.instagram.com/api/v1/accounts/create/"
				he = {
	'Content-Length': '437',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Host': 'i.instagram.com',
	'Connection': 'Keep-Alive',
	'User-Agent': 'Instagram 113.0.0.39.122 Android (30/11; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; en_IQ)',
	'Cookie': 'mid=Y16iBgABAAFggfUYwajggkGFz-hs',
	'Cookie2': '$Version=1',
	'Accept-Language': 'en-IQ, en-US',
	'X-IG-Connection-Type': 'WIFI',
	'X-IG-Capabilities': 'AQ==',
	'Accept-Encoding': 'gzip',}
				da = {
"email":"zodhok@gmail.com",
"username":f"{user}",
"password":"zxcvbm1@"+user,
"device_id":"android-"+str(uuid4()),
"guid":str(uuid4()),
	 	}
				rr = requests.post(url,headers=he,data=da).text
				if "username" in rr:
					bad+=1
				elif 'email_is_taken' in rr:
					good+=1
					tt = f"""
Done get User successfully
═══════════════════
Username : {user}
	═══════════════════
Programmer  : @P_W_7
	"""
					bot.send_message(message.chat.id, f"<strong>{tt}</strong>",parse_mode="html",reply_markup=key)					
				else:
					bad+=1
					
				mees = types.InlineKeyboardMarkup(row_width=1)
				ba12=types.InlineKeyboardButton(f" 📜 Check User Instagram",callback_data='b12')
				ba8=types.InlineKeyboardButton(f" ⏱️ Add : {add} > {z}",callback_data='b8')
				ba11=types.InlineKeyboardButton(f" ✅ Good Username : {good}",callback_data='b11')
				ba10=types.InlineKeyboardButton(f" ❌ Good Username : {bad}",callback_data='b10')
				ba9=types.InlineKeyboardButton(f" 🔍 check Username : {user}",callback_data='b9')
				mees.add(ba12,ba8,ba11,ba10,ba9)
				bot.edit_message_text(chat_id=message.chat.id,message_id=id,text="بدأ صيـد يوزرات انستكرام",parse_mode='markdown',reply_markup=mees)
				
				if z == add:
					bot.send_message(message.chat.id, f"<strong>لقـد انتهاء عدد محاولات الفحـض</strong>",parse_mode="html",reply_markup=key)
					return
					
		else:
			bot.send_message(message.chat.id, f"<strong>لا يمكن فحص اكثـر من 5000 😒</strong>",parse_mode="html",reply_markup=key)				
	except:
		bot.send_message(message.chat.id, f"<strong>هنـاك خطـأ ما </strong>",parse_mode="html",reply_markup=key)
		
						
@bot.message_handler(commands=["info"])
def inf(message):
    global zzk
    zzk+=1
    zxu = datetime.datetime.now()
    nm = message.from_user.first_name
    id2 = message.from_user.id
    userk = message.from_user.username
    bio = bot.get_chat(message.from_user.id).bio
    
    ttg=f'''
رتبتك هي عضو 🥰 
ـــــــــــــــــــــــــــــــــــــــ
اسم المستخدم : {nm}
يوزر المستخدم : @{userk}
ايدي المستخدم : {id2}
رقم المستخدم  : {zzk}
الوقت : {zxu}
بايو المستخدم : {bio}
ـــــــــــــــــــــــــــــــــــــــ
ـ @P_W_7'''
    key = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, f"<strong>{ttg}</strong>",parse_mode="html",reply_markup=key) 	


while True:
	def zzq():
		try:
			bot.polling(none_stop=True)
		except:
			zzq()
	zzq()e": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}""" in r:
					good+=1
					tt = f"""
	Done get User successfully
	═══════════════════
	Username : {user}
	═══════════════════
	Programmer  : @P_W_7
	"""
					bot.send_message(message.chat.id, f"<strong>{tt}</strong>",parse_mode="html",reply_markup=key)
					
				else:
					bad+=1
					
				mees = types.InlineKeyboardMarkup(row_width=1)
				ba12=types.InlineKeyboardButton(f" 📜 Check User Instagram",callback_data='b12')
				ba8=types.InlineKeyboardButton(f" ⏱️ Add : {add} > {z}",callback_data='b8')
				ba11=types.InlineKeyboardButton(f" ✅ Good Username : {good}",callback_data='b11')
				ba10=types.InlineKeyboardButton(f" ❌ Good Username : {bad}",callback_data='b10')
				ba9=types.InlineKeyboardButton(f" 🔍 check Username : {user}",callback_data='b9')
				mees.add(ba12,ba8,ba11,ba10,ba9)
				bot.edit_message_text(chat_id=message.chat.id,message_id=id,text="بدأ صيـد يوزرات انستكرام",parse_mode='markdown',reply_markup=mees)
				
				if z == add:
					bot.send_message(message.chat.id, f"<strong>لقـد انتهاء عدد محاولات الفحـض</strong>",parse_mode="html",reply_markup=key)
					return
					
		else:
			bot.send_message(message.chat.id, f"<strong>لا يمكن فحص اكثـر من 2000 😒</strong>",parse_mode="html",reply_markup=key)			
	except:
		bot.send_message(message.chat.id, f"<strong>هنـاك خطـأ ما </strong>",parse_mode="html",reply_markup=key)
				
						
@bot.message_handler(commands=["info"])
def inf(message):
    global zzk
    zzk+=1
    zxu = datetime.datetime.now()
    nm = message.from_user.first_name
    id2 = message.from_user.id
    userk = message.from_user.username
    bio = bot.get_chat(message.from_user.id).bio
    
    ttg=f'''
رتبتك هي عضو 🥰 
ـــــــــــــــــــــــــــــــــــــــ
اسم المستخدم : {nm}
يوزر المستخدم : @{userk}
ايدي المستخدم : {id2}
رقم المستخدم  : {zzk}
الوقت : {zxu}
بايو المستخدم : {bio}
ـــــــــــــــــــــــــــــــــــــــ
ـ @P_W_7'''
    key = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, f"<strong>{ttg}</strong>",parse_mode="html",reply_markup=key) 	


while True:
	def zzq():
		try:
			bot.polling(none_stop=True)
		except:
			zzq()
	zzq()