# Workflow-CI

Repository CI/CD untuk re-training model Heart Disease Classifier menggunakan MLflow Project dan GitHub Actions.

## Struktur Folder

```
Workflow-CI
├── .github/workflows/train.yml
└── MLProject/
    ├── MLProject
    ├── conda.yaml
    ├── modelling.py
    └── heart_preprocessing/
        └── heart_preprocessing.csv
```

## Cara Jalankan Lokal

```bash
pip install mlflow==2.19.0 scikit-learn==1.5.2 pandas numpy
cd MLProject
mlflow run . --env-manager=local
```
