#imports
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

#loads dataset
file_path = "Data\connect-4.data"
column_names = [f"pos_{i}" for i in range(42)] + ["outcome"] # 6x 7 = 42 total positions
df = pd.read_csv(file_path, names=column_names)

#converts dataset to numerical
#x=player1, o=player2, b=blank tile
conversion = {'x': 1, 'o': -1, 'b': 0}
for col in df.columns[:-1]:
    df[col] = df[col].map(conversion)

#encodes to numeric classes
label_encoder = LabelEncoder()
df['outcome'] = label_encoder.fit_transform(df['outcome'])

#splits dataset into x and y
X = df.drop("outcome", axis=1)
y = df["outcome"]

#splits dataset into 80% training and 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)

#save trained model
joblib.dump(knn_model, "machine_learning_model.joblib")
joblib.dump(label_encoder, "machine_learning_label_encoder_y.joblib")
print("Model and label encoder saved.")