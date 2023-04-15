from bs4 import BeautifulSoup
import requests, lxml, json, sqlite3

connection = sqlite3.connect("itstep,")


connection.close()