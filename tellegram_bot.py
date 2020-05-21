import pyowm
import telebot
import os

owm = pyowm.OWM('1a420a768f9e1ff26e71c86845a06fcc',language = "RU")
#bot = telebot.TeleBot("1042248088:AAFCzpyLI0Ps-m65NkrXR5ErtxDiV6khPg4")
token = os.eviron.get('BOT_TOKEN')

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = "В городе "+ message.text + " сейчас " + w.get_detailed_status()  + "\n"
	answer += " Температура сейчас в районе " + str(temp) + "\n\n"

	if temp < 10:
	    answer +="На улице холодно,чтобы не заболеть одевайтесь теплее:)"
	elif temp <20: 
	    answer +="На улице прохладно оденься теплее."
	else:
	    answer +="На улице тёплая погода,можно идти гулять,одевайся как хочешь!"

	bot.send_message(message.chat.id, answer )

bot.polling( none_stop = True)