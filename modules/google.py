# from duckduckgo_search import ddg
# import urllib3
# from datetime import datetime
import requests
import os, sys, json
import logging

# if we are running in Docker
if os.environ.get("dockerrun") == "yes":
    dockerflag = True
else:
    dockerflag = False

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.environ.get("SEARCH_ENGINE_ID")

# 向 Google 搜索 API 发送请求，但返回的结果只包含关键词搜索结果的标题和摘要，不包括链接。
# 用于构建摘要、查询结果的概览等应用程序
def GoogleSearchSimply(query, numResults):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': query,
        'key': GOOGLE_API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'num': numResults
    }
    headers = {
        'Origin': 'https://chat.openai.com'
    }
    response = requests.get(url, params=params, headers=headers)
    results = response.json()
    items = results['items']
    filteredData = [{'title': item['title'], 'body': item['snippet']} for item in items]
    return filteredData

# 用于向 Google 搜索 API 发送请求并获取搜索结果。它返回的结果包含搜索结果中的标题、链接和摘要等信息
# GoogleSearch() 可用于构建搜索引擎、自然语言处理应用等
def GoogleSearch(query, numResults):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": GOOGLE_API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "num": numResults
    }
    headers = {
        "Origin": "https://chat.openai.com"
    }
    response = requests.get(url, params=params, headers=headers)
    results = response.json()
    items = results["items"]
    filteredData = []
    for item in items:
        data = {"title": item["title"], "href": item["link"], "body": item["snippet"]}
        filteredData.append(data)
    return filteredData