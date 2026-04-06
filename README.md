# 🔧 devops-lab

A full DevOps stack demonstrating infrastructure patterns — containerized application, reverse proxy, CI/CD pipeline, monitoring, and local orchestration.

![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker%20Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/Github%20Actions-282a2e?style=for-the-badge&logo=githubactions&logoColor=367cfe) 
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![CI](https://github.com/hugpaim/devops-lab/actions/workflows/ci.yml/badge.svg)

---

## 📐 Architecture

```
┌─────────────────────────────────────────────────────┐
│             GitHub Actions CI/CD                    │
│   push → build → test → run → healthcheck           │
└──────────────────────┬──────────────────────────────┘
                       │
         ┌─────────────▼─────────────┐
         │       Docker Compose      │
         │                           │
         │  ┌────────┐  ┌─────────┐  │
         │  │  App   │  │  Nginx  │  │
         │  │ :5000  │  │  :80    │  │
         │  └────────┘  └─────────┘  │
         │                           │
         │  ┌──────────────────────┐ │
         │  │  Prometheus :9090    │ │
         │  │  Grafana    :3000    │ │
         │  └──────────────────────┘ │
         └───────────────────────────┘
```

---

## 📁 Project Structure

```
devops-lab/
├── app/
│   ├── app.py              # Flask app with /health and /metrics
│   ├── requirements.txt
│   └── Dockerfile
│
├── nginx/
│   └── nginx.conf          # Reverse proxy config
│
├── monitoring/
│   ├── prometheus.yml      # Metrics scraping
│   └── grafana/
│       └── dashboard.json  # Dashboard (optional)
│
├── scripts/
│   ├── setup.sh            # One-command setup
│   └── healthcheck.sh      # Health verification
│
├── .github/
│   └── workflows/
│       └── ci.yml          # CI pipeline
│
├── docker-compose.yml      # Full stack
├── docker-compose.dev.yml  # Dev mode (hot reload)
├── Makefile
└── README.md
```

---

## 🚀 Quick Start

```bash
# 1. Clone repo
git clone https://github.com/hugpaim/devops-lab.git
cd devops-lab

# 2. Start full stack
make up

# 3. Check health
make health
```

---

## 🌐 Services

| Service    | URL                   |
| ---------- | --------------------- |
| App        | http://localhost      |
| Prometheus | http://localhost:9090 |
| Grafana    | http://localhost:3000 |

👉 Grafana login: **admin / admin**

---

## ⚙️ Make Commands

| Command     | Description                  |
| ----------- | ---------------------------- |
| make up     | Start all services           |
| make down   | Stop everything              |
| make logs   | View logs                    |
| make build  | Rebuild containers           |
| make health | Check system health          |
| make clean  | Remove all containers/images |

---

## 🔄 CI/CD Pipeline

Runs on every push to `main`:

* Build — Docker containers
* Run — Start services
* Test — Health check endpoint
* Validate — Ensure system is up

---

## 📊 Monitoring

* Prometheus scrapes `/metrics` endpoint every 15s
* Grafana visualizes metrics
* Health endpoint `/health` ensures system availability

---

## 🛠️ Tech Stack

| Layer      | Tool                 |
| ---------- | -------------------- |
| App        | Python / Flask       |
| Container  | Docker + Compose     |
| Proxy      | Nginx                |
| CI/CD      | GitHub Actions       |
| Monitoring | Prometheus + Grafana |
| System     | Linux                |

---

## 📈 Features

* Multi-service architecture
* Reverse proxy with Nginx
* Monitoring with Prometheus & Grafana
* Health checks
* Dev & production environments
* CI pipeline integration

---

## 🔮 Future Improvements

* Kubernetes migration
* Terraform integration (AWS)
* Alerting system
* Centralized logging

---

Part of @hugpaim DevOps portfolio

