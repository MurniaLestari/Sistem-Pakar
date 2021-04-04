# Sistem-Pakar
#%% Nama : Murnia Lestari
#%% NPM :1184006
#%% Kelas : D4 TI 3C

# Pada Persoalan kali ini kita akan menggunakan Algoritma Naive Bayesian yang digunakan untuk mengklasifikasikan peluang terjadinya sesuatu berdasarkan data yang dimiliki. sebelumnya.
# Persoalan yang akan kita klasifikasikan dengan Algoritma Naive Bayesian yaitu mengenai Operasi Caesar yang saya dapatkan dari situs (https://medium.com/@kurniasp/naive-bayes-classifier-using-scikit-learn-in-python-3067144af115)
# Dataset yang digunakan yaitu caesarian.csv yang didapatkan dari (http://archive.ics.uci.edu/ml/datasets/Caesarian+Section+Classification+Dataset)
# Data set ini memiliki 6 attrbute yaitu age, delivery number, delivery time, blood pressure , heart status,dan Caesarian.
# Label yang digunakan adalah Caesarian. label ini akan digunakan untuk memprediksi apakah seseorang atau ibu hamil harus dioperasi caesar atau tidak dengan melihat attribute yang ada seperti umur,tekanan darah, dan riwayat jantung yang dimiliki.
# Hasil prediksi dari Algoritma Naive Bayesian ini akan menghasilkan bernilai 1 dan 0. Jika bernilai 1 maka ibu hamil harus menjalani operasi caesar ,namun jika bernilai satu maka ibu hamil tidak harus melakukan operasi caesar.


#%%

import pandas as pd
# digunakan untuk mengimport library pandas
import numpy as np
# digunakan untuk mengimport library numpy
caesarian = pd.read_csv("caesarian.txt")
# digunakan untuk membaca data dari data set caesarian.txt
caesarian.head()
# digunakan digunakan untuk menampilkan data tertas pada dataset
#%%
# Variabel independen
x = caesarian.drop(["Caesarian"], axis = 1)
# digunakan untuk menghapus attribute caesarian
x.head()
# menampilkan data dari variabel independen
#%%
# Variabel dependen
y = caesarian["Caesarian"]
# digunakan untuk mepresentasikan variabel dependen yaitu caesarian yang digunakan untuk menunjukan apakah seseorang perlu di operasi caesar atau tidak.
y.head()
# menampilkan data dari variabel y
#%%
from sklearn.model_selection import train_test_split
# mengimport library train_test split dari library sklearn,mode_selection
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 123)
#  digunakan untuk mempresetasikan variabel training dan testing
#%%
from sklearn.naive_bayes import GaussianNB
# Mengaktifkan/memanggil/membuat fungsi klasifikasi Naive Bayes
modelnb = GaussianNB()
# Memasukkan data training pada fungsi klasifikasi Naive Bayes
nbtrain = modelnb.fit(x_train, y_train)
# melakukan proses training 
#%%
# Menentukan hasil prediksi dari x_test
y_pred = nbtrain.predict(x_test)
#mempresentasikan hasil dari prediksi
y_pred
#%%
np.array(y_test)
# mempresentasikan hasil aktualnya y_test
#%%
# Menentukan probabilitas hasil prediksi
nbtrain.predict_proba(x_test)
#%%
from sklearn.metrics import confusion_matrix
# mengimport library confusion_matrix
confusion_matrix(y_test, y_pred)
# mempresentasikan confussiona_matrix dari t_test dan y_pred
#%%
# Merapikan hasil confusion matrix
y_actual = pd.Series([0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0], name = "actual")
y_pred = pd.Series([1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0], name = "prediction")
df_confusion = pd.crosstab(y_actual, y_pred)
# mempresentasikan hasil prediksi dan aktual dalam berbentuk cross tab
#%%
from sklearn.metrics import classification_report
# mengimport library classification_report dari sklearn_metrics
print(classification_report(y_test, y_pred))
# mencetak hasil dari prediksi

# Hasil dari Naive Bayesian ini menunjukan apabila ada ibu hamil yang melahirkan secara normal sesuai dengan kenyataannya,namun terdapat ibu hamil yang dipredksi melahirkan secara normal namun caesar. Selanjutnya terdapat ibu hamil yang diprediksi melahirkan secara caesar namun kenyataannya melahirkan secara normal,namun ada juga yang diprediksi melahirkan caesar dengan kenytaannya juga melahirkan secara caesar.
# dan hal tersebut diprediksi yang ditunjukan dengan angka 1 dan 0. jika 1 maka caesar jika 0 maka normal.
