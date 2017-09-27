import csv
import psycopg2

DB_HOST='localhost'
DB_NAME='gascheck'
DB_USER='gascheck'
DB_PASSWORD='gascheck'

STATIONFILE = 'stations.csv'

def load_stations():
    with open(STATIONFILE, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        return [row for row in reader if row][1:] # first line should be header


conn = psycopg2.connect(host=DB_HOST,dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
cursor = conn.cursor()
query = "INSERT INTO station (station_id, brandname, city, street, streetno) VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(query, load_stations())
conn.commit()