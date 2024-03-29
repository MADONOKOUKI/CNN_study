from keras.models import Sequential
from keras.layers import Activation,Dense,Dropout
from np_utils import to_categorical
from keras.utils import np_utils
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

  model.add(Dense(5)) #出力層4ノード,全結合している
  model.add(Activation("softmax"))

  return model

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
  elif dir == "potato":
    label = 2
  elif dir == "CurryPowder":
    label = 3
  else:
    label = 4
  for file in os.listdir(dir1):
    if file != ".DS_Store":
      # 配列label_listに正解ラベルを追加(りんご:0 オレンジ:1)
      label_list.append(label)
      filepath = dir1 + "/" + file
      # 画像を25x25pixelに変換し、1要素が[R,G,B]3要素を含む配列の25x25の２次元配列として読み込む。
      # [R,G,B]はそれぞれが0-255の配列。
      image = np.array(Image.open(filepath).resize((25,25)))
      # print(filepath)
      print(image.shape,image.dtype) # (行数、列数、色数) / データタイプ
      # 配列を変換し、[[Redの配列],[Greenの配列],[Blueの配列]] のような形にする。
      image = image.transpose(2,0,1)
      #さらにフラットな1次元配列に変換、最初の1/3がred,次がgreen、最後がblueの要素がフラットに並ぶ
      print(image)
      print(image.shape)
      print(image.shape[0],image.shape[1],image.shape[2])
      print(image.reshape(1,image.shape[0] * image.shape[1] * image.shape[2]).astype("float32"))
      #横一直線にして、最後に外側の配列を外している
      image = image.reshape(1,image.shape[0] * image.shape[1] * image.shape[2]).astype("float32")[0]
      #配列をimage_listに保存する
      print(image)
      #輝度は0-255で表現するので、255のfloat型で割って、正規化している
      image_list.append(image/255.)
      print(image/255.)

# kerasに渡すためにnumpy配列に変換
image_list = np.array(image_list)
print(image_list.shape)
# 0 -> [1,0], 1 -> [0,1] という感じ。
#ラベルの配列を1と0からなるラベル配列に変換する
Y = to_categorical(label_list)
# Y = np_utils.to_categorical(label_list)
print(Y.shape,Y.dtype)
model = multi_layer_perceptron()
# model.summary()
#optimizer → Adamを使用
opt = Adam(lr=0.001)
#compiling model
model.compile(loss="binary_crossentropy",optimizer=opt,metrics=["accuracy"])
#学習の実行
# epochs 繰り返し学習させる回数
model.fit(image_list,Y,nb_epoch=1500,batch_size = 100,validation_split=0.1)

# model.save('vegitable.hdf5')
# #テスト用ディレクトリ(./data/train/)の画像でチェック、正答率を表示する
# total = 0
ok_count = 0

test_label = []
for file in os.listdir("refrigerator_of_food"):
  if file == ".DS_Store":
    continue
  file = "refrigerator_of_food/" + file
  image=  np.array(Image.open(file).resize((25,25)))
  print(file)
  image = image.transpose(2,0,1)
  image = image.reshape(1,image.shape[0] * image.shape[1] * image.shape[2]).astype("float32")[0]
  result = model.predict_classes(np.array([image/255.]))
  print("result",result[0])
  print("reuslt_detail",result)
  test_label.append(result[0])
test_label = sorted(test_label)
for i in range(0,3):
  for j in range(0,len(test_label)):
    if test_label[j] == i:
      ok_count+=1
      break
if(ok_count >=4):
  print("カレーの食材が揃っています")
else:
  print("カレーの食材が揃っていません")
