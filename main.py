# coding=utf-8

# from keras.callbacks import EarlyStopping
from keras.preprocessing import sequence
from sklearn.cross_validation import train_test_split
from BiLSTM import TextBiRNN
import pandas as pd

max_features = 5000
maxlen = 10
batch_size = 32
embedding_dims = 50
epochs = 10

print('Loading data...')
# 划分训练集和测试集，此时都是list列表
data = pd.read_csv('file.csv',sep='\t')
allsentences = data[1]
labels = data[2]
x_train, x_test, y_train, y_test = train_test_split(allsentences, labels, test_size=0.3)
# (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
print(len(x_train), 'train sequences')
print(len(x_test), 'test sequences')

print('Pad sequences (samples x time)...')
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)

print('Build model...')
model = TextBiRNN(maxlen, max_features, embedding_dims).get_model()
model.compile('adam', 'binary_crossentropy', metrics=['accuracy'])

print('Train...')
# early_stopping = EarlyStopping(monitor='val_acc', patience=3, mode='max')
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          # callbacks=[early_stopping],
          validation_data=(x_test, y_test))

print('Test...')
result = model.predict(x_test)