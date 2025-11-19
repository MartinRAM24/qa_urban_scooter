# 🛵 Proyecto de Automatización QA – Urban Scooter  
Pruebas automatizadas para el servicio Urban Scooter: creación de repartidores, login, eliminación y creación/seguimiento de órdenes.

Este proyecto es una práctica personal enfocada en fortalecer habilidades de automatización API en Python utilizando:
- pytest  
- requests  
- parametrización avanzada  
- validaciones en base de datos (PostgreSQL)  
- arquitectura por módulos  

---

## 📌 Objetivo

El objetivo de este repositorio es recrear un flujo completo de testing automatizado para un sistema estilo "Urban Scooter", validando:
- Creación de couriers  
- Login de couriers  
- Eliminación de couriers  
- Creación de órdenes  
- Seguimiento de órdenes  
- Validaciones correctas de campos (positivas y negativas)  
- Comprobación del estado en la base de datos  

---

## 🧱 Arquitectura del proyecto

Basado en los archivos del repositorio:  

├── configuration.py # Endpoints del servicio y URL base

├── data.py # Headers y datos por defecto para peticiones
├── helpers.py # Funciones de apoyo y conexión a BD

├── sender_stand_request.py # Métodos para llamar a la API (POST, GET, DELETE)

└── test_create_user.py # Suite de pruebas automatizadas


---

## 🌐 API Usada (Entrenamiento)

URL Base:  
`https://cnt-8989a145-1d0a-4a2c-b6c5-804d58dde624.containerhub.tripleten-services.com`  
:contentReference[oaicite:0]{index=0}

Endpoints incluidos:  
- `POST /api/v1/courier` – Crear courier  
- `POST /api/v1/courier/login` – Login de courier  
- `DELETE /api/v1/courier/:id` – Eliminar courier  
- `POST /api/v1/orders` – Crear orden  
- `GET /api/v1/orders/track` – Consultar orden por track  

---

## 🧪 Funcionalidades Automatizadas

### ✔️ 1. **Crear Courier**
El test cubre valores válidos e inválidos para el campo `login`.  

Basado en el archivo:  
:contentReference[oaicite:1]{index=1}

### ✔️ 2. **Login Courier**
Login exitoso con datos correctos y validación del atributo `id`.

### ✔️ 3. **Eliminar Courier**
Flujo completo:  
1. Login → obtener `courier_id`  
2. DELETE `/courier/:id`  
3. Intento de eliminar nuevamente → se espera 404  

### ✔️ 4. **Crear Orden**
Con campos como:  
- firstName  
- lastName  
- dirección  
- metroStation  
- fecha  
- colores  
- etc.

Se valida:  
- Código 201 al crear  
- Código 200 al consultar  
- Que el valor enviado sea igual al de la respuesta  

### ✔️ 5. **Validaciones Negativas**
Si un campo no cumple el criterio → status 400.

### ✔️ 6. **Validación en Base de Datos**
Helpers incluidos para:  
- Buscar courier por login  
- Verificar su creación/eliminación  
:contentReference[oaicite:2]{index=2}

---

## 🧪 Tecnologías utilizadas

- Python 3  
- Pytest  
- Requests  
- PostgreSQL (para validaciones internas)  
- psycopg2  

---