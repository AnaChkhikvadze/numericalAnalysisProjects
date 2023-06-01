import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Generate a sample dataset
data = np.random.rand(100, 10)
labels = np.random.randint(0, 2, 100)

# Split the dataset into training and testing sets
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=0.2, random_state=42)

# Define machine learning algorithms
logistic_regression = LogisticRegression()
decision_tree = DecisionTreeClassifier()
random_forest = RandomForestClassifier()

# Train and evaluate each algorithm
logistic_regression.fit(train_data, train_labels)
logistic_regression_predictions = logistic_regression.predict(test_data)
logistic_regression_accuracy = accuracy_score(test_labels, logistic_regression_predictions)
print(f"Logistic Regression Accuracy: {logistic_regression_accuracy:.4f}")

decision_tree.fit(train_data, train_labels)
decision_tree_predictions = decision_tree.predict(test_data)
decision_tree_accuracy = accuracy_score(test_labels, decision_tree_predictions)
print(f"Decision Tree Accuracy: {decision_tree_accuracy:.4f}")

random_forest.fit(train_data, train_labels)
random_forest_predictions = random_forest.predict(test_data)
random_forest_accuracy = accuracy_score(test_labels, random_forest_predictions)
print(f"Random Forest Accuracy: {random_forest_accuracy:.4f}")
