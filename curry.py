from keras.models import Sequential
from keras.layers import Activation,Dense,Dropout
from np_utils import to_categorical
from keras.optimizers import Adagrad
from keras.optimizers import Adam
import numpy as np
from PIL import Image
import os

# learning data
def multi_layer_perceptron():
  #モデルを生成してニューラルネットを構築
  model = Sequential()
  model.add(Dense(200,input_dim=1875)) # 入力層1875ノード, 隠れ層に200ノード, 全結合
  model.add(Activation("relu")) #活性化関数relu
  model.add(Dropout(0.2))

  model.add(Dense(200)) #中間層200ノード
  model.add(Activation("relu")) #活性化関数relu
  model.add(Dropout(0.2))

  model.add(Dense(2)) #出力層3ノード,全結合している
  model.add(Activation("softmax"))

  return model

# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Flatten
# from keras.layers import Conv2D, MaxPooling2D
# def multi_layer_perceptron():
#     model = Sequential()
#     model.add(Dense(200,input_dim=1875)) # 入力層1875ノード, 隠れ層に200ノード, 全結合
#     model.add(Activation("relu")) #活性化関数relu
#     model.add(Dropout(0.2))

#     # model.add(Conv2D(32, kernel_size=(3, 3),
#     #                  activation='relu',
#     #                  input_shape=(3, 25, 25)))
#     # model.add(Conv2D(64, (3, 3), activation='relu'))
#     # model.add(MaxPooling2D(pool_size=(2, 2)))
#     # model.add(Dropout(0.25))
#     model.add(Flatten())
#     model.add(Dense(128, activation='relu'))
#     model.add(Dropout(0.5))
#     model.add(Dense(Activation='softmax'))

#     return model

image_list = []
label_list = []

for dir in os.listdir("data/train"):
  if dir == ".DS_Store":
    continue

  dir1 = "data/train/" + dir
  label = 0

  if dir == "orion": #onionのlabel = 0
    label = 0
  elif dir == "carot": #carotのlabel = 0
    label = 1
  else:
    continue
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
      print(image.shape)
      image = image.transpose(2,0,1)
      #さらにフラットな1次元配列に変換、最初の1/3がred,次がgreen、最後がblueの要素がフラットに並ぶ
      print(image.shape)
      image = image.reshape(1,image.shape[0] * image.shape[1] * image.shape[2]).astype("float32")[0]
      #配列をimage_listに保存する
      print(image.shape)
      image_list.append(image/255.)

# kerasに渡すためにnumpy配列に変換
image_list = np.array(image_list)
print(image_list.shape)
# 0 -> [1,0], 1 -> [0,1] という感じ。
#ラベルの配列を1と0からなるラベル配列に変換する
Y = to_categorical(label_list)
print(Y.shape)
model = multi_layer_perceptron()
#optimizer → Adamを使用
opt = Adam(lr=0.001)
#compiling model
# マルチクラス分類問題の場合
model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])
model.compile(loss="categorical_crossentropy",optimizer=opt,metrics=["accuracy"])
#学習の実行
# epochs 繰り返し学習させる回数
model.fit(image_list,Y,nb_epoch=1500,batch_size = 100,validation_split=0.1)

#テスト用ディレクトリ(./data/train/)の画像でチェック、正答率を表示する
total = 0
ok_count = 0

for dir in os.listdir("data/test"):
  if dir == ".DS_Store":
    continue

  dir2 = "data/test/" + dir
  label = 0

  if dir == "onion":
    label = 0
  elif dir == "carot":
    label = 1

  for file in os.listdir(dir2):
    if file != ".DS_Store":
      label_list.append(label)
      filepath = dir2 + "/" + file
      image = np.array(Image.open(filepath).resize((25,25)))
      print(filepath)
      image = image.transpose(2,0,1)
      image = image.reshape(1,image.shape[0] * image.shape[1] * image.shape[2]).astype("float32")[0]
      result = model.predict_classes(np.array([image/255.]))
      print("label:",label,"result",result[0])

      total += 1.

      if label == result[0]:
        ok_count += 1.

print("seikai:",ok_count / total * 100,"%")
