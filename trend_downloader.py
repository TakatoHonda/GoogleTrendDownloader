#!/usr/bin/env python
#-*- coding:utf-8 -*-

# trend_downloader.py
# written by Takato Honda
# August 13th, 2016

from pytrends.pyGTrends import pyGTrends
import time
from random import randint

# settings 
# input your google account information
google_username = ""
google_password = ""
save_path = ""

# keyword samples
sns = "Twitter, Facebook, Instagram"
os  = "Windows, OS X, Android"
browser = "Google Chrome, Safari, firefox"
game = "final fantasy, pokemon, crush of clans"
fashion_cheap = "ZARA, H&M, GAP"
fashion_expensive = "Ralph Lauren, Burberry, Aquascutum"
music = "ROCK, POP, JAZZ"
staple_food = "rice, bread, corn"
smart_phone = "Galaxy, XPERIA, iPhone"
anime = "Fullmetal Alchemist, Death Note, Bleach"
vehicle = "Toyota, Volkswagen, General Motors"
electric_company = "Samsung, LG, SONY"
script_language = "Javascript, Python, Perl"
math_language = "Matlab, R, Octave"
watch = "Rolex, Omega, Apple Watch"
dog = "Bulldog, Chihuahua, Dachshund"
cat = "Munchkin, Scottish fold, Ragdoll"
animal = "Dog, Cat, Hamster"
sport = "Football, Baseball, Basketball"
cpu = "Intel, AMD, ARM"
earphone = "Audio technica, Shure, Beats"
movie = "Prime video, Hulu, Netflix"
wearable = "Jawbone, Fitbit, Misfit"
sick = "Gastroentitis, Influenza, Ebola"

key_sets = [browser, game, fashion_cheap, fashion_expensive, music, staple_food, smart_phone, anime, vehicle, electric_company, script_language, math_language, watch, dog, cat, animal, sport, cpu, earphone, movie, wearable, sick]

# countries
geos = ["", "US", "JP", "CA", "FR", "IS", "IE", "AZ", "AF", "VI", "AE", "DZ", "AR", "AW", "AL", "AM", "AI", "AO", "AG", "AD", "YE", "GB", "VG", "IL", "IT", "IQ", "IR", "IN", "ID", "UG", "UA", "UZ", "UY", "EC", "EG", "EE", "ET", "SV", "AU", "AT", "AX", "OM", "NL", "GH", "GG", "GY", "KZ", "QA", "CV", "GA", "CM", "GM", "KH", "MP", "GN", "CY", "CU", "CW", "GR", "KG", "GT", "GP", "GU", "KW", "GL", "GD", "HR", "KY", "KE", "CI", "CR", "KM", "CO", "CG", "CD", "SA", "BL", "ZM", "PM", "SM", "MF", "SL", "DJ", "GI", "JE", "JM", "GE", "SY", "SG", "SX", "ZW", "CH", "SE", "SD", "ES", "SR", "LK", "LK", "SK", "SI", "SZ", "SC", "GQ", "SN", "RS", "KN", "VC", "SH", "LC", "SO", "SB", "TC", "TH", "KR", "TW", "TJ", "TZ", "CZ", "TD", "CF", "CN", "TN", "CL", "DK", "DE", "TG", "DO", "DM", "TT", "TM", "TR", "NG", "NA", "NI", "NE", "NC", "NZ", "NP", "NO", "BH", "HT", "PK", "VU", "BS", "PG" , "BM", "PW", "PY", "BB", "PS", "HU", "BD", "TL", "FJ", "PH", "FI", "BT", "PR", "FO", "FK", "BR", "GF", "BG", "BF", "BN", "BI", "BI", "VN", "BJ", "VE", "BY", "BZ", "PE", "BE", "PL", "BA", "BW", "BQ", "BO", "PT", "HK", "HN", "MH", "MO", "MK", "MG", "YT", "MW", "ML", "MT", "MQ", "MY", "IM", "FM", "ZA", "SS", "MM", "MX", "MU", "MR", "MZ", "MC", "MV", "MD", "MA", "MN", "ME", "MS", "JO", "LA", "LV", "LT", "LY", "LI", "LR", "RO", "LU", "RW", "LS", "LB", "RE", "RU"]

# connect to Google
connector = pyGTrends(google_username, google_password)

# get trends for each keywords and geometries
for keywords in key_sets:
    for geo in geos:
        # make request
        connector.request_report(keywords, geo=geo)

        # wait a random amount of time between requests to avoid the bot detection
        time.sleep(randint(5,10))

        # download file
        connector.save_csv(save_path, keywords + ", geo=" + geo)

