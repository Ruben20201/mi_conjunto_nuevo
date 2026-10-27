# 🏢 ResiControl - Sistema de Gestión y Control Residencial

**ResiControl** es una aplicación web desarrollada con **Django** diseñada para optimizar la administración y el control de acceso en conjuntos residenciales. Permite gestionar boletines informativos, consultar placas vehiculares y verificar el personal de obra o contratistas autorizados de forma rápida e intuitiva.

---

## 🚀 Características Principales

- 🔍 **Consulta de Placas Vehiculares:** Búsqueda rápida de vehículos registrados asociados a residentes o apartamentos. Incluye sistema de alerta y número de atención para visitantes no registrados.
- 📢 **Boletines Informativos:** Panel para la publicación y lectura de comunicados oficiales de la administración.
- 👷 **Control de Personal de Obra:** Gestión y consulta de contratistas y remodeladores autorizados.
- 🎨 **Interfaz Moderna y Adaptativa:** Diseño limpio y balanceado orientado a la facilidad de uso (*UI/UX responsive*).

---

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python 3.13 / Django 6.1
- **Frontend:** HTML5, CSS3 (Flexbox & Grid Layout)
- **Persistencia de Datos / DB:** SQLite / JSON
- **Despliegue:** Render / Git Workflow

---

## 📂 Estructura del Proyecto

```text
mi_conjunto_nuevo/
├── core/                   # Aplicación principal de Django
│   ├── templates/core/     # Plantillas HTML de la aplicación
│   ├── static/core/        # Archivos estáticos (CSS, imágenes)
│   ├── models.py           # Modelos de datos (Vehículo, Empleado, Boletín)
│   └── views.py            # Lógica de las vistas y búsquedas
├── mi_conjunto/            # Configuración global del proyecto Django
├── build.sh                # Script de compilación para despliegue en Render
└── manage.py               # Script de gestión de Django