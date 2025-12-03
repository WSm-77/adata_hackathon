train_data = pd.read_csv("bit-x-adata/train.csv")
train_data.drop(columns=["id"], inplace=True)
train_data[["święto", "dzień_roboczy"]] = train_data[["święto", "dzień_roboczy"]].astype(int)
train_data[['year', 'month', 'day']] = train_data['data'].str.split('-', expand=True).astype(int)
train_data.drop("data", axis=1, inplace=True)

train_data_with_dummies = pd.get_dummies(train_data, columns=['pogoda'], dtype=int)

X = train_data_with_dummies.drop("studenty_ms", axis=1)
Y = train_data_with_dummies["studenty_ms"]

X = train_data_with_dummies.drop("studenty_ms", axis=1).values
Y = train_data_with_dummies["studenty_ms"].values.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
