# imporr library yg diperlukan
import numpy as np #untuk mengolah data
import pandas as pd #untuk mengolah data
import matplotlib.pyplot  as plt #untuk menampilkan gambar/ grafik visual
import seaborn as sns #untuk menampilkan gambar/ grafik visual
from sklearn.model_selection import train_test_split #libarry machine learning, dipakai untuk membuat model regresi linear dan evaluasi
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# membuat data

data = {
    "Luas_Kamar" : [12, 15, 18, 20, 22, 25, 30],
    "Harga_Sewa" : [250, 275, 310, 350, 370, 410, 480]
}
datas = data
df = pd.DataFrame(datas)

#ekspolrasi data(memviusualisasikan data) 
sns.scatterplot(data=df, x = "Jumlah_Iklan", y = "Jumlah_Pembeli")
plt.title('Jumlah iklan dengan jumlah pembeli')

# persiapan data
x = df[['Luas_Kamar']] #features
y = df['Harga_Sewa'] #target

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 42)

# membangun model
model = LinearRegression()
model.fit(x_train, y_train)

#evaluasi model

y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error {mse}")

# visualisasi hasil
plt.scatter(x, y, color= 'blue')
plt.plot(x, model.predict(x), color= 'brown')
plt.title('Linear Regression')
plt.xlabel('Luas kamar')
plt.ylabel('Harga sewa')

