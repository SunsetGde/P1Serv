
import logging
from aiogram import Bot,Dispatcher,executor,types
from glob import glob
from aiogram.types import InlineKeyboardMarkup , InlineKeyboardButton, InputTextMessageContent, InlineQueryResultArticle
import os, hashlib
from config import TOKEN, on_startup, cmd, Wel,Well, rules, lists;

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


#инлайн
inline_btn_1 = InlineKeyboardButton('❤️Чат❤️',url='http://t.me/gamster_1', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

inline_btn_11 = InlineKeyboardButton('📄Правила📄', callback_data='button6')
inline_btn_12 = InlineKeyboardButton('🇷🇺Канал🇷🇺', url='http://t.me/gamster_71')
inline_kb11 = InlineKeyboardMarkup().add(inline_btn_11, inline_btn_12)

inline_btn_2 = InlineKeyboardButton('📄Музыка📄', callback_data='button1')
inline_btn_3 = InlineKeyboardButton('👮‍♀️Комманды👮‍♀️',callback_data='button2')
inline_kb2 = InlineKeyboardMarkup().add(inline_btn_2, inline_btn_3)

#приветствие
@dp.message_handler(content_types=['new_chat_members'])
async def welll(message: types.Message):
	await bot.send_photo(message.chat.id, open('Welcome/1.png', 'rb') , caption= Well, reply_markup = inline_kb11)
@dp.message_handler(content_types=['left_chat_member'])
async def exit(message: types.Message):
	name3 = message.from_user.get_mention(as_html=True)
	await message.answer(f"{name3}, покинул(а) чат😢", parse_mode='html')


#downld_audio
@dp.message_handler(commands=["start"])
async def commands_send(message : types.Message):
        with open('Welcome/1.png', 'rb') as photo:
        	await bot.send_photo (message.from_user.id, photo, caption= "😀Приветствую тебя😀" , reply_markup = inline_kb1, )
        	await message.bot.send_message(message.from_user.id, "😀Нажми для просмотра списка Комманд и Музыки😀", reply_markup = inline_kb2)	
@dp.message_handler(content_types=["audio"])
async def p1bot(message: types.Message):
	await message.audio.download(destination_file=f"{message.audio.file_name.split('.')[0]}.mp3")
	await message.bot.send_message(message.from_user.id,("|Успешно загружено|"))
	
#Музыка	
@dp.message_handler(text=['1',"Выпускник", "выпускник", "ВЫПУСКНИК"])
async def sendaudio(message: types.Audio):
	await message.bot.send_message(message.from_user.id, 'Да ты - заебал мой код дрочить')
	await bot.send_audio(message.from_user.id , audio=open("Music/ВЫПУСКНИК.mp3", 'rb'))
@dp.message_handler(text=['2',"LaCuca", "lacuca", "Lacuca"])
async def sendaudio(message: types.Audio):
	await message.bot.send_message(message.from_user.id, 'Да ты - заебал мой код дрочить')
	await bot.send_audio(message.from_user.id , audio=open("Music/LaCuca.mp3", 'rb'))	
@dp.message_handler(text=['3',"Я солдат","я солдат","Я Солдат"])
async def sendaudio(message: types.Audio):
	await message.bot.send_message(message.from_user.id, 'Да ты - заебал мой код дрочить')
	await bot.send_audio(message.from_user.id , audio=open("Music/Я солдат.mp3", 'rb'))
@dp.message_handler(text=['4','Бисакодил','бисакодил'])
async def sendaudio(message: types.Audio):
 await message.bot.send_message(message.from_user.id, 'Да ты - заебал мой код дрочить')
 await bot.send_audio(message.from_user.id , audio=open("Music/Бисакодил.mp3", 'rb'))
@dp.message_handler(text=['5','Дорогу молодым','дорогу молодым'])
async def sendaudio(message: types.Audio):
 await message.bot.send_message(message.from_user.id, 'Да ты - заебал мой код дрочить')
 await bot.send_audio(message.from_user.id , audio=open("Music/Дорогу молодым.mp3", 'rb'))
@dp.message_handler(text=['6','Лали','лали'])
async def sendaudio(message: types.Audio):
	await message.bot.send_message(message.from_user.id, 'Да ты - заебал мой код дрочить')
	await bot.send_audio(message.from_user.id , audio=open("Music/Лали.mp3", 'rb'))
@dp.message_handler(text=['7','Ночь','ночь'])
async def sendaudio(message: types.Audio):
	await message.bot.send_message(message.from_user.id, 'Да ты - заебал мой код дрочить')
	await bot.send_audio(message.from_user.id , audio=open("Music/Ночь.mp3", 'rb'))
@dp.message_handler(text=['8','Про любовь','про любовь'])
async def sendaudio(message: types.Audio):
	await message.bot.send_message(message.from_user.id, 'Да ты - заебал мой код дрочить')
	await bot.send_audio(message.from_user.id , audio=open("Music/Про любовь.mp3", 'rb'))
@dp.message_handler(text=['9','Аллея','аллея'])
async def sendaudio(message: types.Audio):
	await message.bot.send_message(message.from_user.id, 'Да ты - заебал мой код дрочить')
	await bot.send_audio(message.from_user.id , audio=open("Music/Аллея.mp3", 'rb'))
@dp.message_handler(text=['10','Камин','Камин'])
async def sendaudio(message: types.Audio):
	await message.bot.send_message(message.from_user.id, 'Да ты - заебал мой код дрочить')
	await bot.send_audio(message.from_user.id , audio=open("Music/Камин.mp3", 'rb'))

#адмсписок
@dp.message_handler(text=["адм","Адм"])
async def admins(message: types.Message):
    chat_admins = await bot.get_chat_administrators(message.chat.id)
    lst = ['-------------------\n👮‍♀️Админ -> ' f"@{admin.user.username}👮‍♀️|\n ➡️Ник:  {admin.user.full_name}\n 🔎TGID : @id{admin.user.id}|" for admin in chat_admins]
    await bot.send_message(message.chat.id, text="\n".join(lst))
   
#модер
@dp.message_handler(text=['бан', 'Бан'], user_id=('5163851408' , '5206349660'))
async def ban(message: types.Message):
	await message.bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
	name2 = message.from_user.get_mention(as_html=True)
	await message.answer(f"🔴 @{message.reply_to_message.from_user.username}: был забанен🔴\n👮‍♀️Модератор: {name2}", parse_mode='html')
@dp.message_handler(text=['разбан', 'Разбан'], user_id=('5163851408','5206349660'))
async def unban(message: types.Message):
	await message.bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
	await message.answer(f"🆘 @{message.reply_to_message.from_user.username}: Разбанен🆘")		

#inline_mode	
@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery):
    input_content = types.InputTextMessageContent(inline_query.query or Wel)
    item = types.InlineQueryResultArticle(id='1', title='🥺Красивое Приветсвие🥺',
    
    input_message_content=input_content)
    await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)
 
#развличение
@dp.message_handler(commands=[""], commands_prefix='!')
async def repus(message:types.Message):
	   mes = message.text.lower()
	   await message.reply("А вы знали что...")
	   await message.reply(mes)
	   await message.delete()
	   
@dp.message_handler(text=["Кости"])
async def Dice(m: types.Message):
	msg = await m.reply_dice()	
#говорун
@dp.message_handler(text=['Добавь друзей','Друзей добавь','Друзей','Добавь','добавь друзей'])
async def dl(message: types.Message):
	await message.reply('А сам то Добавь!😠\nСам сидишь и Жопу греешь😠')

@dp.message_handler(text=['Привет','привет','Здравствуй','Прив','прив'])
async def deel(message: types.Message):
	await bot.send_audio(message.chat.id , audio=open("Joke/1.ogg", 'rb'))
	await message.reply("Спать Пиздуй😠\nЛибо я Приду и тебя отшлепаю😠")
#inline_callback
@dp.callback_query_handler(lambda c: c.data == 'button1' )
async def process_callback_button1(callback_query: types.CallbackQuery ):
    await bot.answer_callback_query(callback_query.id , 'Держи❤️')	
    await bot.send_message(callback_query.from_user.id, lists)   
@dp.callback_query_handler(lambda c: c.data == 'button2' , )
async def process_callback_button1(callback_query: types.CallbackQuery ):
    await bot.answer_callback_query(callback_query.id , 'Пользуйся❤️')	
    await bot.send_message(callback_query.from_user.id, cmd)   
@dp.callback_query_handler(lambda c: c.data == 'button6' , )
async def process_callback_button1(callback_query: types.CallbackQuery , ):
    await bot.answer_callback_query(callback_query.id , 'Внимательно прочитай❤️' )
    await bot.send_message(callback_query.message.chat.id, rules) 
 #кмд
@dp.message_handler(text=['кмд','Кмд','Помощь'])
async def cmmd(message:types.Message):
	await message.reply(cmd)
#правила
@dp.message_handler(text=['Правила','правила'])
async def rul(message: types.Message):
	await message.reply(rules)
@dp.message_handler(text=['Мут','мут'],user_id=('5163851408','5206349660'))
async def rul(message):
	await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages=False)
	name1 = message.from_user.get_mention(as_html=True)
	await message.answer(f'🔇 @{message.reply_to_message.from_user.username} Лишается прав слова🔇\n👮‍♀️Модератор: {name1}',parse_mode= 'html')
@dp.message_handler(text=['Размут','размут'],user_id=('5163851408','5206349660'))
async def rul(message):
	await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_other_messages=False)
	await message.reply(f"🔊 @{message.reply_to_message.from_user.username}: Внезапно перестал быть Немым🔊")

@dp.message_handler(text=['-ФФГ','-ффг'],user_id=('5163851408','5206349660'))
async def rul(message):
	await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages=True)
	await message.reply(f"🎆@{message.reply_to_message.from_user.username}: Ограничен в отправке ФОТО/ФАЙЛЫ/ГЕО🎆")
@dp.message_handler(text=['+ФФГ','+ффг'],user_id=('5163851408','5206349660'))
async def rul(message):
	await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages=True)
	await message.reply(f"🎆@{message.reply_to_message.from_user.username}: Теперь может отправлять ФОТО/ФАЙЛЫ/ГЕО🎆")
	
#рп
@dp.message_handler(text=['Трахнуть','трахнуть','Выебать','выебать'])
async def rp(message: types.Message):
	name1 = message.from_user.get_mention(as_html=True)
	name2 = message.reply_to_message.from_user.get_mention(as_html=True)
	await bot.send_message(message.chat.id, f'🥵| {name1} Выебал(-а) {name2}',parse_mode='html')
@dp.message_handler(text=['Чмок','чмок','Чмокнуть'])
async def rp(message: types.Message):
	name1 = message.from_user.get_mention(as_html=True)
	name2 = message.reply_to_message.from_user.get_mention(as_html=True)
	await bot.send_message(message.chat.id, f'☺️|{name1} Чмокнул(а) {name2}',parse_mode='html')
@dp.message_handler(text=['Ебнуть','ебнуть'])
async def rp(message: types.Message):
	name1 = message.from_user.get_mention(as_html=True)
	name2 = message.reply_to_message.from_user.get_mention(as_html=True)
	await bot.send_message(message.chat.id, f'🤯|{name1} Уебал(а) Керпичем {name2}',parse_mode='html')
@dp.message_handler(text=['Кусь','кусь'])
async def rp(message: types.Message):
	name1 = message.from_user.get_mention(as_html=True)
	name2 = message.reply_to_message.from_user.get_mention(as_html=True)
	await bot.send_message(message.chat.id, f'😋|{name1} Откусил(а) кусок кожи у {name2}',parse_mode='html')
	
@dp.message_handler(lambda message: message.text.lower() == "бот")
async def boot(msg: types.Message):
	await msg.answer(f"""♻️По вашему приказу прибыл!""")


	
	
#старт	
if __name__ == '__main__':
	executor.start_polling(dp , skip_updates=True, on_startup=on_startup)
