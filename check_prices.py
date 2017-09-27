import csv
import os
import requests
import json
import psycopg2

STATIONFILE = 'stations.csv'
PRICE_API_URL = 'https://www.tankerkoenig.de/json/detail.php'
API_KEY = '00000000-0000-0000-0000-000000000002'

DB_HOST='localhost'
DB_NAME='gascheck'
DB_USER='gascheck'
DB_PASSWORD='gascheck'


def load_stations():
    with open(STATIONFILE, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        return [row[0] for row in reader if row][1:] # first line should be header


def load_api_key():
    if os.path.isfile('apikey'):
        with open('apikey') as apikeyfile:
            return apikeyfile.read()
    return API_KEY


def check_price(station_id):
    params = {
        'apikey': API_KEY,
        'id': station_id
    }
    r = requests.get(PRICE_API_URL, params=params)
    parsed = json.loads(r.text[1:-1])
    return parsed


def db_insert_price(conn, station, type, price):
    cursor = conn.cursor()
    query = "INSERT INTO pricecheck (station_id, type, price) VALUES ('%s', '%s', %s)" % (station, type, price)
    cursor.execute(query)


API_KEY = load_api_key()

conn = psycopg2.connect(host=DB_HOST,dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
for station in load_stations():
    info = check_price(station)
    for type in ('e5', 'e10', 'diesel'):
        price = info.get(type, False)
        if price:
            db_insert_price(conn, station, type, price)

conn.commit()
