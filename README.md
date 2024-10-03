## Setup Virtual Environtment - Anaconda

```
conda create --name dashboard_da python=3.11.1
conda activate dashboard_da
pip install -r requirements.txt
```

## Setup Virtual Environtment - Local Prompt

```
python -m venv dashboard_da
dashboard_da\Scripts\activate
pip install -r requirements.txt
```

## Run Streamlit

Masuk ke dalam direktori /dashboard terlebih dahulu dengan command "cd dashboard"

```
streamlit run dashboard.py
```
