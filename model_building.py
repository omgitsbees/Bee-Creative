from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, SVR
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.neural_network import MLPClassifier, MLPRegressor

def train_logistic_regression(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def train_svm_classifier(X_train, y_train):
    model = SVC()
    model.fit(X_train, y_train)
    return model

def train_svm_regressor(X_train, y_train):
    model = SVR()
    model.fit(X_train, y_train)
    return model

def train_random_forest_classifier(X_train, y_train):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def train_random_forest_regressor(X_train, y_train):
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model

def train_knn_classifier(X_train, y_train):
    model = KNeighborsClassifier()
    model.fit(X_train, y_train)
    return model

def train_knn_regressor(X_train, y_train):
    model = KNeighborsRegressor()
    model.fit(X_train, y_train)
    return model

def train_mlp_classifier(X_train, y_train):
    model = MLPClassifier()
    model.fit(X_train, y_train)
    return model

def train_mlp_regressor(X_train, y_train):
    model = MLPRegressor()
    model.fit(X_train, y_train)
    return model

def train_gradient_boosting_classifier(X_train, y_train):
    model = GradientBoostingClassifier()
    model.fit(X_train, y_train)
    return model

def train_gradient_boosting_regressor(X_train, y_train):
    model = GradientBoostingRegressor()
    model.fit(X_train, y_train)
    return model
