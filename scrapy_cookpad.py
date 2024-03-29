# -*- coding:utf-8 -*-

import urllib
import BeautifulSoup

# HTML を取得
html = urllib.urlopen("http://cookpad.com/recipe/1069321").read()

# 解析用の BeautifulSoup オブジェクトを作成
soup = BeautifulSoup.BeautifulSoup(html)

# レシピのメイン部を取得
recipe_main = soup.find("div", attrs={"id": "recipe-main"})

# レシピのタイトルを取得
recipe_title = recipe_main.find("h1", attrs={"class": "recipe-title fn clearfix"})
print recipe_title.text

# 材料を取得
for ingredient in recipe_main.findAll("div", attrs={"class": "ingredient_name"}):
    print ingredient.span.text

#写真を取得
img = recipe_main.find('div',attrs={"id" : "main-photo"}).find('img',attrs={"class":'analytics_tracking photo large_photo_clickable'})
print img['src']
