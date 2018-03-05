# -*- coding:utf-8 -*-
import pyowm
from twilio.rest import Client
from settings import twilio_acct, owm, city, incoming_num, outgoing_num

# Twilio credentials
client = Client(twilio_acct.keys()[0], twilio_acct.values()[0])


owm_credentials = pyowm.OWM(owm) # OpenWeatherMap API key

nrb_forecast = owm_credentials.daily_forecast(city)
tomorrow = pyowm.timeutils.tomorrow() # The next day's forecast

if nrb_forecast.will_be_rainy_at(tomorrow): # If it's gonna rain the next day
    client.api.account.messages.create(
            to=incoming_num,
            from_=outgoing_num,
            body="Wear rain cloths, it's gonna rain tomorrow"
        )
else:
    client.api.account.messages.create(
        to=incoming_num,
        from_=outgoing_num,
        body="Do not worry it won't rain tomorrow, you can wear shorts"
    )
    





