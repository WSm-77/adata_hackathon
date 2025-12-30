# Student Campus Attendance Prediction - Hackathon Solution

## Description

Following a series of concerning incidents at a student campus, the authorities of a Polish university decided to act without delay: they needed to strengthen the security of the Student Campus. For this responsible task, they chose Gepard Security. It's a new player in the security market - full of enthusiasm, but still learning the realities of student life and how many people show up on different days of the week.

Gepard, though ambitious, needs knowledge. That's why they hired you - a team of programmers with a clear goal: to train a model that, based on several available data points, will be able to predict the number of students on a given day. This solution can determine the effectiveness of security and the safety of the entire campus.

Fortunately, you're not starting from scratch - the previous company left behind a rich resource of information: data from an extensive student surveillance system. It's a treasure trove of raw signals and patterns that, when properly processed, will allow you to build a precise crowd prediction model.

The stakes are high: a well-trained model is not just numbers on a chart, it's a real impact on the safety and peace of the campus residents. You have the tools, data, and responsibility - now it's time to turn raw data into intelligent forecasts that will allow Gepard to become the guardian this campus needs.

## Project Structure

```
.
├── bit-x-adata/
│   ├── train.csv              # Training dataset
│   ├── test.csv               # Test dataset
│   └── sample_submission.csv  # Sample submission format
├── model.ipynb                # Main Jupyter notebook with model development
├── pyproject.toml             # Project dependencies
└── README.md                  # This file
```

## Dataset

### Features

- **id** - Unique identifier for each record
- **data** - Date (YYYY-MM-DD format)
- **święto** - Holiday indicator (Boolean)
- **dzień_roboczy** - Working day indicator (Boolean)
- **pogoda** - Weather condition (categorical)
- **temperatura** - Temperature in Celsius
- **odczuwalna_temperatura** - Feels-like temperature in Celsius
- **wilgotność** - Humidity percentage
- **prędkość_wiatru** - Wind speed

### Target Variable

- **studenty_ms** - Number of students on campus (only in training data)

## Solution Approach

This solution implements an ensemble approach combining two models, but in practice the Neural Network model is the primary focus due to its superior performance in this task.

### 1. Neural Network (PyTorch)
- Architecture: Multi-layer perceptron with 3 hidden layers (256 units each)
- Dropout: 0.3 for regularization
- Activation: ReLU with Softplus output layer
- Optimizer: AdamW with L2 regularization
- Loss: Custom RMSLE (Root Mean Squared Logarithmic Error)
- Early stopping with patience of 100 epochs

### 2. Random Forest Regressor
- 300 estimators
- Maximum depth: 12
- Provides robust baseline predictions

### Data Preprocessing

1. Date dropped (not used as a feature) - we had an idea to extract more features from it but didn't implement it
2. Boolean features converted to integers
3. Weather conditions one-hot encoded
4. Features standardized using StandardScaler
5. Train/validation split: 80/20

## Prerequisites

- `Python 3.12` or higher
- `uv` package manager (optional but recommended)

### Dependencies

```bash
# Us uv to install dependencies
uv sync
```

## Usage

### Running the Model

Execute cells sequentially to:
1. Load and preprocess data
2. Train both models
3. Evaluate performance
4. Generate submission file

### Generating Predictions

The notebook will generate `comunicadores_submission.csv` with predictions for the test set.

## Evaluation

Submissions are evaluated on **RMSLE** (Root Mean Squared Logarithmic Error) between the predicted values and the observed target.

RMSLE formula:

$$
RMSLE = \sqrt{\frac{1}{n} \sum_{i=1}^n((\log(\text{predicted}_i + 1) - \log(\text{actual}_i + 1))^2)}
$$

## Submission File Format

For each ID in the test set, you must predict a TARGET variable. The file should contain a header and have the following format:

```csv
id,studenty_ms
2,12
5,23
6,9
```

## Results

The final model achieved an RMSLE of approximately `0.87` on the validation set. Incorporating additional feature engineering on the date column and hyperparameter tuning could further enhance performance. Also further exploration of ensemble methods like XGBoost may yield better results.
