import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Function to impute missing values
# Supports 'mean', 'median', or 'mode' for numerical columns
# Uses 'mode' for categorical columns

def impute_missing_values(data, strategy='mean'):
    """
    Fill missing values in the dataset, except for the target column.
    """
    for col in data.columns:
        if col == 'target':
            continue  # Skip target column to avoid changing class labels
        if data[col].dtype in ['int64', 'float64']:
            if strategy == 'mean':
                data[col].fillna(data[col].mean(), inplace=True)
            elif strategy == 'median':
                data[col].fillna(data[col].median(), inplace=True)
            elif strategy == 'mode':
                data[col].fillna(data[col].mode()[0], inplace=True)
        elif data[col].dtype == 'object':
            data[col].fillna(data[col].mode()[0], inplace=True)
    return data

# Function to remove duplicate rows from the dataset
def remove_duplicates(data):
    """
    Remove duplicate rows from the dataset.
    """
    return data.drop_duplicates()

# Function to normalize numerical data
# Supports 'minmax' scaling (default) or 'standard' scaling
def normalize_data(data, method='minmax'):
    """
    Apply normalization to numerical features.
    """
    numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
    scaler = MinMaxScaler() if method == 'minmax' else StandardScaler()
    data[numerical_columns] = scaler.fit_transform(data[numerical_columns])
    return data

# Function to remove redundant features based on correlation
def remove_redundant_features(data, threshold=0.9):
    """
    Remove redundant numerical columns based on correlation.
    """
    numeric_data = data.select_dtypes(include=['number'])
    if numeric_data.shape[1] < 2:
        return data  # Not enough numeric columns for correlation analysis
    
    corr_matrix = numeric_data.corr().abs()
    upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > threshold)]
    return data.drop(columns=to_drop)

# Function to train a simple logistic regression model
def simple_model(input_data, split_data=True, scale_data=False, print_report=False):
    """
    Train a logistic regression model for binary classification.
    """
    input_data.dropna(subset=['target'], inplace=True)  # Remove rows with missing target values
    target = input_data.iloc[:, 0]
    features = input_data.iloc[:, 1:]

    for col in features.columns:
        if features[col].dtype == 'object':
            features = pd.get_dummies(features, columns=[col])
    
    if split_data:
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, stratify=target, random_state=42)
    else:
        X_train, X_test, y_train, y_test = features, features, target, target
    
    if scale_data:
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
    
    model = LogisticRegression(random_state=42, max_iter=100, solver='liblinear', penalty='l2', C=1.0)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    print(f'Accuracy: {accuracy}')
    if print_report:
        print('Classification Report:\n', report)
    
    return model

# ---------------------------------------------------
# Test the Preprocessing Functions
# ---------------------------------------------------

# # Create a sample dataset for testing the functions
# test_data = pd.DataFrame({
#     'A': [1, 2, np.nan, 2, 1, 5, 6, 7, 8, 9],  # Numeric with missing values
#     'B': [1, 2, 3, 2, 1, 5, 6, 7, 8, 9],       # Numeric (potential redundancy)
#     'C': ['cat', 'dog', 'cat', 'dog', np.nan, 'dog', 'cat', 'dog', 'cat', 'dog'],  # Categorical with missing
#     'D': [10, 20, 30, 20, 10, 50, 60, 70, 80, 90],  # Numeric (potential redundancy)
#     'target': [0, 1, 1, 0, 0, 1, 1, 0, 0, 1]  # Binary target variable
# })

# # Display original test data
# print("Original Test Data:")
# print(test_data)

# # Apply each function step-by-step and display results
# test_data = impute_missing_values(test_data, strategy='mean')
# print("\nAfter Imputing Missing Values:")
# print(test_data)

# test_data = remove_duplicates(test_data)
# print("\nAfter Removing Duplicates:")
# print(test_data)

# test_data = normalize_data(test_data, method='minmax')
# print("\nAfter Normalizing Numerical Data:")
# print(test_data)

# test_data = remove_redundant_features(test_data, threshold=0.9)
# print("\nAfter Removing Redundant Features:")
# print(test_data)

# # Save the cleaned dataset
# test_data.to_csv('cleaned_test_data.csv', index=False)
# print("\nCleaned dataset saved to 'cleaned_test_data.csv'.")