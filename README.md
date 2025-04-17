# 🌤️ Life OS v5 – Cloud Edition

**Modular FastAPI backend to track personal tasks, emotions, reflections, and health logs using lightweight JSON file storage.**  
Built for quick local or Dockerized deployment, with a focus on simplicity, modularity, and observability.

---

## 🔧 Features

- 🧠 **FastAPI-based API** with modular endpoints:
  - `/tasks` – Create and manage to-dos
  - `/emotions` – Log and track feelings
  - `/reflections` – Store thoughts and realizations
  - `/health` – Record basic wellness metrics
- 📁 JSON file-based persistence (`data/*.json`)
- 🐳 **Fully Dockerized**
- 📜 Built-in Swagger UI (`/docs`) and ReDoc (`/redoc`)
- 💻 Easy to extend, deploy, or integrate into daily journaling apps

---

## 🚀 Getting Started

### ⚙️ 1. Clone the Repository

```bash
git clone https://github.com/rajkamaldas/life-os-v5-cloud.git
cd life-os-v5-cloud
```

### 🐳 2. Run with Docker

```bash
docker build -t lifeos .
docker run -p 8000:8000 lifeos
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) to try the API.

### 🔁 3. Run Fail Simulation

```bash
docker exec -it <container_name> python vanara_logger/fail_simulation.py
```

Or if running locally:
```bash
python vanara_logger/fail_simulation.py
```

---

## 💡 API Example (curl)

### ➕ Add a Task

```bash
curl -X POST "http://localhost:8000/tasks" -H "Content-Type: application/json" -d '{"task": "Revise Day 1", "priority": "low"}'
```

### 📥 Get All Tasks

```bash
curl -X GET "http://localhost:8000/tasks"
```

---

## 📂 Project Structure

```
life-os-v5-cloud/
├── Dockerfile
├── docker-compose.yml
├── .env
├── requirements.txt
├── README.md
├── run_fail_simulation.bat
├── vanara_logger/
│   ├── divine_logger.py
│   ├── example_scene.py
│   └── fail_simulation.py
└── data/
    ├── tasks.json
    ├── emotions.json
    ├── reflections.json
    └── health.json
```

---

## 📬 Future Upgrades

- [ ] Add JWT Authentication
- [ ] Add Telegram Bot integration
- [ ] Push logs to cloud storage or PostgreSQL
- [ ] Weekly digest email report
- [ ] Frontend dashboard (React or Terminal)

---

## 🧠 Made By RKD

A backend crafted to observe thoughts, discipline habits, and log the in-between moments of life.
