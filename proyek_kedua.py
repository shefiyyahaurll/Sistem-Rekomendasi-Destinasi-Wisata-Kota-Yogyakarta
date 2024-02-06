import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

destination_rating = pd.read_csv('dataset/tourism_rating.csv')
destination = pd.read_csv('dataset/tourism_with_id.csv')
user = pd.read_csv('dataset/user.csv')

destination = destination.drop(destination[['Unnamed: 11','Unnamed: 12', 'Time_Minutes']], axis=1)
merge_destination = pd.merge(destination_rating, destination, how='left', left_on='Place_Id', right_on='Place_Id')
merge_destination = merge_destination[merge_destination['City']=='Yogyakarta']

top_10 = merge_destination['Place_Name'].value_counts().reset_index(name='Count')[0:10]
# Membuat dictionary untuk data ‘Place_Id’, 'Place_Name’, dan ‘Category’
destination_new = pd.DataFrame({
    'id': merge_destination['Place_Id'],
    'Place_Name': merge_destination['Place_Name'],
    'Category': merge_destination['Category']
})
# Membuang data duplikat pada variabel preparation
preparation = destination_new.drop_duplicates('id')
data = preparation
from sklearn.feature_extraction.text import TfidfVectorizer
 
# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()
 
# Melakukan perhitungan idf pada data cuisine
tf.fit(data['Category']) 
 
# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out() 
# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(data['Category']) 
 
# Melihat ukuran matrix tfidf
tfidf_matrix.shape 
# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()
from sklearn.metrics.pairwise import cosine_similarity
 
# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix) 
# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama resto
cosine_sim_df = pd.DataFrame(cosine_sim, index=data['Place_Name'], columns=data['Place_Name'])
print('Shape:', cosine_sim_df.shape)
 
# Melihat similarity matrix pada setiap resto
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)
def place_recommendations(nama_tempat, similarity_data=cosine_sim_df, items=data[['Place_Name', 'Category']], k=5):
    """
    Rekomendasi Resto berdasarkan kemiripan dataframe
 
    Parameter:
    ---
    nama_tempat : tipe data string (str)
                Nama tempat (index kemiripan dataframe)
    similarity_data : tipe data pd.DataFrame (object)
                      Kesamaan dataframe, simetrik, dengan resto sebagai 
                      indeks dan kolom
    items : tipe data pd.DataFrame (object)
            Mengandung kedua nama dan fitur lainnya yang digunakan untuk mendefinisikan kemiripan
    k : tipe data integer (int)
        Banyaknya jumlah rekomendasi yang diberikan
    ---
 
 
    Pada index ini, kita mengambil k dengan nilai similarity terbesar 
    pada index matrix yang diberikan (i).
    """
 
 
    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan    
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,nama_tempat].to_numpy().argpartition(
        range(-1, -k, -1))
    
    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    
    # Drop nama_resto agar nama resto yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(nama_tempat, errors='ignore')
 
    return pd.DataFrame(closest).merge(items).head(k)

data[data.Place_Name.eq('Pantai Kesirat')]

# Mendapatkan rekomendasi restoran yang mirip dengan Pantai Kesirat
place_recommendations('Pantai Kesirat')

# Import library
import pandas as pd
import numpy as np 
from zipfile import ZipFile
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from pathlib import Path
import matplotlib.pyplot as plt

# Membaca dataset
 
df = destination_rating

# Mengubah userID menjadi list tanpa nilai yang sama
user_ids = df['User_Id'].unique().tolist()
print('list 	User_Id: ', user_ids)
 
# Melakukan encoding userID
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded 	User_Id: ', user_to_user_encoded)
 
# Melakukan proses encoding angka ke ke userID
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded angka ke User_Id: ', user_encoded_to_user)

# Mengubah placeID menjadi list tanpa nilai yang sama
Place_Id_ids = df['Place_Id'].unique().tolist()
 
# Melakukan proses encoding placeID
Place_Id_to_place_encoded = {x: i for i, x in enumerate(Place_Id_ids)}
 
# Melakukan proses encoding angka ke placeID
Place_Id_encoded_to_place = {i: x for i, x in enumerate(Place_Id_ids)}

# Mapping userID ke dataframe user
df['user'] = df['User_Id'].map(user_to_user_encoded)
 
# Mapping placeID ke dataframe tempat wisata
df['tempat_wisata'] = df['Place_Id'].map(Place_Id_to_place_encoded)

# Mendapatkan jumlah user
num_users = len(user_to_user_encoded)
print(num_users)
 
# Mendapatkan jumlah tempat wisata
num_place = len(Place_Id_encoded_to_place)
print(num_place)
 
# Mengubah rating menjadi nilai float
df['Place_Ratings'] = df['Place_Ratings'].values.astype(np.float32)
 
# Nilai minimum rating
min_rating = min(df['Place_Ratings'])
 
# Nilai maksimal rating
max_rating = max(df['Place_Ratings'])
 
print('Number of User: {}, Number of Place: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_place, min_rating, max_rating
))

# Membuat variabel x untuk mencocokkan data user dan tempat wisata menjadi satu value
x = df[['user', 'tempat_wisata']].values
 
# Membuat variabel y untuk membuat rating dari hasil 
y = df['Place_Ratings'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values
 
# Membagi menjadi 80% data train dan 20% data validasi
train_indices = int(0.8 * df.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)
 
print(x, y)

class RecommenderNet(tf.keras.Model):
 
  # Insialisasi fungsi
  def __init__(self, num_users, num_place, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_place = num_place
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding( # layer embedding user
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1) # layer embedding user bias
    self.place_embedding = layers.Embedding( # layer embeddings resto
        num_place,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.place_bias = layers.Embedding(num_place, 1) # layer embedding resto bias
 
  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    resto_vector = self.place_embedding(inputs[:, 1]) # memanggil layer embedding 3
    place_bias = self.place_bias(inputs[:, 1]) # memanggil layer embedding 4
 
    dot_user_resto = tf.tensordot(user_vector, resto_vector, 2) 
 
    x = dot_user_resto + user_bias + place_bias
    
    return tf.nn.sigmoid(x) # activation sigmoid

model = RecommenderNet(num_users, num_place, 100) # inisialisasi model

# model compile
model.compile(
    loss=tf.keras.losses.MeanSquaredError(),
    optimizer=keras.optimizers.Adam(learning_rate=0.0001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

# Memulai training
early_stopping_loss = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True
)

early_stopping_rmse = tf.keras.callbacks.EarlyStopping(
    monitor='val_root_mean_squared_error',
    patience=20,
    restore_best_weights=True
)

history = model.fit(
    x=x_train,
    y=y_train,
    batch_size=16,
    epochs=150,
    validation_data=(x_val, y_val),
    callbacks=[early_stopping_loss, early_stopping_rmse]
)

