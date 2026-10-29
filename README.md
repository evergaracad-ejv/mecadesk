# MecaDesk - Plataforma de Gestión para Talleres Mecánicos

**Subproyecto:** Desarrollo de Aplicaciones I  
**Metodología:** Modelo en V (Fase Descendente - Verificación)  
**Stack Tecnológico:** Python, Django REST Framework, Vite.js, PostgreSQL y Docker

---

## A.1- Rama Descendente de la Metodología en V

### 1. Análisis de Requisitos (Requirement Gathering)
MecaDesk responde a la necesidad de digitalizar y optimizar la gestión operativa de un taller mecánico. 
* **Necesidades del Usuario:**
  * Autenticación segura y control de acceso basado en roles.
  * Registro y gestión de clientes y sus vehículos.
  * Creación y seguimiento del estado de órdenes de trabajo mecanizadas.
  * Control de inventario de repuestos y asignación a servicios.
* **Funcionalidades del Sistema:**
  * Módulo de autenticación vía tokens JWT.
  * Panel de administración centralizado (Django Admin).
  * Dashboard e interfaz interactiva para recepción y mecánicos.

### 2. Análisis del Sistema (System Analysis)
El comportamiento general del software se estructura mediante una arquitectura de tres capas desmembradas y desacopladas en contenedores de Docker:
* **Entrada de Datos (Frontend):** SPA desarrollada en Vite.js para una experiencia de usuario rápida y fluida.
* **Capa de Negocio (Backend):** Servidor Django REST Framework encargándose de las validaciones, permisos por rol y lógica de procesos.
* **Capa de Persistencia (Base de Datos):** PostgreSQL para almacenamiento relacional e integridad referencial.

### 3. Diseño de Software / Arquitectura (Software Design)
* **Arquitectura de Microservicios / Contenedores (`docker-compose`):**
  * `db`: PostgreSQL 15 en el puerto `5432`.
  * `backend`: Django 5.x ejecutándose en `http://localhost:8000`.
  * `frontend`: Vite.js ejecutándose en `http://localhost:5173`.
* **Mecanismos de Seguridad e Interfaces:**
  * Autenticación mediante `djangorestframework-simplejwt` (`/api/token/`).
  * Comunicación asíncrona mediante JSON a través de HTTP/REST.

### 4. Diseño de Módulos (Module Design)
* **Módulo `accounts`:**
  * Modelo `User` personalizado heredando de `AbstractUser`.
  * Campo de rol (`Role`): `ADMIN`, `RECEPCIONISTA`, `MECANICO`.
* **Módulos Futuros (Mantenimiento / Vehículos / Órdenes):**
  * Modelos relacionales para vincular Clientes (`Customer`), Vehículos (`Vehicle`) y Órdenes (`WorkOrder`).

### 5. Punto de Inflexión
Fase de transición entre la especificación teórica del sistema y la construcción física del código, garantizando que el entorno containerizado esté alineado con las especificaciones del cliente.

### 6. Codificación (Coding)
Implementación práctica del stack tecnológico utilizando contenedores aislados de Docker para asegurar la portabilidad y paridad entre entornos de desarrollo y producción.