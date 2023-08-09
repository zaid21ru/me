import requests 
import telebot 
from telebot import types
import random
import json

key = types.InlineKeyboardMarkup()
import datetime
zxu = datetime.datetime.now()
tok ='6370336437:AAG32-nIXIguOOh4MoYgx793doR1zZMXMTU'

ida = '5000568348'
bot = telebot.TeleBot(tok)
#معلوماتي
@bot.message_handler(func=lambda followinG:True )
def re(message):
  text = message.text
  id = message.chat.id
  if 'تعليمات' in text:
  	key = types.InlineKeyboardMarkup()
  	f="""
1- للتقيد : تقيد + ايديه
2- لفك التقيد : فك +ايديه
3- لمعلومات حسابك : معلوماتي
4- لمعرفه رتبتك - رتبتي
"""
  	bot.reply_to(message, f"<strong>{f}</strong>",parse_mode="html",reply_markup=key)
  elif 'تقيد' in text:
  	try:
	  	idf = message.from_user.id
	  	if int(ida) == int(idf):
		  	ch = text.split('تقيد ')[1]
		  	bot.restrict_chat_member(id, ch, can_send_messages=False)
		  	key = types.InlineKeyboardMarkup()
		  	bot.reply_to(message, f"<strong>قيدته</strong>",parse_mode="html",reply_markup=key)
	  	else:
	  		key = types.InlineKeyboardMarkup()
	  		bot.reply_to(message, f"<strong>انت لست المدير</strong>",parse_mode="html",reply_markup=key)
  	except:pass	  	
  elif 'فك' in text:
  	try:
	  	if int(ida) == int(idf):
		  	ch = text.split('فك ')[1]
		  	bot.restrict_chat_member(id, ch, can_send_messages=True)
		  	key = types.InlineKeyboardMarkup()
		  	bot.reply_to(message, f"<strong>تم رفعت القيود</strong>",parse_mode="html",reply_markup=key)
		  	
	  	else:
	  		key = types.InlineKeyboardMarkup()
	  		bot.reply_to(message, f"<strong>انت لست المدير</strong>",parse_mode="html",reply_markup=key)
  	except:pass	  		
  elif 'معلوماتي' in text:
    nm = message.from_user.first_name
    id2 = message.from_user.id
    userk = message.from_user.username
    bio = bot.get_chat(message.from_user.id).bio
    
    ttg=f''' 
معلومات الوصخ وصلت
ـــــــــــــــــــــــــــــــــــــــ
اسم المستخدم : {nm}
يوزر المستخدم : @{userk}
ايدي المستخدم : {id2}
الوقت : {zxu}
بايو المستخدم : {bio}
ـــــــــــــــــــــــــــــــــــــــ'''
    key = types.InlineKeyboardMarkup()
    bot.reply_to(message, f"<strong>{ttg}</strong>",parse_mode="html",reply_markup=key)
 
  elif 'رتبتي' in text:
  	idf = message.from_user.id
  	if int(ida) == int(idf):
  		mo=['المدير العسل ✨','صأحب احلى ضحكه ✨','القائد 🦅','المدير الصاك😍','المعدل🔥','الهيبه🌚','المدير الشمع ❤️‍🔥','المنور دائماً🖤','المدير الورد🥀']
  		dr = random.choice(mo)
  		key = types.InlineKeyboardMarkup()
  		bot.reply_to(message, f"<strong>{dr}</strong>",parse_mode="html",reply_markup=key)
  	else:
  		rm = ['زربه مدري شني','ابو صماخ','كـس عـجوز','طفل جني ✨','الجلب النغل','نعال حمام الكروب','العريض','الفاهي','العـاهره','زب الهاشه','صأحب المؤخره ذهبيبه✨','حصان ميت','كلب ابن خوش بشر','طلقه','ابو زرف✨','الكافر🙂','انته سلفا حطه بيك','الغبي','الشاخط','شحاطه','نعال',"زربه مال بشر",'بوله مال صخل','كـس جني','خريه','عيران اثنان','نيااج','مفتوح مابيك خير','مطي مكصوص اذانه','وحش مجاري','اجيف البشر','خيسه','مطلقه','ابو لباس','حيوان نادر جدأ','حمار وحشي','ابو طيـز المعضل','هواي ضرط','كـس جاموسه','المحترم✨','الـطيف','العسـل✨','المفترس✨','المبرمج القوي','خادم للتواليت','راس البريج','اسوء ماخلق✨','حيوان الليف','حيوان مفترس','بريعصي بي سكر','قرد بي فلاوزنه','تمساح مجاري','تاج راسكم✨','كاضم الساهر✨','هيفا وهبي مصلخه','العضيم✨','انته مو ميت؟','عبالي متت😓','رتبتك بل حاويه','حالك حال صطل','رتبتك العافيه','كـس خروف','مايا خليفه','النمر الوردي','صاحب اكبر مؤخره','لاحس الارجل','زعطووط','زعطوط','المابيك حض','المحمض','زواع نمر','زواع حامل','البربوك','البقره الضاحكه🔥','الحقير😠','شغلك وراه 12🥺','صطل لبن','كـس عجل','المخربط','زمال🙂','مثيل ديس زلمه ماتفيد بشي😓','ابو ديوس','صأحب اعضم طيز','عيـر ميت','ممثل سـكسي','رجل دين','معيدي','نوع من انواع الحيتان','شـعره مال شايب✨','دم ليلت دخله','بيك مرض خطر','كافر ومشرك','زربه انته','زربان انته','عيـر يابس','كـس قرش','كـس هاني','زمال مدري نعال','كـس اسود','ضروك مال حمام','بيك بواسير؟','ابو طيـز المحبحب','السافل ','صأحب اطول قضيب','ابو وجه الـكس','عباس ركابي','تيسير','عكروك فاطس','زيج شايب','مطي اسود','مطي ابيض','كـس مطي','كـس جريذي','زب حوت','زب فيل','زب كحبـه','مطي محنط','زفر','بربوك متطور✨','حيوان مائي','حيوان برري','ديس جحش','مفتوح خلفي','وضيفتك تمص للناس✨','ممثل فاشل','انسان فاشل✨','حوت اصفر','كـس بزون','زب عكروك','زب قرش اخضر','زب فار']
  		dn = random.choice(rm)
  		key = types.InlineKeyboardMarkup()
  		bot.reply_to(message, f"<strong>{dn}</strong>",parse_mode="html",reply_markup=key)

  elif 'ابن' in text:
  	key = types.InlineKeyboardMarkup()
  	bot.reply_to(message, f"<strong>نعم انا موجود🤷🏻‍♂️</strong>",parse_mode="html",reply_markup=key)
  elif 'بوت' in text:
  	key = types.InlineKeyboardMarkup()
  	bot.reply_to(message, f"<strong>احم احد صأحلي بوت؟🕺🏻</strong>",parse_mode="html",reply_markup=key)
  elif 'حلو' in text:
   	key = types.InlineKeyboardMarkup()
   	bot.reply_to(message, f"<strong>صلِ على محمد والَ محمد</strong>",parse_mode="html",reply_markup=key)
   	
   	
  elif 'سلفادور' in text:
  	o=['تأج راسك','هسه يجي','لا تصيح على ابي','ابي نأئم','سلفادور عمك','هسه يجي سلفا','شتريد منه ؟','نصي صوت هسه يجي سلفا','لا تلح هسه يرد']
  	dn=random.choice(o)
  	key = types.InlineKeyboardMarkup()
  	bot.reply_to(message, f"<strong>{dn}</strong>",parse_mode="html",reply_markup=key)
  elif 'سلفا' in text:
  	o=['تأج راسك','هسه يجي','لا تصيح على ابي','ابي نأئم','سلفادور عمك','هسه يجي سلفا','شتريد منه ؟','نصي صوت هسه يجي سلفا','لا تلح هسه يرد']
  	dn=random.choice(o)
  	key = types.InlineKeyboardMarkup()
  	bot.reply_to(message, f"<strong>{dn}</strong>",parse_mode="html",reply_markup=key)

  elif 'زيد'  or 'zaid' in text:
  	if 'zaid' in text:
  		try:
	  		ch = text.split('zaid ')[1]
	  		url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
	  		head = {
		    'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
		    'Connection': 'keep-alive',
		    'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
		    'Accept': '*/*',
		    'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
		    'Content-Type': 'application/json',
		    'Accept-Language': 'en-GB,en;q=0.9'}
		    
	  		data = {
		    'data': {
		        'message':ch,
		    }
		}   
	  		response = requests.post(url, headers=head, data=json.dumps(data))
	  		try:
	  			result = response.json()["result"]["choices"][0]["text"]
	  			key = types.InlineKeyboardMarkup()
	  			bot.reply_to(message, f"<strong>{result}</strong>",parse_mode="html",reply_markup=key)
	  		except:
	  			key = types.InlineKeyboardMarkup()
	  			bot.reply_to(message, f"<strong>لـم افهم ؟</strong>",parse_mode="html",reply_markup=key)
  		except:pass
  	elif 'زيد' in text:
  		try:
	  		ch = text.split('زيد ')[1]
	  		url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
	  		head = {
		    'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
		    'Connection': 'keep-alive',
		    'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
		    'Accept': '*/*',
		    'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
		    'Content-Type': 'application/json',
		    'Accept-Language': 'en-GB,en;q=0.9'}
		    
	  		data = {
		    'data': {
		        'message':ch,
		    }
		}   
	  		response = requests.post(url, headers=head, data=json.dumps(data))
	  		try:
	  			result = response.json()["result"]["choices"][0]["text"]
	  			key = types.InlineKeyboardMarkup()
	  			bot.reply_to(message, f"<strong>{result}</strong>",parse_mode="html",reply_markup=key)
	  		except:
	  			key = types.InlineKeyboardMarkup()
	  			bot.reply_to(message, f"<strong>لـم افهم ؟</strong>",parse_mode="html",reply_markup=key)
  		except:pass		
  else:
  	pass
while True :
    try:
        bot.infinity_polling()
    except Exception as error :
        time.sleep(3)
