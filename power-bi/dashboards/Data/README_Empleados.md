# 📊 Dashboards Power BI

## Dashboard Empleados 

**Archivo:** `Dashboard_Empleados.pbix`

### 🎯 Objetivo
Desarrollar un dashboard interactivo de Recursos Humanos que permita analizar la composición de los empleados desde distintas dimensiones: edad, género, sueldo, desempeño, departamento y ubicación, facilitando la toma de decisiones estratégicas y el análisis exploratorio de datos.

Este dashboard está orientado a demostrar habilidades en Power BI, modelado de datos, visualización, diseño y storytelling con datos, enfocado en un caso típico de RRHH.

### 📂 Dataset
- **Fuente:** BD_RRHH_Empleados.csv
- **Registros:** 196 empleados
- **Alcance geográfico:** Esados Unidos

---

## 📄 Estructura del Dashboard

### Página 1: Reporte A
**Objetivo:** Brindar una visión general de la plantilla de empleados, combinando indicadores clave con análisis demográfico, salarial y organizacional.

### 🔢 KPIs Principales

- Total de Empleados
- Promedio de Edad
- Promedio de Sueldo
- Promedio de Evaluación

Estos indicadores permiten obtener una lectura rápida del estado general de la organización.

**Visualizaciones:**
Botones:
- Reporte A
- Repore B
- Reporte C
Filtros (segmentadores):
- Estado
Gráficos:
- Empleados por rango de edad
- Empleados por evaluación de desempeño
- Empleados por rango salarial
- Empleados por género
- Empleados por departamento
Tabla detallada:
- Listado de empleados con nombre, género, estado y departamento

Interactividad
- Todos los gráficos están conectados entre sí
- Los filtros afectan a la totalidad del dashboard
- Navegación mediante botones entre Reporte A, B y C

**Técnicas aplicadas:**
Power BI / DAX
- Creación de medidas para:
	- Promedios
	- Conteos
	- Agrupaciones por rangos
- Uso de segmentadores para análisis dinámico
- Modelado de datos simple y eficiente

Power Query
- Importación de archivos CSV
- Limpieza y normalización de datos
- Creación de columnas auxiliares para rangos de edad, sueldo y evaluación

![Dashboard_Empleados.png](screenshots/Dashboard_Empleados.png)

---

## 🛠�?Habilidades Técnicas Demostradas

### Power Query
- Importación y transformación de datos desde MySQL
- Configuración regional para correcta interpretación de decimales
- Creación de columnas condicionales
- Creación de medidas
- Limpieza y preparación de datos

### Visualizaciones
- Gráficos de barras y columnas
- Tarjetas
- Segmentación de datos

### Formato y Diseño
- Formato condicional con escalas de color
- Barras de datos en visualizaciones
- Paletas de colores consistentes
- Diseño responsive y balanceado
- Títulos y subtítulos descriptivos
- Utilización de imágenes
- Uso de bordes redondeados y fondos suaves para una estética moderna
- Dashboard optimizado para lectura ejecutiva

---

## 📈 Insights Principales

### Análisis de Empleados
- La empresa cuenta con 194 empleados activos, con una edad promedio cercana a los 45 años.
- La mayor concentración de empleados se encuentra en los rangos etarios intermedios.
- La distribución de género es relativamente equilibrada.
- Producción y Tecnología de la Información concentran la mayor cantidad de empleados.
- La mayoría de los sueldos se agrupan en rangos medios, con oportunidades para análisis de equidad salarial.
- El promedio de evaluación indica un nivel general de desempeño positivo.

---

## 📚 Aprendizajes y Desafíos

### Aprendizajes
- Diseño de dashboards enfocados en RRHH y análisis organizacional
- Uso de KPIs claros para audiencias no técnicas
- Importancia de la segmentación por rangos para mejorar la interpretación
- Integración de tablas detalladas con visualizaciones resumidas
- Mejora en criterios de diseño visual y experiencia de usuario

### Desafíos
- Definir rangos adecuados para edad, sueldo y evaluación
- Mantener claridad visual con múltiples gráficos en una sola página
- Lograr un diseño atractivo sin perder foco analítico
- Balancear detalle y visión general en un mismo dashboard

---

## 📦 Archivos Incluidos
```
power-bi/dashboards/
├── Dashboard_Empleados.pbix
├── screenshots/
�?  ├── Dashboard_Empleados.png
├── data/
�?  ├── BD_RRHH_Empleados.xlsx
�?  └── README_Empleados.md
```

---

## 🚀 Cómo Abrir el Dashboard

1. Descargar **Power BI Desktop** (gratuito) desde Microsoft
2. Abrir el archivo `Dashboard_Empleados.pbix`
3. Explorar las páginas usando las pestañas inferiores
4. Interactuar con filtros y visualizaciones

---

**Fecha de creación:** Febrero 2026  
**Herramienta:** Microsoft Power BI Desktop  
**Nivel:** Intermedio  
**Tiempo de desarrollo:** 2 días