import requests
import json
import time
from .models import Category, SubCategory
from json import JSONDecodeError


def createnewtoken() -> object:
    url = "https://public-apis-api.herokuapp.com/api/v1/auth/token"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    res = json.loads(response.text)
    return res["token"]


def getapilist():
    token = createnewtoken()
    k = 0
    for i in Category.objects.all():
        print(i)
        count = 1
        while count < 6:
            url = f"https://public-apis-api.herokuapp.com/api/v1/apis/entry?page={count}&category={i}"
            payload = {}
            headers = {
                'Authorization': f"Bearer {token}"
            }
            try:
                response = requests.request("GET", url, headers=headers, data=payload)
                k += 1
                res = response.json()
                if not res['categories']:
                    break
                for j in res['categories']:
                    api = j['API']
                    desc = j['Description']
                    auth = j['Auth']
                    https = j['HTTPS']
                    cors = j['Cors']
                    link = j['Link']
                    category_ = j['Category']
                    # print(api, category_)
                    b = SubCategory(Api=api, Description=desc, Auth=auth, HTTPS=https, Cors=cors, Link=link,
                                    Category=category_)
                    # print("SAVED IN THE DATABASE")
                    b.save()
            except JSONDecodeError:
                time.sleep(61)
                response = requests.request("GET", url, headers=headers, data=payload)
                k += 1
                res = response.json()
                try:
                    if not res['categories']:
                        break
                except KeyError:
                    break
                for j in res['categories']:
                    api = j['API']
                    desc = j['Description']
                    auth = j['Auth']
                    https = j['HTTPS']
                    cors = j['Cors']
                    link = j['Link']
                    category_ = j['Category']
                    print(api, category_)
                    b = SubCategory(Api=api, Description=desc, Auth=auth, HTTPS=https, Cors=cors, Link=link,
                                    Category=category_)
                    print("SAVED IN THE DATABASE")
                    b.save()
            except KeyError:
                break
            count += 1
        if k >= 40:
            token = createnewtoken()


def getcategory():
    token = createnewtoken()
    x = []
    for i in range(1, 6):
        url = f"https://public-apis-api.herokuapp.com/api/v1/apis/categories?page={i}"
        payload = {}
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.json()
        x += result['categories']
    for i in x:
        b = Category(name=i)
        b.save()
