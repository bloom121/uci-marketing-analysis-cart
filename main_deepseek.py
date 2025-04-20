import pandas as pd
import requests
from io import BytesIO
from zipfile import ZipFile
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

DATA_URL = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"

def load_data():
    response = requests.get(DATA_URL)
    with ZipFile(BytesIO(response.content)) as main_zip:
        with main_zip.open('bank-additional.zip') as f:
            additional_zip = ZipFile(BytesIO(f.read()))
            with additional_zip.open('bank-additional/bank-additional-full.csv') as csv_file:
                return pd.read_csv(csv_file, delimiter=';')

# Load and clean data
df = load_data()

# Clean target variable
df['y'] = df['y'].str.strip().str.lower()
df['conversion'] = df['y'].map({'yes': 1, 'no': 0})

# Clean categorical features
df['job'] = df['job'].str.strip().str.lower()
df['education'] = df['education'].str.strip().str.lower()

# Prepare features
X = pd.get_dummies(df.drop(['y', 'conversion'], axis=1))
y = df['conversion']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Metrics function
def print_metrics(name, y_true, y_pred):
    print(f"\n{name} Set")
    print(f"Samples: {len(y_true):,}")
    print(f"Accuracy: {accuracy_score(y_true, y_pred):.2%}")
    print(f"Conversion Rate: {y_true.mean():.2%}")

print_metrics("Training", y_train, model.predict(X_train))
print_metrics("Testing", y_test, model.predict(X_test))

# Calculate job/education groups
job_edu_groups = (
    df.groupby(['job', 'education'])
    .agg(
        Conversion_Rate=('conversion', 'mean'),
        Samples=('conversion', 'count')
    )
    .query('Samples >= 50')
    .sort_values('Conversion_Rate', ascending=False)
    .head(10)
)

# Verify and print results
print("\nConversion Rate Ranges:")
print(f"Max: {job_edu_groups['Conversion_Rate'].max():.2%}")
print(f"Min: {job_edu_groups['Conversion_Rate'].min():.2%}")

print("\nTop 10 Job/Education Groups:")
print(job_edu_groups.to_markdown(floatfmt=(".6%", ".6f")))
