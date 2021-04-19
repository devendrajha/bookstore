import requests
import json
import random
import string

letters = string.ascii_letters
#print ( ''.join(random.choice(letters) for i in range(10)) )

def post():
    url = "http://127.0.0.1:8000/bookstore/"
    payload = json.dumps({
        "title": "Devendra k Jha",
        "author": "Alex",
        "book_description": "Python 3.6x engineering",
        "cost": 153,
        "create_time": "2021-04-21T00:33:41+00:00"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

def getbookdetails(bid):
    url = "http://127.0.0.1:8000/bookstore/bookdetails/" + bid
    headers = {}
    response = requests.request("GET", url, headers=headers)
    return response.text


def getallbooks():
    url = "http://127.0.0.1:8000/bookstore/"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    return response.text


def get_with_limit(limit):
    url = "http://127.0.0.1:8000/bookstore/page/" + str(limit)
    payload = {}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


def delete(bid):
    url = "http://127.0.0.1:8000/bookstore/" + bid
    payload = {}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)

    return response.text



def update(bid):
    url = "http://127.0.0.1:8000/bookstore/" + bid
    payload = json.dumps({
        "title": "Mandel kk",
        "author": "pearson",
        "book_description": "Python 3.6x",
        "cost": 153,
        "create_time": "2021-04-21T00:33:41+00:00"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response.text


def search(search_string):
    url = "http://127.0.0.1:8000/bookstore/search/" + search_string
    headers = {}
    response = requests.request("GET", url, headers=headers)

    return response.text


#print(search('google'))
print(getbookdetails())
#post()

