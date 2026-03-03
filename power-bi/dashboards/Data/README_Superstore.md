# 📊 Dashboards Power BI

## Dashboard Superstore - Análisis de Ventas

**Archivo:** `Dashboard_Superstore_Modulo3.pbix`

### 🎯 Objetivo
Análisis completo de datos de ventas de la empresa Superstore utilizando visualizaciones avanzadas de Power BI, demostrando habilidades en transformación de datos, visualizaciones interactivas y storytelling con datos.

### 📂 Dataset
- **Fuente:** Sample Superstore Dataset (adaptado)
- **Registros:** 50 transacciones
- **Período:** 2014-2017
- **Categorías:** Furniture, Office Supplies, Technology
- **Alcance geográfico:** Estados Unidos

---

## 📄 Estructura del Dashboard

### Página 1: Análisis con Tablas y Matrices
**Objetivo:** Visualización detallada de ventas por cliente y clasificación por rangos

**Visualizaciones:**
- 3 tarjetas KPI: Total de Ventas, Total de Ganancias, Cantidad de Ventas
- Tabla detallada por cliente y segmento
- Matriz: Ventas por Categoría vs Segmento
- Gráfico de barras: Distribución por Rango de Venta (Baja, Media, Alta, Premium)
- TreeMap: Ventas por subcategoría
- Mapa geográfico: Distribución de ventas por estado
- 3 Slicers interactivos: Categoría, Segmento, Rango de fechas

**Técnicas aplicadas:**
- Columnas condicionales en Power Query para clasificación de ventas
- Formato condicional en matriz (escalas verde-amarillo-rojo)
- Paleta de colores tipo semáforo para análisis visual rápido

![Página 1 - Tablas y Matrices](screenshots/Página 1 Tablas-Matrices-Clasificación.png)

---

### Página 2: Análisis Geográfico con Jerarquías
**Objetivo:** Exploración interactiva de datos por ubicación con navegación drill-down

**Visualizaciones:**
- Gráfico de columnas con jerarquía Country → State → City (drill-down)
- Matriz con formato condicional: Profit por Categoría y Segmento
- Gráfico de dispersión: Análisis de Ventas vs Profit por Subcategoría
- Gráfico circular: Distribución por nivel de descuento

**Técnicas aplicadas:**
- Creación de jerarquías personalizadas en Vista de Modelo
- Navegación drill-down interactiva
- Formato condicional avanzado
- Análisis de correlación entre variables

![Página 2 - Análisis Geográfico](screenshots/Página 2 Análisis Geográfico.png)

---

## 🛠️ Habilidades Técnicas Demostradas

### Power Query
- Importación y transformación de datos desde CSV
- Configuración regional para correcta interpretación de decimales
- Creación de columnas condicionales
- Limpieza y preparación de datos

### Visualizaciones
- Tablas y matrices con totales
- Gráficos de barras y columnas
- TreeMap para visualización jerárquica
- Mapas geográficos interactivos
- Gráficos de dispersión (scatter plot)
- Gráficos circulares

### Formato y Diseño
- Formato condicional con escalas de color
- Barras de datos en visualizaciones
- Paletas de colores consistentes
- Diseño responsive y balanceado
- Títulos y subtítulos descriptivos

### Interactividad
- Slicers (segmentadores) múltiples
- Jerarquías con drill-down/drill-up
- Filtros de página
- Cross-filtering entre visualizaciones

---

## 📈 Insights Principales

### Análisis de Ventas
- **Total de ventas:** $14,094.65
- **Total de ganancias:** $2,612.13
- **Margen promedio:** ~18.5%
- **Cantidad de transacciones:** 49 órdenes

### Por Segmento
- El segmento **Consumer** representa la mayor parte de las ventas
- **Corporate** muestra mayor margen de ganancia proporcional
- **Home Office** tiene menor volumen pero buen margen

### Por Categoría
- **Technology** lidera en ventas totales
- **Office Supplies** tiene el mayor número de transacciones
- **Furniture** muestra los montos más variables

### Distribución Geográfica
- **California** es el estado con mayores ventas
- Concentración de ventas en costa este y oeste
- Estados centrales con menor penetración

### Clasificación de Ventas
- 67.35% de las transacciones son ventas sin descuento
- 26.53% tienen descuento medio
- Pocas transacciones con descuento alto (6.12%)

---

## 🎨 Decisiones de Diseño

### Paleta de Colores
- **Azul corporativo** como color principal (profesional y confiable)
- **Escala verde-amarillo-rojo** para formato condicional (intuitivo)
- **Colores diferenciados** para categorías (fácil identificación)

### Layout
- **KPIs arriba** para contexto inmediato
- **Visualizaciones principales** en zona central
- **Filtros abajo** para acceso fácil sin interferir
- **Balance entre visualizaciones** para evitar sobrecarga

---

## 📚 Aprendizajes y Desafíos

### Desafíos Resueltos
1. **Problema de separador decimal:** Dataset con puntos en vez de comas
   - Solución: Configuración regional en Power Query
   
2. **Formato condicional en matriz:** Configuración de escalas de color
   - Solución: Uso de punto medio en 0 para pérdidas/ganancias
   
3. **Jerarquías navegables:** Implementación de drill-down
   - Solución: Creación de jerarquía en Vista de Modelo

### Próximos Pasos
- Incorporar medidas DAX personalizadas
- Agregar análisis de tendencias temporales
- Implementar tooltips personalizados
- Crear página de dashboard ejecutivo integrado

---

## 📦 Archivos Incluidos
```
power-bi/dashboards/
├── Dashboard_Superstore_Modulo3.pbix
├── screenshots/
│   ├── pagina1_tablas_matrices.png
│   └── pagina2_geografico_jerarquias.png
├── data/
│   ├── Superstore_ES.csv
│   └── README_Superstore.md
```

---

## 🚀 Cómo Abrir el Dashboard

1. Descargar **Power BI Desktop** (gratuito) desde Microsoft
2. Abrir el archivo `Dashboard_Superstore_Modulo3.pbix`
3. Explorar las páginas usando las pestañas inferiores
4. Interactuar con filtros y visualizaciones
5. Probar la funcionalidad de drill-down en la página 2

---

**Fecha de creación:** Noviembre 2024  
**Herramienta:** Microsoft Power BI Desktop  
**Nivel:** Intermedio  
**Tiempo de desarrollo:** 2 días