from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np
import sklearn  # Add this import

print("NumPy version:", np.__version__)
print("Scikit-learn version:", sklearn.__version__)

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Train model
model = RandomForestClassifier(
    n_estimators=10,
    random_state=42,
    max_depth=3
)

model.fit(X, y)

# Save model
with open('app/model.pkl', 'wb') as f:
    pickle.dump(model, f, protocol=4)

print(f"Model saved to app/model.pkl with scikit-learn {sklearn.__version__}")
