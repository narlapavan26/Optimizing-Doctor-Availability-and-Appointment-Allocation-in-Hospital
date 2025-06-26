```markdown
# 📅 Medical Appointment No-Show Prediction

This project analyzes a real-world dataset to predict whether a patient will show up for their scheduled medical appointment. It uses classification algorithms and standard exploratory data analysis (EDA) techniques to find factors contributing to patient no-shows.

---

## 📊 Dataset

- **Source**: [Kaggle - Medical Appointment No Shows](https://www.kaggle.com/datasets/joniarroba/noshowappointments)
- **Records**: 110,527 medical appointments
- **Target variable**: `No-show` (whether a patient showed up or not)

---

## 🧠 Project Objectives

- Analyze the dataset for patterns and correlations
- Clean and preprocess the data
- Train a logistic regression model from scratch
- Evaluate the performance using classification metrics

---

## 📁 Project Structure

```
miniproject_modified/
├── miniproject_modified.ipynb  # Main notebook (EDA + ML)
├── README.md                   # Project documentation
├── environment.yml             # (Optional) Conda environment file
└── data/
    └── KaggleV2-May-2016.csv   # Original dataset
```

---

## ⚙️ Requirements

Install the required packages with:

```bash
pip install -r requirements.txt
```

Or, if using Conda:

```bash
conda env create -f environment.yml
conda activate no_show_env
```

### 🧪 Libraries used:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `datetime`

---

## 🔧 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/lucky3156/Mini_project_sem_6.git
   cd Mini_project_sem_6
   ```

2. Open the Jupyter notebook:
   ```bash
   jupyter notebook miniproject_modified.ipynb
   ```

3. Run cells in order: it performs EDA, data cleaning, logistic regression, and evaluates model performance.

---

## 📈 Results

- Logistic regression was used for binary classification.
- Accuracy, precision, recall, and F1-score were calculated.
- Feature importance was derived from the model coefficients.

---

## 📌 Key Insights

- Features like **SMS reminders**, **previous no-shows**, and **age** influence the likelihood of missing appointments.
- Data had column name inconsistencies (e.g., `Hipertension`) which were corrected.

---

## 📃 License

This project is for educational purposes only.
```
