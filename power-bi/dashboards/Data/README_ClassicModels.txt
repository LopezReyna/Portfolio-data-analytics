# 📊 Dashboards Power BI

## Dashboard Concesionaria - ClassicModels

**Archivo:** `Dashboard_Concesionario.pbix`

### 🎯 Objetivo
Análisis completo de datos de ventas de la empresa ClassicModels utilizando visualizaciones avanzadas de Power BI, demostrando habilidades en transformación de datos, visualizaciones interactivas y storytelling con datos.

### 📂 Dataset
- **Fuente:** base+de+datos+classicmodels (adaptado)
- **Registros:** 2996
- **Período:** 2003-2005
- **Alcance geográfico:** Internacional

---

## 📄 Estructura del Dashboard

### Página 1: Análisis con Tablas y Matrices
**Objetivo:** Visualización detallada de Reporte de Ventas 

**Visualizaciones:**
- 5 Filtros: Categoría, Producto, Cliente, Vendedor, Fecha
- 7 tarjetas: Total de Ventas, Transacciones válidas, Ventas promedio, Cantidad vendida, Cantidad promedio, Cetegorías, Variedad de productos
- Gráfico de columnas: Ventaspor Año y Mes
- Gráfico de barras: Ventas por Categoría
- Gráfico de barras: Venta por Producto
- 6 tarjetas: Rentabilidad en ventas, Margen en ventas, Porcentaje de cancelación, Tiempo promedio de entrega, Clientes que han comprado, Países
- Gráfico de barras: Margen de ventas por categoría
- Gráfico de barras: Margen en ventas por producto

**Técnicas aplicadas:**
- Columnas condicionales en Power Query para calcular días de entrega
- Creación de diferentes medidas
- Formato condicional en matriz (escalas verde-amarillo-rojo)
- Paleta de colores en diferentes tonalidades de verde
- Etiquetas de datos en gráficos de barras
- Añadir imágenes en las tarjetas
- Añadir imágen de fondo

![Página 1 - BI ClassicModels](screenshots/Ventas_ClassicModels.png)

---

## 🛠️ Habilidades Técnicas Demostradas

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

---

## 📈 Insights Principales

### Análisis de Ventas
- Las ventas presentan una tendencia creciente a lo largo del período 2003–2005, con picos destacados hacia finales de cada año, lo que sugiere un comportamiento estacional.
- Las categorías Classic Cars y Vintage Cars concentran el mayor volumen de ventas, representando una parte significativa del total facturado.
- Algunos productos específicos generan altos niveles de ventas y margen, evidenciando que un conjunto reducido de productos explica gran parte del rendimiento comercial.
- El margen de ventas varía entre categorías, destacándose Motorcycles y Vintage Cars como las más rentables.
- El porcentaje de cancelación se mantiene bajo, lo que indica estabilidad en los procesos de venta.
- El tiempo promedio de entrega es relativamente estable, permitiendo evaluar oportunidades de optimización logística.
- La empresa cuenta con una base de clientes diversificada en múltiples países, reforzando su carácter internacional.

---

## 🎨 Decisiones de Diseño

### Paleta de Colores
- Se utilizó una paleta de colores en tonalidades verdes para asociar el análisis con conceptos de crecimiento, rentabilidad y desempeño financiero.
- Se priorizó el uso de tarjetas KPI para facilitar una lectura rápida de los indicadores clave.
- Los gráficos de barras y columnas fueron elegidos para simplificar la comparación entre categorías, productos y períodos de tiempo.
- Se aplicó formato condicional para resaltar valores relevantes y mejorar la interpretación visual de los datos.
- Se incorporaron íconos e imágenes en las tarjetas para reforzar la comprensión de cada métrica.
- Se utilizó una imagen de fondo suave para mejorar la estética general sin afectar la legibilidad.

### Layout
- **Fila superior:** Filtros principales (categoría, producto, cliente, vendedor y fecha) junto con los KPIs generales de ventas.
- **Zona central:** Análisis temporal de ventas y distribución por categoría y producto.
- **Zona inferior:** Indicadores de rentabilidad, margen, cancelaciones, tiempos de entrega y alcance comercial.
- El layout fue diseñado siguiendo un enfoque de arriba hacia abajo, permitiendo pasar de una visión general a un análisis más detallado.
- Se mantuvo un diseño equilibrado y limpio para evitar la saturación visual.

---

## 📚 Aprendizajes y Desafíos

### Desafíos Resueltos

Aprendizajes
- Importancia de una correcta transformación y limpieza de datos en Power Query antes del modelado.
- Uso de medidas DAX para calcular métricas clave como ventas, márgenes y rentabilidad.
- Aplicación de buenas prácticas de visualización y diseño para facilitar la lectura del dashboard.
- Organización de múltiples métricas en un único reporte manteniendo claridad y coherencia visual.
- Integración de datos relacionales en un modelo analítico orientado a negocio.

Desafíos
- Adaptar una base de datos relacional a un modelo adecuado para análisis en Power BI.
- Definir métricas de rentabilidad y margen de forma clara y consistente.
- Lograr un balance entre cantidad de información y simplicidad visual.
- Diseñar un dashboard completo en una sola página sin perder legibilidad ni jerarquía visual.

---

## 📦 Archivos Incluidos
```
power-bi/dashboards/
├── Dashboard_Concesionario.pbix
├── screenshots/
│   ├── Ventas_ClassicModels.png
├── data/
│   ├── base+de+datos+classicmodels.sql
│   └── README_ClassicModels.md
```

---

## 🚀 Cómo Abrir el Dashboard

1. Descargar **Power BI Desktop** (gratuito) desde Microsoft
2. Abrir el archivo `Dashboard_Concesionario.pbix`
3. Explorar las páginas usando las pestañas inferiores
4. Interactuar con filtros y visualizaciones

---

**Fecha de creación:** Enero 2026  
**Herramienta:** Microsoft Power BI Desktop  
**Nivel:** Intermedio  
**Tiempo de desarrollo:** 2 días