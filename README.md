# 🌙 MoonInsurance Microservices Platform

This repository contains the complete codebase and configuration files for the **MoonInsurance** platform — a scalable, fault-tolerant, and secure microservices application deployed on **Amazon EKS** and managed using **Docker**, **Kubernetes**, and **GitHub Actions CI/CD pipelines**.

## 📦 Services Overview

The platform consists of independent microservices, each deployed and scaled separately:

- **🔹 Agent Service**  
  Manages insurance agent data, including agent profiles and allowed products.  
  ⤷ Data stored in **Amazon RDS (PostgreSQL)**

- **🔹 Integration Service**  
  Ingests and syncs insurance sales data from MoonInsurance's core system.

- **🔹 Notification Service**  
  Sends real-time alerts to stakeholders when sales goals are achieved.  
  ⤷ Uses **AWS SES** for email notifications.

- **🔹 Aggregator Service**  
  Periodically aggregates team performance and product sales data.  
  ⤷ Runs as a **Kubernetes CronJob**

- **🔹 Reporting/Redshift Publisher Service**  
  Publishes aggregated metrics to **AWS Redshift** for analytics and reporting.  
  ⤷ Visualized using **AWS QuickSight**

Each service is containerized using Docker and deployed on **Amazon EKS** with Kubernetes manifests stored under the `/k8` directory.

## ☁️ Cloud & Deployment Architecture

### ✅ Deployed AWS Components

- **Amazon EKS**  
  Orchestrates and auto-scales microservices in a managed Kubernetes environment.

- **Amazon ECR**  
  Stores versioned Docker images used by GitHub Actions during deployments.

- **Amazon RDS (PostgreSQL)**  
  Used by Agent and Integration services to persist operational data.

- **Amazon Redshift**  
  Stores aggregated performance metrics for company-wide analytics.

- **AWS QuickSight**  
  Interactive dashboards visualizing Redshift metrics.

- **AWS SES**  
  Sends automated notifications via email from the Notification Service.

## 🔁 CI/CD Pipeline

All services are deployed via a **GitHub Actions-based CI/CD pipeline** that supports:

- **Automated builds** using Docker
- **Push to Amazon ECR**
- **Deployment to Amazon EKS** via `kubectl`
- **Blue-Green Deployment Strategy** for zero-downtime releases
- **Automated testing** after deployment to ensure service reliability

CI/CD workflows are defined under `.github/workflows/`.

> This pipeline ensures secure, repeatable, and fully automated deployments with rollback support.

## 🔍 Observability

Each service is monitored via:

- **Kubernetes readiness & liveness probes**
- **Logging and metrics collection** via Kubernetes stdout + CloudWatch (optional)
- **Cron-based health jobs** to validate ongoing data processing in Aggregator & Redshift Publisher services

## 🐳 Docker & Local Development

Each service contains a `Dockerfile`. Build locally for testing:
```bash
docker build -t agent-service ./agent-service
docker build -t integration-service ./integration-service
docker build -t notification-service ./notification-service
docker build -t aggregator-service ./aggregator-service
docker build -t reporting-service ./reporting-service
```

Developed by Kalhari Ekanayake for the CMM707 Cloud Computing coursework (Robert Gordon University, 2025).
