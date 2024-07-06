from data_handling import load_and_preprocess_data
from model_building import (
    train_linear_regression, train_decision_tree, evaluate_model,
    train_logistic_regression, train_svm_classifier, train_svm_regressor,
    train_random_forest_classifier, train_random_forest_regressor,
    train_knn_classifier, train_knn_regressor, train_mlp_classifier,
    train_mlp_regressor, train_gradient_boosting_classifier,
    train_gradient_boosting_regressor
)

def main():
    X_train, X_test, y_train, y_test = load_and_preprocess_data()

    print("Welcome to the Machine Learning Model Builder")
    print("1. Train Linear Regression")
    print("2. Train Decision Tree")
    print("3. Train Logistic Regression")
    print("4. Train SVM Classifier")
    print("5. Train SVM Regressor")
    print("6. Train Random Forest Classifier")
    print("7. Train Random Forest Regressor")
    print("8. Train KNN Classifier")
    print("9. Train KNN Regressor")
    print("10. Train MLP Classifier")
    print("11. Train MLP Regressor")
    print("12. Train Gradient Boosting Classifier")
    print("13. Train Gradient Boosting Regressor")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        model = train_linear_regression(X_train, y_train)
        mse = evaluate_model(model, X_test, y_test, model_type='regression')
        print(f"Linear Regression Model Mean Squared Error: {mse}")
    elif choice == '2':
        model = train_decision_tree(X_train, y_train)
        accuracy = evaluate_model(model, X_test, y_test, model_type='classification')
        print(f"Decision Tree Model Accuracy: {accuracy}")
    elif choice == '3':
        model = train_logistic_regression(X_train, y_train)
        accuracy = evaluate_model(model, X_test, y_test, model_type='classification')
        print(f"Logistic Regression Model Accuracy: {accuracy}")
    elif choice == '4':
        model = train_svm_classifier(X_train, y_train)
        accuracy = evaluate_model(model, X_test, y_test, model_type='classification')
        print(f"SVM Classifier Model Accuracy: {accuracy}")
    elif choice == '5':
        model = train_svm_regressor(X_train, y_train)
        mse = evaluate_model(model, X_test, y_test, model_type='regression')
        print(f"SVM Regressor Model Mean Squared Error: {mse}")
    elif choice == '6':
        model = train_random_forest_classifier(X_train, y_train)
        accuracy = evaluate_model(model, X_test, y_test, model_type='classification')
        print(f"Random Forest Classifier Model Accuracy: {accuracy}")
    elif choice == '7':
        model = train_random_forest_regressor(X_train, y_train)
        mse = evaluate_model(model, X_test, y_test, model_type='regression')
        print(f"Random Forest Regressor Model Mean Squared Error: {mse}")
    elif choice == '8':
        model = train_knn_classifier(X_train, y_train)
        accuracy = evaluate_model(model, X_test, y_test, model_type='classification')
        print(f"KNN Classifier Model Accuracy: {accuracy}")
    elif choice == '9':
        model = train_knn_regressor(X_train, y_train)
        mse = evaluate_model(model, X_test, y_test, model_type='regression')
        print(f"KNN Regressor Model Mean Squared Error: {mse}")
    elif choice == '10':
        model = train_mlp_classifier(X_train, y_train)
        accuracy = evaluate_model(model, X_test, y_test, model_type='classification')
        print(f"MLP Classifier Model Accuracy: {accuracy}")
    elif choice == '11':
        model = train_mlp_regressor(X_train, y_train)
        mse = evaluate_model(model, X_test, y_test, model_type='regression')
        print(f"MLP Regressor Model Mean Squared Error: {mse}")
    elif choice == '12':
        model = train_gradient_boosting_classifier(X_train, y_train)
        accuracy = evaluate_model(model, X_test, y_test, model_type='classification')
        print(f"Gradient Boosting Classifier Model Accuracy: {accuracy}")
    elif choice == '13':
        model = train_gradient_boosting_regressor(X_train, y_train)
        mse = evaluate_model(model, X_test, y_test, model_type='regression')
        print(f"Gradient Boosting Regressor Model Mean Squared Error: {mse}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
