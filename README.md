# ☕ Sistema de Pedidos para Cafetería — Arquitectura de Microservicios

## 📌 Descripción del Proyecto

Este proyecto consiste en el desarrollo de una aplicación web para la gestión de pedidos de una cafetería utilizando una arquitectura basada en microservicios. El sistema fue diseñado con tecnologías modernas de desarrollo y herramientas DevOps, permitiendo implementar una solución modular, escalable, resiliente y fácil de mantener.

La aplicación simula el funcionamiento de una cafetería donde los usuarios pueden realizar pedidos, gestionar usuarios, consultar inventario y enviar notificaciones mediante diferentes microservicios independientes.

Además, el proyecto incorpora herramientas de contenerización, orquestación, monitoreo, integración continua y observabilidad para cumplir con una arquitectura moderna basada en microservicios.

---

# 🎯 Objetivos

## Objetivo General

Desarrollar un sistema web de pedidos para cafetería utilizando arquitectura de microservicios, implementando Docker, Kubernetes, monitoreo, CI/CD y mecanismos básicos de seguridad.

## Objetivos Específicos

* Dividir la aplicación en microservicios independientes.
* Implementar APIs REST para la comunicación.
* Contenerizar los servicios utilizando Docker.
* Orquestar los microservicios mediante Kubernetes.
* Implementar monitoreo con Prometheus y Grafana.
* Automatizar el proceso de integración continua mediante GitHub Actions.
* Aplicar mecanismos básicos de autenticación.
* Simular tolerancia a fallos y resiliencia utilizando Kubernetes.

---

# 🏗️ Arquitectura del Proyecto

El sistema está compuesto por varios microservicios independientes:

| Microservicio          | Puerto | Función                |
| ---------------------- | ------ | ---------------------- |
| pedidos-service        | 5001   | Gestiona pedidos       |
| usuarios-service       | 5002   | Gestiona usuarios      |
| inventario-service     | 5003   | Gestiona inventario    |
| notificaciones-service | 5004   | Envía notificaciones   |
| frontend               | 5500   | Interfaz web principal |

---

# 🧰 Tecnologías Utilizadas

| Tecnología          | Uso                       |
| ------------------- | ------------------------- |
| Python              | Desarrollo backend        |
| Flask               | APIs REST                 |
| HTML/CSS/JavaScript | Frontend                  |
| Docker              | Contenerización           |
| Docker Compose      | Gestión de contenedores   |
| Kubernetes          | Orquestación              |
| Prometheus          | Recolección de métricas   |
| Grafana             | Visualización de métricas |
| GitHub Actions      | CI/CD                     |
| Git                 | Control de versiones      |
| VS Code             | Desarrollo                |

---

# 📁 Estructura del Proyecto

```text
cafeteria-microservices/
│
├── frontend/
├── pedidos-service/
├── usuarios-service/
├── inventario-service/
├── notificaciones-service/
├── monitoring/
├── kubernetes/
├── .github/
│   └── workflows/
│       └── main.yml
│
├── docker-compose.yml
└── README.md
```

---

# 🔹 División en Microservicios

La aplicación fue dividida en servicios independientes con responsabilidades específicas.

## pedidos-service

Responsable de:

* Crear pedidos.
* Procesar solicitudes.
* Gestionar información de compras.

## usuarios-service

Responsable de:

* Gestionar usuarios.
* Registrar clientes.
* Administrar información de usuarios.

## inventario-service

Responsable de:

* Controlar productos.
* Verificar disponibilidad.
* Administrar existencias.

## notificaciones-service

Responsable de:

* Simular envío de notificaciones.
* Confirmar acciones del sistema.

---

# 🌐 Comunicación entre Microservicios

La comunicación se implementó mediante APIs REST utilizando Flask.

Ejemplo de endpoints:

| Servicio               | Endpoint      |
| ---------------------- | ------------- |
| pedidos-service        | /pedido       |
| usuarios-service       | /usuario      |
| inventario-service     | /inventario   |
| notificaciones-service | /notificacion |

Las peticiones se realizan mediante HTTP usando formato JSON.

---

# 🐳 Docker y Contenerización

Cada microservicio fue contenerizado utilizando Docker.

## Ejemplo Dockerfile

```dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

---

# 📦 Docker Compose

Docker Compose permite levantar todos los servicios simultáneamente.

## Ejemplo docker-compose.yml

```yaml
version: '3'

services:

  pedidos:
    build: ./pedidos-service
    ports:
      - "5001:5001"

  usuarios:
    build: ./usuarios-service
    ports:
      - "5002:5002"

  inventario:
    build: ./inventario-service
    ports:
      - "5003:5003"

  notificaciones:
    build: ./notificaciones-service
    ports:
      - "5004:5004"
```

---

# ☸️ Kubernetes

El proyecto utiliza Kubernetes para la orquestación de microservicios.

## Características implementadas

* Deployments.
* Pods.
* Réplicas.
* Services.
* Escalado horizontal.
* Recuperación automática.

---

# 📄 Ejemplo Deployment

```yaml
apiVersion: apps/v1
kind: Deployment

metadata:
  name: pedidos

spec:
  replicas: 2

  selector:
    matchLabels:
      app: pedidos

  template:

    metadata:
      labels:
        app: pedidos

    spec:

      containers:
      - name: pedidos
        image: pedidos-image

        ports:
        - containerPort: 5001
```

---

# 📄 Ejemplo Service

```yaml
apiVersion: v1
kind: Service

metadata:
  name: pedidos-service

spec:
  selector:
    app: pedidos

  ports:
    - protocol: TCP
      port: 5001
      targetPort: 5001

  type: NodePort
```

---

# 📊 Monitoreo y Observabilidad

Se implementó monitoreo utilizando Prometheus y Grafana.

## Prometheus

Responsable de:

* Recolectar métricas.
* Monitorear servicios.
* Supervisar contenedores.

## Grafana

Responsable de:

* Crear dashboards.
* Mostrar gráficas.
* Visualizar métricas en tiempo real.

---

# 📈 Métricas Implementadas

* flask_http_request_total
* process_cpu_seconds_total
* process_resident_memory_bytes
* flask_http_request_duration_seconds_count

---

# 🔐 Seguridad

Se implementó autenticación básica mediante tokens.

## Ejemplo de validación

```python
from flask import request, jsonify

@app.route('/pedido', methods=['POST'])
def pedido():

    token = request.headers.get("Authorization")

    if token != "12345":
        return jsonify({"error": "No autorizado"}), 401

    return jsonify({
        "mensaje": "Pedido realizado"
    })
```

---

# 🔄 CI/CD con GitHub Actions

Se implementó integración continua mediante GitHub Actions.

## Funcionalidades

* Construcción automática.
* Validación automática.
* Automatización del pipeline.
* Verificación de contenedores Docker.

---

# 📄 Workflow CI/CD

```yaml
name: CI/CD

on:
  push:
    branches:
      - master

jobs:

  build:
    runs-on: ubuntu-latest

    steps:

      - name: Descargar repositorio
        uses: actions/checkout@v3

      - name: Construir contenedores Docker
        run: docker compose build
```

---

# 💥 Chaos Engineering y Resiliencia

Se realizaron pruebas básicas de resiliencia eliminando pods manualmente mediante Kubernetes.

## Ejemplo

```bash
kubectl delete pods --all
```

Kubernetes recrea automáticamente los pods eliminados, demostrando:

* Alta disponibilidad.
* Recuperación automática.
* Resiliencia del sistema.

---

# 🚀 Instalación del Proyecto

## 1. Clonar repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

---

## 2. Entrar al proyecto

```bash
cd cafeteria-microservices
```

---

## 3. Levantar contenedores

```bash
docker compose up --build
```

---

## 4. Abrir frontend

Abrir:

```text
http://127.0.0.1:5500
```

---

# 📊 Acceso a Herramientas

| Herramienta | URL                                            |
| ----------- | ---------------------------------------------- |
| Frontend    | [http://127.0.0.1:5500](http://127.0.0.1:5500) |
| Prometheus  | [http://localhost:9090](http://localhost:9090) |
| Grafana     | [http://localhost:3000](http://localhost:3000) |

---

# 🧪 Pruebas Realizadas

## Pruebas funcionales

* Comunicación entre microservicios.
* Validación de APIs REST.
* Procesamiento de pedidos.

## Pruebas de resiliencia

* Eliminación de pods.
* Recuperación automática.

## Pruebas de monitoreo

* Visualización de métricas.
* Dashboards activos.

## Pruebas CI/CD

* Build automático.
* Validación de contenedores.

---

# 📌 Resultados Obtenidos

* Arquitectura modular y escalable.
* Separación de responsabilidades.
* Monitoreo en tiempo real.
* Recuperación automática ante fallos.
* Automatización del despliegue.
* Integración moderna de tecnologías DevOps.

---

# 📚 Conclusión

El proyecto permitió implementar una arquitectura moderna basada en microservicios utilizando tecnologías ampliamente utilizadas en entornos empresariales.

La integración de Docker, Kubernetes, Prometheus, Grafana y GitHub Actions permitió desarrollar una solución escalable, resiliente y automatizada.

Además, el sistema demuestra cómo los microservicios facilitan el mantenimiento, la modularidad y la evolución de aplicaciones distribuidas.

---

# 👨‍💻 Autor

Proyecto desarrollado con fines académicos para la implementación de arquitectura de microservicios, contenerización, orquestación y observabilidad.
