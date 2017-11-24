# 学習済モデルの作成

#kerasを使用

N_CATEFORIES  = 3
IMAGE_SIZE = 224
BATCH_SIZE = 16

NUM_TRAINING = 1600
NUM_VALIDATION = 400

input_tensor = Input(shape = (IMAGE_SIZE,IMAGE_SIZE,3))
base_model = VGG16(weights = 'imagenet',include_top=False,input_tensor=input_tensor)


x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024,activation='relu')(x)

prediction = Dense(N_CATEFORIES,activation='softmax')(x)
model = Model(input=base_model.input,outputs=predictions)

for layer in base_model.layers:
  layer.trainable = False

from keras.optimizers import SGD
model.compile(optimizer=SGD(lr=0.0001,momentum=0.9),loss='categorial_crossent')
