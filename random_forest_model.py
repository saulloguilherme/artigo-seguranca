from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def model_v1() -> RandomForestClassifier:
    dataBase = pd.read_csv('datasets/data_base.csv', sep=',')
    X, y = dataBase.drop(['phishing', 'url'], axis=1), dataBase['phishing']
    X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=910)
    rf = RandomForestClassifier(max_depth=10, min_samples_split=10, min_samples_leaf=4, n_estimators=100, max_features='sqrt', min_impurity_decrease=0.001, bootstrap=True)
    rf.fit(X_treino, y_treino)

    return rf

def model_v2() -> RandomForestClassifier:
    dataset_Souza = pd.read_csv('datasets/dataset_Souza.csv', sep=',')
    X, y = dataset_Souza.drop(['phishing', 'url'], axis=1), dataset_Souza['phishing']
    X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=910)
    rf = RandomForestClassifier(max_depth=10, min_samples_split=10, min_samples_leaf=4, n_estimators=100, max_features='sqrt', min_impurity_decrease=0.001, bootstrap=True)
    rf.fit(X_treino, y_treino)

    return rf