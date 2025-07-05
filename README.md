# UCI Marketing Analysis with CART 🌟

![CART Analysis](https://img.shields.io/badge/CART-Analysis-brightgreen)

Welcome to the **UCI Marketing Analysis CART** repository! This project dives into the UCI bank marketing dataset using Classification and Regression Trees (CART) to analyze marketing strategies. We aim to uncover insights that can help improve conversion rates and enhance marketing analytics.

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Data Description](#data-description)
- [Analysis Techniques](#analysis-techniques)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

This repository focuses on analyzing the UCI bank marketing dataset. The dataset contains information about customer demographics and their responses to marketing campaigns. Using decision trees, specifically CART, we can identify patterns that lead to successful marketing strategies.

### Why CART?

CART is a powerful method for both classification and regression tasks. It builds decision trees that are easy to interpret and visualize. This makes it an excellent choice for understanding customer behavior and optimizing marketing efforts.

## Getting Started

To get started with this project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bloom121/uci-marketing-analysis-cart.git
   cd uci-marketing-analysis-cart
   ```

2. **Set up your environment**:
   Use Miniconda to create a virtual environment. This ensures that you have the right dependencies installed without affecting your system Python installation.

   ```bash
   conda create -n marketing-analysis python=3.8
   conda activate marketing-analysis
   ```

3. **Install required packages**:
   Install the necessary libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the dataset**:
   You can find the dataset [here](https://archive.ics.uci.edu/ml/datasets/bank+marketing). Download it and place it in the `data` folder of this repository.

5. **Run the analysis**:
   Execute the Jupyter Notebook to see the analysis in action:
   ```bash
   jupyter notebook analysis.ipynb
   ```

For detailed instructions, visit the [Releases section](https://github.com/bloom121/uci-marketing-analysis-cart/releases).

## Data Description

The dataset consists of various attributes related to bank marketing campaigns. Key features include:

- **Age**: Age of the client.
- **Job**: Type of job (e.g., admin, technician, etc.).
- **Marital Status**: Marital status of the client.
- **Education**: Education level of the client.
- **Balance**: Account balance in euros.
- **Duration**: Duration of the last contact in seconds.
- **Campaign**: Number of contacts performed during this campaign for this client.
- **Response**: Target variable indicating if the client subscribed to a term deposit.

## Analysis Techniques

In this project, we utilize various techniques to analyze the data:

1. **Data Preprocessing**:
   - Handle missing values.
   - Encode categorical variables.
   - Normalize numerical features.

2. **Decision Tree Implementation**:
   - Build a decision tree model using `scikit-learn`.
   - Visualize the decision tree to understand splits.

3. **Model Evaluation**:
   - Use metrics like accuracy, precision, and recall to evaluate the model.
   - Plot ROC curves to assess performance.

## Usage

To use the analysis, follow these steps:

1. Load the dataset:
   ```python
   import pandas as pd
   data = pd.read_csv('data/bank.csv')
   ```

2. Preprocess the data:
   ```python
   # Handle missing values and encode categorical variables
   ```

3. Train the CART model:
   ```python
   from sklearn.tree import DecisionTreeClassifier
   model = DecisionTreeClassifier()
   model.fit(X_train, y_train)
   ```

4. Evaluate the model:
   ```python
   from sklearn.metrics import accuracy_score
   predictions = model.predict(X_test)
   accuracy = accuracy_score(y_test, predictions)
   print(f'Accuracy: {accuracy}')
   ```

For detailed analysis, refer to the Jupyter Notebook provided in the repository.

## Results

The results from our analysis provide insights into customer behavior and effective marketing strategies. The decision tree model highlights key factors influencing a client's decision to subscribe to a term deposit. By understanding these factors, marketing teams can tailor their campaigns to target potential clients more effectively.

### Key Findings

- **Age** and **Job Type** significantly impact the likelihood of subscription.
- Clients with higher account balances are more likely to subscribe.
- The duration of the last contact is a strong predictor of success.

These insights can guide future marketing efforts and improve overall conversion rates.

## Contributing

We welcome contributions from the community! If you have suggestions or improvements, please fork the repository and submit a pull request. Ensure that your code follows the existing style and includes tests where applicable.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Add your message"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please reach out:

- **Author**: Your Name
- **Email**: your.email@example.com
- **GitHub**: [Your GitHub Profile](https://github.com/yourprofile)

Thank you for visiting the UCI Marketing Analysis CART repository! We hope you find the insights useful. For updates and releases, check the [Releases section](https://github.com/bloom121/uci-marketing-analysis-cart/releases).