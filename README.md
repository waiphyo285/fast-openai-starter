## 🚀 Quick Start

Install Python 3 and pip3 (If not already installed) in your machine.

### 1. Clone the Repo

```
git clone <repo-url>
cd openai-fastapi
```

### 2. Cerate VENV

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```
pip3 install -r requirements.txt
```

### 4. Start Server

```
uvicorn app.main:app --reload --port 8001

[ OR ]

python3 -m app.main
```

### 5. Update requirements (opt)

```
pip3 freeze > requirements.txt
```
