# Doctor Availability Prediction

Predict whether a doctor will be available for an appointment using a trained SVM model and a simple Flask web form.

## Summary

This repository contains a small Flask web application and supporting files for predicting doctor availability based on patient and appointment features. The web app loads a serialized scikit-learn model (`svm_model.pkl`) and exposes a single web form to submit features and receive a prediction.

## Quick Start

- Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

- Install dependencies:

```bash
pip install -r requirements.txt
```

- Make sure a trained model file named `svm_model.pkl` is in the project root. The Flask app expects this file to exist.

- Run the web app:

```bash
python app.py
```

Open http://127.0.0.1:5000/ in your browser and use the form.

## Files Overview

- **app.py**: Flask application that loads `svm_model.pkl`, renders the form at `/`, and accepts POSTs to `/predict`. It extracts form fields, builds a feature array and calls `model.predict(...)` to generate a human-readable result ("Doctor Will be available" or "Doctor Will not be available"). See [app.py](app.py#L1).

- **main.py**: A tiny script with a `main()` placeholder that prints a greeting. Not required for the Flask app but present as an entry/test file. See [main.py](main.py#L1).

- **templates/index.html**: HTML form used by the Flask app. The form fields map directly to the features expected by the model (Gender, Age, Scholarship, Hypertension, Diabetes, Alcoholism, Handicap, SMS_received, WeekDay, DayScheduled). See [templates/index.html](templates/index.html#L1).

- **requirements.txt**: Pinning of runtime packages used to run the app (Flask, NumPy, scikit-learn). See [requirements.txt](requirements.txt#L1).

- **pyproject.toml**: Project metadata and broader dependency declarations. Useful if you publish or package the project. See [pyproject.toml](pyproject.toml#L1).

- **KaggleV2-May-2016.csv** and **data.csv**: Dataset files (likely the original dataset and/or a derived subset). These are included for reference and for retraining the model.

- **miniproject_modified.ipynb**: Jupyter notebook (likely contains data exploration, preprocessing and model training experiments). If you want to retrain the model, this notebook is a good starting point.

## Expected Model & Inputs

The Flask app expects a serialized scikit-learn model saved as `svm_model.pkl` in the project root. The model must accept a 2D array of features with columns in this order:

1. Gender (encoded as 1 for male, 0 for female in `app.py`)
2. Age (integer)
3. Scholarship (0/1)
4. Hypertension (0/1)
5. Diabetes (0/1)
6. Alcoholism (0/1)
7. Handicap (0/1)
8. SMS_received (0/1)
9. WeekDay (numeric day-of-month / weekday encoding — match how the model was trained)
10. DayScheduled (numeric day-of-month)

If you need to retrain the model, inspect `miniproject_modified.ipynb` or create a new training script that saves a scikit-learn model using `pickle.dump(model, open('svm_model.pkl', 'wb'))`.

## Recreating/Training the Model

Suggested steps (high level):

1. Load the dataset (`KaggleV2-May-2016.csv`) and preprocess to match the features used by the current web form.
2. Train a classifier (SVM or other) using `scikit-learn`.
3. Validate the model, then serialize it to `svm_model.pkl` in the project root.

Example snippet (training + saving):

```python
from sklearn.svm import SVC
import pickle
# X, y = <your feature matrix and labels>
model = SVC()
model.fit(X, y)
with open('svm_model.pkl', 'wb') as f:
    pickle.dump(model, f)
```

## Notes & Troubleshooting

- If you see errors about `svm_model.pkl` not found, create the file as described above or place a trained model with that filename into the project root.
- The `app.py` form parsing assumes `Gender` values of "Male" or "Female" (case-insensitive). Other values will cause an error.
- Make sure numeric fields use 0/1 where expected (Scholarship, Hypertension, Diabetes, Alcoholism, Handicap, SMS_received).
- The mapping for `WeekDay` and `DayScheduled` must match how you trained the model. If in doubt, inspect `miniproject_modified.ipynb`.

## Development

- Run `python app.py` for local development with `debug=True` (already set in `app.py`).
- Use the notebook to iterate on features and preprocessing.

## Dependencies

Install exact environment using `requirements.txt`:

```bash
pip install -r requirements.txt
```

Key packages:

- Flask
- numpy
- scikit-learn



---
