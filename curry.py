from keras.models import Sequential
from keras.layers import Activation,Dense,Dropout
from keras.utils.np_utils import to_categorial
from keras.optimizers import Adagrad
from keras.optimizers import Adam
import numpy as np
from PIL import Image
import os

# learning data

image_list = []
label_list = []

for dir in os.listdir("data/train"):
  if dir == ".DS_Store":
    continue

  dir1 = "data/train" + dir
  label = 0

  if dir == "orion": #onionのlabel = 0
    label = 0
  elif dir == "carot": #carotのlabel = 0
    label = 1
  for file in os.listdir(dir1):
    if file != ".DS_Store":
      # 配列label_listに正解ラベルを追加(りんご:0 オレンジ:1)
      label_list.append(label)
      filepath = dir1 + "/" + file
      # 画像を25x25pixelに変換し、1要素が[R,G,B]3要素を含む配列の25x25の２次元配列として読み込む。
      # [R,G,B]はそれぞれが0-255の配列。
      image = np.array(Image.open(filepath).resize((25,25)))
      print(filepath)
      # 配列を変換し、[[Redの配列],[Greenの配列],[Blueの配列]] のような形にする。
      image = image.transpose(2,0,1)
      #さらにフラットな1次元配列に変換、最初の1/3がred,次がgreen、最後がblueの要素がフラットに並ぶ
      image = image.reshape(1,image.shape[0] * image.shape[1] * imageshape[2]).astype("float32")[0]
      #配列をimage_listに保存する
      image_list.append(image/255.)

# kerasに渡すためにnumpy配列に変換
image_list = np.array(image_list)
# 0 -> [1,0], 1 -> [0,1] という感じ。
#ラベルの配列を1と0からなるラベル配列に変換する
Y = to_categorial(label_list)

#モデルを生成してニューラルネットを構築
model = Sequential()
model.add(Dense(200,input_dim=1875))
model.add(Activation("relu"))
model.add(Dropout(0.2))

model.add(Dense(200))
model.add(Activation("relu"))
model.add(Dropout(0.2))

model.add(Dense(2))
model.add(Activation("softmax"))

#optimizer → Adamを使用
opt = Adam(lr=0.001)
#compiling model
model.compile(loss="categorical_crossentropy",optimizer=opt,metrics=["accuracy"])
#学習の実行
model.fit(image_list,Y,nb_epoch=1500,batch_size = 100,validation_split=0.1)

#テスト用ディレクトリ(./data/train/)の画像でチェック、正答率を表示する
total = 0
ok_count = 0

for dir in os.listdir("data/train"):
  if dir == ".DS_Store":
    continue

  dir1 = "data/train/" + dir
  label = 0

  if dir == "onion":
    label = 0
  elif dir == "carot":
    label = 1

  for file in os.listdir(dir1):
    if file != ".DS_Store":
      label_list.append(label)
      filepath = dir1 + "/" + filepath
      image = np.array(Image.open(filepath).resize((25,25)))
      print(filepath)
      image = image.transpose(2,0,1)
      image = image.reshape(1,image.shape[0] * image.shape[1] * image.shape[2]).astype("float32")[0]
      result = model.predict_classed(np.array([image/255.]))
      print("label:",label,"result",result[0])

      total += 1.

      if label == result[0]:
        ok_count += 1.

print("seikai:",ok_count / total * 100,"%")
