import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ucimlrepo import fetch_ucirepo

# Fetch the UCI Bank Marketing Dataset
bank_marketing = fetch_ucirepo(id=222)
X = bank_marketing.data.features
y = bank_marketing.data.targets['y']

# Encode target variable ('yes' to 1, 'no' to 0)
y = (y == 'yes').astype(int)

# Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Identify categorical and numerical features
categorical_features = X.select_dtypes(include=['object']).columns.tolist()
numerical_features = X.select_dtypes(exclude=['object']).columns.tolist()

# Create preprocessor for one-hot encoding categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
        ('num', 'passthrough', numerical_features)
    ]
)

# Create pipeline with preprocessor and CART classifier
clf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', DecisionTreeClassifier(random_state=42))
])

# Train the model
clf.fit(X_train, y_train)

# Make predictions
y_train_pred = clf.predict(X_train)
y_test_pred = clf.predict(X_test)

# Calculate metrics
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)
train_conversion_rate = y_train.mean()
test_conversion_rate = y_test.mean()

# Output training and testing results
print("Training set:")
print(f"  Sample number: {len(X_train)}")
print(f"  Accuracy: {train_accuracy:.4f}")
print(f"  Conversion rate: {train_conversion_rate:.4f}")
print("\nTesting set:")
print(f"  Sample number: {len(X_test)}")
print(f"  Accuracy: {test_accuracy:.4f}")
print(f"  Conversion rate: {test_conversion_rate:.4f}")

# Calculate top ten groups by job and education
df = X[['job', 'education']].copy()
df['y'] = y
group_rates = df.groupby(['job', 'education'])['y'].agg(['mean', 'count']).reset_index()
group_rates.columns = ['Job', 'Education', 'Conversion Rate', 'Sample Number']
top_groups = group_rates.sort_values('Conversion Rate', ascending=False).head(10)

# Output top ten groups
print("\nTop 10 groups based on job and education with highest conversion rates:")
print(top_groups.to_string(index=False))
