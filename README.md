# DevSecOps Flask Application

Modern Flask-based DevSecOps landing page with:

- Flask
- Gunicorn
- Docker Multi-stage Build
- Docker Compose
- Virtual Environment
- Static Assets Separation
- Responsive Modern UI

---

## Project Structure

```text
devsecops-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
└── venv/
```

---

## Features

- Modern DevSecOps Landing Page
- Responsive UI
- Dockerized Application
- Multi-stage Docker Build
- Gunicorn WSGI Server
- Dynamic Hostname Footer
- Lightweight Python Slim Image
- Production-ready Container Structure

---

## Local Development

### 1. Create Virtual Environment

#### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

---

### 2. Install Dependency

```bash
pip install -r requirements.txt
```

---

### 3. Run Flask Application

```bash
python app.py
```

Application URL:

```text
http://127.0.0.1:5000
```

---

## Requirements

### requirements.txt

```text
Flask==3.1.1
gunicorn==23.0.0
```

---

## Docker Multi-stage Build

### Build Image

```bash
docker build -t devsecops-flask:1.0.0 .
```

---

### Run Container

```bash
docker run -d \
  --name devsecops-app \
  --hostname devsecops-prod \
  -p 5000:5000 \
  devsecops-flask:1.0.0
```

---

## Docker Compose

### Start Application

```bash
docker compose up -d --build
```

---

### Stop Application

```bash
docker compose down
```

---

### View Logs

```bash
docker compose logs -f
```

---

## Dockerfile

Application uses:

- Python 3.12 Slim
- Multi-stage Build
- Gunicorn Production Server

Gunicorn command:

```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

---

## Production Improvements

Recommended next improvements:

- NGINX Reverse Proxy
- HTTPS / TLS
- CI/CD Pipeline
- GitHub Actions
- Trivy Container Scanning
- Kubernetes Deployment
- Helm Chart
- Health Check Endpoint
- Prometheus Metrics
- Loki Logging
- OpenTelemetry Tracing
- Non-root Container
- Environment Variable Management
- Secrets Management

---

## Example Health Endpoint

Example future endpoint:

```python
@app.route("/health")
def health():
    return {"status": "ok"}, 200
```

---

## Example Commands

## Check Running Container

```bash
docker ps
```

---

### Check Images

```bash
docker images
```

---

### Enter Container Shell

```bash
docker exec -it devsecops-app sh
```

---

## Tech Stack

- Python
- Flask
- Gunicorn
- Docker
- Docker Compose
- HTML
- CSS
- JavaScript

---

## Version

```text
v1.0.0
```

---

## Author

DevSecOps Platform Engineering Demo Project
