import pandas as pd

dataset = pd.read_csv('item-purchase-data.csv')
X = dataset.iloc[:1000, 3:7].values
y = dataset.iloc[:1000, 7].values

from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
X[:, 2] = enc.fit_transform(X[:, 2])

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from keras.models import Sequential
from keras.layers import Dense

from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV
def build_classifier(optimizer):
    classifiers = Sequential()
    classifiers.add(Dense(units=4, kernel_initializer='uniform', activation='relu'))
    classifiers.add(Dense(units=3, kernel_initializer='uniform', activation='relu'))
    classifiers.add(Dense(units=3, kernel_initializer='uniform', activation='relu'))
    classifiers.add(Dense(units=3, kernel_initializer='uniform', activation='relu'))
    classifiers.add(Dense(units=3, kernel_initializer='uniform', activation='relu'))
    classifiers.add(Dense(units=3, kernel_initializer='uniform', activation='relu'))
    classifiers.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))
    classifiers.compile(optimizer = optimizer, loss='binary_crossentropy', metrics=['accuracy'])
    return classifiers

classifiers = KerasClassifier(build_fn = build_classifier)
parameters = {'batch_size': [25, 32], 'epochs': [100, 500], 'optimizer': ['adam', 'rmsprop', 'sgd'] }
gridSearch = GridSearchCV(estimator = classifiers, param_grid=parameters, scoring='accuracy', n_jobs=1, cv=10)
gridSearch = gridSearch.fit(X_train, y_train)
params = gridSearch.best_params_
estimate = gridSearch.best_estimator_
index = gridSearch.best_index_
score = gridSearch.best_score_
