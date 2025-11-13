-- ============================================
-- 20 EJERCICIOS SQL - NIVEL INTERMEDIO
-- Autor: Portfolio Data Analytics
-- Base de datos: Tienda Online (E-commerce)
-- ============================================

/*
TEMAS CUBIERTOS:
- JOINs (INNER, LEFT, RIGHT)
- GROUP BY con funciones agregadas
- HAVING
- Subconsultas
- CASE WHEN
- Funciones de fecha
- DISTINCT
- ORDER BY avanzado
*/

-- ============================================
-- BLOQUE 1: JOINs BÁSICOS
-- ============================================

-- EJERCICIO 1: INNER JOIN simple
-- Obtené una lista de todos los pedidos mostrando:
-- id_pedido, fecha_pedido, nombre_cliente, apellido_cliente

select p.id_pedido, p.fecha_pedido, c.nombre nombre_cliente, c.apellido apellido_cliente
from tienda_online.dbo.pedidos p
inner join tienda_online.dbo.clientes c
    on p.id_cliente = c.id_cliente


-- EJERCICIO 2: LEFT JOIN
-- Listá TODOS los clientes y sus pedidos (si los tienen)
-- Incluí clientes que NO tienen pedidos
-- Mostrá: nombre_cliente, apellido_cliente, id_pedido

select c.nombre nombre_cliente, c.apellido apellido_cliente, p.id_pedido
from tienda_online.dbo.clientes c
left join tienda_online.dbo.pedidos p
    on c.id_cliente = p.id_cliente


-- EJERCICIO 3: JOIN múltiple
-- Obtené información completa de pedidos:
-- nombre_cliente, nombre_producto, cantidad, precio_unitario
-- Usá las 3 tablas: clientes, pedidos, detalles_pedido, productos

select c.nombre nombre_cliente, pr.nombre_producto, dp.cantidad, dp.precio_unitario
from tienda_online.dbo.clientes c
inner join tienda_online.dbo.pedidos p
    on c.id_cliente = p.id_cliente
inner join tienda_online.dbo.detalles_pedido dp 
    on p.id_pedido = dp.id_pedido
inner join tienda_online.dbo.productos pr
    on dp.id_producto = pr.id_producto



-- ============================================
-- BLOQUE 2: FUNCIONES AGREGADAS Y GROUP BY
-- ============================================

-- EJERCICIO 4: Contar pedidos por cliente
-- Mostrá cuántos pedidos hizo cada cliente
-- Columnas: nombre_completo (concatenado), total_pedidos

select c.nombre + ' ' +  c.apellido as nombre_completo, count(p.id_pedido) total_pedidos
from tienda_online.dbo.clientes c
inner join tienda_online.dbo.pedidos p
    on c.id_cliente = p.id_cliente
group by c.nombre, c.apellido
order by nombre_completo asc



-- EJERCICIO 5: Total de ventas por producto
-- Calculá el total vendido de cada producto (cantidad * precio)
-- Mostrá: nombre_producto, total_vendido
-- Ordená de mayor a menor

select p.nombre_producto, sum(dp.cantidad * dp.precio_unitario) as total_vendido
from tienda_online.dbo.detalles_pedido dp
inner join tienda_online.dbo.productos p
    on dp.id_producto = p.id_producto
group by p.nombre_producto
order by total_vendido desc

-- EJERCICIO 6: Promedio de monto por pedido
-- Calculá el monto promedio de los pedidos por cliente
-- Mostrá: nombre_cliente, promedio_gasto

select c.nombre + ' ' + c.apellido as nombre_cliente, avg(dp.cantidad * dp.precio_unitario) as promedio_gasto
from tienda_online.dbo.clientes c
inner join tienda_online.dbo.pedidos p 
    on c.id_cliente = p.id_cliente
inner join tienda_online.dbo.detalles_pedido dp
    on p.id_pedido = dp.id_detalle
group by c.nombre, c.apellido 



-- EJERCICIO 7: Productos más vendidos
-- Mostrá los 5 productos con mayor cantidad vendida
-- Columnas: nombre_producto, cantidad_total_vendida

select top 5 p.nombre_producto , sum(dp.cantidad) as cantidad_total_vendida
from tienda_online.dbo.detalles_pedido dp
inner join tienda_online.dbo.productos p
    on dp.id_producto = p.id_producto
group by dp.id_producto, p.nombre_producto
order by cantidad_total_vendida desc


-- ============================================
-- BLOQUE 3: HAVING (Filtrar después de agrupar)
-- ============================================

-- EJERCICIO 8: Clientes frecuentes
-- Encontrá clientes que hicieron MÁS de 2 pedidos
-- Mostrá: nombre_cliente, cantidad_pedidos

select c.nombre as nombre_cliente, count(p.id_pedido) as cantidad_pedidos
from tienda_online.dbo.clientes c
inner join tienda_online.dbo.pedidos p
    on c.id_cliente = p.id_cliente
group by c.nombre
having count(p.id_pedido) >= 2

-- EJERCICIO 9: Productos con ventas superiores
-- Mostrá productos cuyas ventas totales superan $500
-- Columnas: nombre_producto, total_ventas

select p.nombre_producto, sum(dp.cantidad * dp.precio_unitario) as total_ventas
from tienda_online.dbo.detalles_pedido dp
inner join tienda_online.dbo.productos p
    on dp.id_producto = p.id_producto
group by p.id_producto, p.nombre_producto
having sum(dp.cantidad * dp.precio_unitario) > 500

-- EJERCICIO 10: Categorías rentables
-- Mostrá categorías con un promedio de precio > $500
-- Columnas: categoria, precio_promedio

select p.categoria, avg(p.precio)
from tienda_online.dbo.productos p
group by p.id_producto, p.categoria
having avg(p.precio) > 500


-- ============================================
-- BLOQUE 4: SUBCONSULTAS (Subqueries)
-- ============================================

-- EJERCICIO 11: Productos más caros que el promedio
-- Listá productos cuyo precio es mayor al precio promedio
-- Mostrá: nombre_producto, precio, categoria

select p.nombre_producto, p.precio, p.categoria 
from tienda_online.dbo.productos p
where p.precio > (select avg(p.precio) 
                    from tienda_online.dbo.productos p)



-- EJERCICIO 12: Cliente con mayor gasto
-- Encontrá el cliente que más gastó en total
-- Mostrá: nombre_cliente, total_gastado

select top 1 c.nombre as nombre_cliente, sum(dp.cantidad * dp.precio_unitario) as total_gastado
from tienda_online.dbo.clientes c
inner join tienda_online.dbo.pedidos p
    on c.id_cliente = p.id_cliente
inner join tienda_online.dbo.detalles_pedido dp
    on p.id_pedido = dp.id_detalle
group by c.id_cliente, c.nombre
order by total_gastado desc


-- EJERCICIO 13: Productos nunca vendidos
-- Listá productos que NO aparecen en ningún pedido
-- Usá NOT IN o NOT EXISTS

select p.id_producto, p.nombre_producto, p.categoria, p.precio
from tienda_online.dbo.productos p
where p.id_producto not in (select dp.id_producto
                             from tienda_online.dbo.detalles_pedido dp)



-- ============================================
-- BLOQUE 5: CASE WHEN (Condicionales)
-- ============================================

-- EJERCICIO 14: Clasificar clientes por actividad
-- Clasificá clientes según cantidad de pedidos:
-- 0 pedidos: "Inactivo"
-- 1-2 pedidos: "Ocasional"
-- 3+ pedidos: "Frecuente"
-- Mostrá: nombre_cliente, cantidad_pedidos, clasificacion

select c.nombre + ' ' + c.apellido as nombre_cliente, count(p.id_pedido) as cantidad_pedidos, 
    case when count(p.id_pedido) = 0 then 'Inactivo'
         when count(p.id_pedido) <= 2 then 'Ocasional'
         when count(p.id_pedido) >= 3 then 'Frecuente'
    end as clasificacion
from tienda_online.dbo.clientes c
inner join tienda_online.dbo.pedidos p
    on c.id_cliente = p.id_cliente
group by c.id_cliente, c.nombre, c.apellido


-- EJERCICIO 15: Categorizar productos por precio
-- Clasificá productos:
-- precio < 300: "Económico"
-- precio 300-800: "Medio"
-- precio > 800: "Premium"
-- Mostrá: nombre_producto, precio, rango_precio

select p.nombre_producto, p.precio,
    case when p.precio < 300 then 'Economico'
         when p.precio between 300 and 800 then 'Medio'
         when p.precio > 800 then 'Premium' 
    end as rango_precio
from tienda_online.dbo.productos p


-- EJERCICIO 16: Estado de stock
-- Mostrá productos con su estado:
-- stock = 0: "Sin stock"
-- stock < 10: "Stock bajo"
-- stock >= 10: "Stock disponible"

select p.id_producto, p.nombre_producto, 
    case when p.stock = 0 then 'Sin Stock'
         when p.stock < 10 then 'Stock Bajo'
         when p.stock >= 10 then 'Stock Disponible'
    end as estado
from tienda_online.dbo.productos p




-- ============================================
-- BLOQUE 6: FUNCIONES DE FECHA
-- ============================================

-- EJERCICIO 17: Pedidos del último mes
-- Listá pedidos realizados en los últimos 15 meses
-- Mostrá: id_pedido, fecha_pedido, nombre_cliente

select p.id_pedido, p.fecha_pedido, c.nombre as nombre_cliente
from tienda_online.dbo.pedidos p
inner join tienda_online.dbo.clientes c
    on p.id_cliente = c.id_cliente
where p.fecha_pedido >= dateadd(month, -15, getdate())



-- EJERCICIO 18: Ventas por mes
-- Calculá el total de ventas agrupado por mes y año
-- Mostrá: año, mes, total_ventas
-- Ordená cronológicamente

select year(p.fecha_pedido) as año, month(p.fecha_pedido) as mes, 
    sum(dp.cantidad * dp.precio_unitario) as total_ventas
from tienda_online.dbo.pedidos p
inner join tienda_online.dbo.detalles_pedido dp
    on p.id_pedido = dp.id_pedido
group by year(p.fecha_pedido), month(p.fecha_pedido)
order by year(p.fecha_pedido) asc, month(p.fecha_pedido) asc


-- ============================================
-- BLOQUE 7: CONSULTAS COMPLEJAS
-- ============================================

-- EJERCICIO 19: Reporte completo de ventas
-- Creá un reporte que muestre:
-- - Producto, categoría, cantidad vendida, total ventas
-- - Solo productos que se vendieron al menos 1 vez
-- - Ordenado por total_ventas descendente

select p.nombre_producto, p.categoria, sum(dp.cantidad) as cantidad_vendida, 
    sum(dp.cantidad * dp.precio_unitario) as total_ventas
from tienda_online.dbo.detalles_pedido dp
inner join tienda_online.dbo.productos p
    on dp.id_producto = p.id_producto
group by p.id_producto, p.nombre_producto, p.categoria
order by total_ventas desc



-- EJERCICIO 20: Análisis de clientes VIP
-- Encontrá clientes que cumplan TODAS estas condiciones:
-- - Hicieron más de 2 pedidos
-- - Su gasto total supera $1000
-- - Hicieron al menos 1 pedido en los últimos 14 meses
-- Mostrá: nombre_cliente, total_pedidos, total_gastado, ultimo_pedido

select concat(c.nombre, ' ', c.apellido) as nombre_cliente, count(distinct p.id_pedido) as total_pedidos,
    sum(dp.cantidad * dp.precio_unitario) as total_gastado, max(p.fecha_pedido) as ultimo_pedido
from tienda_online.dbo.clientes c
inner join tienda_online.dbo.pedidos p
    on c.id_cliente = p.id_cliente
inner join tienda_online.dbo.detalles_pedido dp
    on p.id_pedido = dp.id_pedido
--where p.fecha_pedido 
group by c.id_cliente, c.nombre, c.apellido
having count(distinct p.id_pedido) > 2 
    and sum(dp.cantidad * dp.precio_unitario) > 1000
    and max(p.fecha_pedido) >= dateadd(month, -14, GETDATE())

-- ============================================
-- CREACIÓN DE BASE DE DATOS DE PRÁCTICA
-- ============================================

CREATE DATABASE tienda_online;
USE tienda_online;

-- Tabla Clientes
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY IDENTITY (1,1),
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    email VARCHAR(100),
    fecha_registro DATE
);

-- Tabla Productos
CREATE TABLE productos (
    id_producto INT PRIMARY KEY IDENTITY (1,1),
    nombre_producto VARCHAR(100),
    categoria VARCHAR(50),
    precio DECIMAL(10,2),
    stock INT
);

-- Tabla Pedidos
CREATE TABLE pedidos (
    id_pedido INT PRIMARY KEY IDENTITY (1,1),
    id_cliente INT,
    fecha_pedido DATE,
    estado VARCHAR(20),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- Tabla Detalles del Pedido
CREATE TABLE detalles_pedido (
    id_detalle INT PRIMARY KEY IDENTITY (1,1),
    id_pedido INT,
    id_producto INT,
    cantidad INT,
    precio_unitario DECIMAL(10,2),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- Insertar datos de prueba

-- Clientes
INSERT INTO clientes (nombre, apellido, email, fecha_registro) VALUES
('Ana', 'García', 'ana.garcia@email.com', '2024-01-15'),
('Carlos', 'López', 'carlos.lopez@email.com', '2024-02-20'),
('María', 'Rodríguez', 'maria.rodriguez@email.com', '2024-03-10'),
('Juan', 'Martínez', 'juan.martinez@email.com', '2024-04-05'),
('Laura', 'Fernández', 'laura.fernandez@email.com', '2024-05-12'),
('Pedro', 'González', 'pedro.gonzalez@email.com', '2024-06-18');

-- Productos
INSERT INTO productos (nombre_producto, categoria, precio, stock) VALUES
('Laptop HP', 'Electrónica', 850.00, 15),
('Mouse Logitech', 'Accesorios', 25.00, 50),
('Teclado Mecánico', 'Accesorios', 120.00, 30),
('Monitor Samsung 24"', 'Electrónica', 200.00, 20),
('Webcam HD', 'Accesorios', 60.00, 25),
('Auriculares Sony', 'Electrónica', 150.00, 40),
('SSD 1TB', 'Componentes', 100.00, 35),
('RAM 16GB', 'Componentes', 80.00, 45),
('Tablet Android', 'Electrónica', 300.00, 18),
('Cargador USB-C', 'Accesorios', 20.00, 0);

-- Pedidos
INSERT INTO pedidos (id_cliente, fecha_pedido, estado) VALUES
(1, '2024-07-01', 'Entregado'),
(1, '2024-08-15', 'Entregado'),
(2, '2024-07-10', 'Entregado'),
(2, '2024-09-20', 'Entregado'),
(2, '2024-10-05', 'En proceso'),
(3, '2024-08-25', 'Entregado'),
(4, '2024-09-30', 'Entregado'),
(4, '2024-10-15', 'Entregado'),
(4, '2024-10-28', 'En proceso'),
(5, '2024-10-20', 'Entregado');

-- Detalles de pedidos
INSERT INTO detalles_pedido (id_pedido, id_producto, cantidad, precio_unitario) VALUES
(1, 1, 1, 850.00),
(1, 2, 2, 25.00),
(2, 5, 1, 60.00),
(2, 6, 1, 150.00),
(3, 4, 2, 200.00),
(4, 7, 1, 100.00),
(4, 8, 2, 80.00),
(5, 3, 1, 120.00),
(6, 9, 1, 300.00),
(6, 2, 3, 25.00),
(7, 1, 1, 850.00),
(7, 4, 1, 200.00),
(8, 6, 2, 150.00),
(8, 7, 1, 100.00),
(9, 8, 1, 80.00),
(9, 9, 1, 300.00),
(10, 3, 2, 120.00),
(10, 5, 1, 60.00);

