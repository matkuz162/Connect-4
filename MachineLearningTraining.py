import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

file_path = "Data\connect-4.data"
column_names = [f"pos_{i}" for i in range(42)] + ["outcome"]
df = pd.read_csv(file_path, names=column_names)

conversion = {'x': 1, 'o': -1, 'b': 0}
for col in df.columns[:-1]:
    df[col] = df[col].map(conversion)

label_encoder = LabelEncoder()
df['outcome'] = label_encoder.fit_transform(df['outcome'])

X = df.drop("outcome", axis=1)
y = df["outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)

joblib.dump(knn_model, "machine_learning_model.joblib")
joblib.dump(label_encoder, "machine_learning_label_encoder_y.joblib")
print("Model and label encoder saved.")