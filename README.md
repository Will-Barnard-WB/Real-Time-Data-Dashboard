# **📊 Real-Time Data Web Dashboard**  
*A Dockerized full-stack application that retrieves and displays financial data from PostgreSQL using Flask and React.*  

## 🚀 Overview  
This project is a **real-time data web dashboard** that:  
- Accesses financial data stored in **PostgreSQL**  
- Serves data through a **Flask API**  
- Displays it in **React** and **Flask** (each running in separate Docker containers)  
- Runs all components using **Docker Compose** for easy deployment
  

## 🛠️ Features  
✔ **Data Retrieval** – Accesses financial data from **PostgreSQL** via Flask  
✔ **Multiple Frontend Views** – Displays data using both **React** and Flask  
✔ **Containerized Deployment** – Uses **Docker Compose** to manage services  
✔ **Scalable & Modular** – Each component runs in its own **Docker container**  

## 🛠️ Technologies Used  
👉 **Flask** – API for retrieving data from PostgreSQL  
👉 **PostgreSQL** – Database for storing financial data  
👉 **React** – Frontend for dynamic data visualization  
👉 **Docker & Docker Compose** – Containerized deployment  

---

## 📂 Project Structure  
```bash
├── flask_app/                   # Flask API for accessing PostgreSQL
│   ├── app.py                   # Main Flask application
│   ├── Dockerfile               # Dockerfile for Flask API
│   ├── requirements.txt         # Flask dependencies
├── react-frontend/              # React web application
│   ├── src/                     # React components
│   ├── public/                  # Static assets
│   ├── node-modules/            # Installed dependencies 
│   ├── public/                  # Dockerfile for React app
├── docker-compose.yml           # Docker Compose configuration
├── README.md                    # Project documentation
```




### **Furture Improvements**
- **React:** Displays data in an interactive dashboard.  
- **Flask (for UI):** Provides an alternative interface for accessing data.  



---

