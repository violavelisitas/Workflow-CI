# Workflow-CI

Repository CI/CD untuk re-training model Iris Classifier menggunakan MLflow Project dan GitHub Actions.

## Struktur Folder

```
Workflow-CI
├── .github/
│   └── workflows/
│       └── train.yml              ← GitHub Actions workflow
└── MLProject/
    ├── MLProject                  ← Konfigurasi MLflow Project
    ├── conda.yaml                 ← Environment dependencies
    ├── modelling.py               ← Script training model
    └── iris_preprocessing/
        └── iris_preprocessing.csv ← Dataset siap latih
```

## Cara Kerja CI

Workflow GitHub Actions terpantik ketika:
- Push ke branch `main`
- Manual trigger (`workflow_dispatch`)

Tahapan workflow:
1. Checkout repository
2. Setup Python 3.12
3. Install dependencies (mlflow, scikit-learn, pandas)
4. Jalankan `mlflow run MLProject/`
5. Upload artefak MLflow ke GitHub Artifacts

## Cara Menjalankan Lokal

```bash
pip install mlflow==2.19.0 scikit-learn pandas numpy
cd MLProject
mlflow run . --env-manager=local
```
