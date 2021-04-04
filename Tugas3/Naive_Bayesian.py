# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:23:29 2021

@author: ACER
"""
import pandas as pd
import numpy as np
caesarian = pd.read_csv("caesarian.txt")
caesarian.head()
#%%
# Variabel independen
x = caesarian.drop(["Caesarian"], axis = 1)
x.head()
#%%
# Variabel dependen
y = caesarian["Caesarian"]
y.head()
#%%
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 123)
#%%
from sklearn.naive_bayes import GaussianNB
# Mengaktifkan/memanggil/membuat fungsi klasifikasi Naive Bayes
modelnb = GaussianNB()
# Memasukkan data training pada fungsi klasifikasi Naive Bayes
nbtrain = modelnb.fit(x_train, y_train)
#%%
# Menentukan hasil prediksi dari x_test
y_pred = nbtrain.predict(x_test)
y_pred
#%%
np.array(y_test)
#%%
# Menentukan probabilitas hasil prediksi
nbtrain.predict_proba(x_test)
#%%
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)
#%%
# Merapikan hasil confusion matrix
y_actual = pd.Series([0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0], name = "actual")
y_pred = pd.Series([1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0], name = "prediction")
df_confusion = pd.crosstab(y_actual, y_pred)
#%%
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

