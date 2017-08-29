# data handling
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# nearest neighbors
from sklearn.neighbors import KNeighborsClassifier

# measures
from sklearn.metrics import accuracy_score
import timeit


# read the csv file
iris = pd.read_csv('Iris.csv', index_col='Id')

# get X,y data
X = iris.as_matrix(iris.columns[0:-1])

lenc = LabelEncoder()
y = iris['Species'].as_matrix()
y = lenc.fit_transform(y)

# shuffle and split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y)

ohenc = OneHotEncoder()
ohenc.fit(y.reshape((-1, 1)))
y_train_oh = ohenc.transform(y_train.reshape((-1, 1))).toarray()
y_test_oh = ohenc.transform(y_test.reshape((-1, 1))).toarray()

model_type = 'KNeighbors'
if model_type == 'KNeighbors':
    model = KNeighborsClassifier()
elif model_type == 'GaussianNB':
    model = GaussianNB() 
else:
    continue

def fn():
    model.fit(X_train, y_train)

t = timeit.timeit(fn, number=1)

y_pred = model.predict(X_test)
y_pred = [round(value) for value in y_pred]
accuracy = accuracy_score(y_test, y_pred)

config['algorithm'] = model_type
stats = {'training_time': t, 'accuracy': accuracy}
print(stats)
