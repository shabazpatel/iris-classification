# data handling
import os
import sys
import json
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# nearest neighbors
from sklearn.neighbors import KNeighborsClassifier

# naive bayes
from sklearn.naive_bayes import GaussianNB

# measures
from sklearn.metrics import accuracy_score
import timeit


# read the csv file
print("Loading data")
iris = pd.read_csv('Iris.csv', index_col='Id')

# get X,y data
X = iris.as_matrix(iris.columns[0:-1])

lenc = LabelEncoder()
y = iris['Species'].as_matrix()
y = lenc.fit_transform(y)

# shuffle and split into train and test sets
print("Splitting data into train and test set")
X_train, X_test, y_train, y_test = train_test_split(X, y)

ohenc = OneHotEncoder()
ohenc.fit(y.reshape((-1, 1)))
y_train_oh = ohenc.transform(y_train.reshape((-1, 1))).toarray()
y_test_oh = ohenc.transform(y_test.reshape((-1, 1))).toarray()

with open(os.environ['INPUT_DIR']+'/config.json') as f:
     config_dict = json.load(f)

# Selecting type of model based on configuration
if config_dict['algorithm'] == 'KNeighbors':
    model = KNeighborsClassifier()
elif config_dict['algorithm'] == 'GaussianNB':
    model = GaussianNB() 
else:
    sys.exit()

def fn():
    model.fit(X_train, y_train)

t = timeit.timeit(fn, number=1)

y_pred = model.predict(X_test)
y_pred = [round(value) for value in y_pred]
accuracy = accuracy_score(y_test, y_pred)

stats = {'training_time': t, 'accuracy': accuracy}
print("stats:", stats)

# saving model file
model_filename = os.path.join(os.environ['OUTPUT_DIR'], 'model.dat')
pickle.dump(model, open(model_filename, 'wb'))
# saving stats file
stats_filename = os.path.join(os.environ['OUTPUT_DIR'],'stats.json')
with open(stats_filename, 'w') as f:
    f.write(json.dumps(stats))
