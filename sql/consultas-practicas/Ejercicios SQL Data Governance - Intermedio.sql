/*
EJERCICIO 1 – AUDITORIA DE CAMBIOS
Obtener el ultimo registro de auditoria correspondiente a la tabla 'datasets'.
*/

select top 1 id_auditoria, tabla_afectada, id_registro, fecha as ult_fecha, rv
from auditoria_cambios
where tabla_afectada = 'datasets'
order by fecha desc

/*
EJERCICIO 2 – ULTIMO CAMBIO POR TABLA
Identificar el ultimo registro de auditoria para cada tabla afectada.
*/

with ultimo_cambio as
	(
	select id_auditoria, tabla_afectada,
	row_number() over(partition by tabla_afectada order by fecha desc) rn,
	id_registro, accion, usuario, fecha, rv
	from auditoria_cambios
	)
select id_auditoria, tabla_afectada,id_registro, accion, usuario, fecha, rv
from ultimo_cambio
where rn = 1

/*
EJERCICIO 3 – DATASETS PRODUCTIVOS MODIFICADOS
Listar los datasets en estado 'productivo' que tengan al menos un registro de auditoria,
mostrando el ultimo cambio realizado sobre cada uno.
*/

with datasets_prod as
	(
	select id_auditoria, tabla_afectada, id_registro, accion, usuario, fecha, rv,
		ROW_NUMBER() over(partition by id_registro order by fecha desc) rn
	from auditoria_cambios
	where tabla_afectada = 'datasets'
	)
select a.*, b.id_dataset, b.nombre_dataset, b.dominio_dato, b.nivel_sensibilidad, b.id_area, b.estado
from datasets_prod a
inner join datasets b
on b.id_dataset = a.id_registro
where estado = 'productivo'
and rn = 1

/*
EJERCICIO 4 – ACCESOS INDEBIDOS A DATOS
Objetivo:
Detectar empleados inactivos que aun conservan accesos a datasets.
*/


select a.id_empleado, concat(a.nombre, ' ', a.apellido) nombre_completo, 
	a.id_area, b.id_acceso, b.id_dataset, b.nivel_acceso, b.fecha_otorgado
from empleados a
inner join accesos_datasets b
	on a.id_empleado = b.id_empleado
where estado = 'inactivo'

/*
EJERCICIO 5 – ACCESO A DATOS SENSIBLES
Listar los empleados que poseen acceso a datasets con nivel de sensibilidad 'alto',
indicando el nivel de acceso otorgado.
*/

select a.id_dataset, a.nombre_dataset, a.dominio_dato, a.nivel_sensibilidad, a.id_area, a.estado,
	b.id_acceso, b.nivel_acceso, b.fecha_otorgado, 
	c.id_empleado, concat(c.nombre, ' ', c.apellido) nombre_completo, c.id_area, c.estado
from datasets a
inner join accesos_datasets b
	on a.id_dataset = b.id_dataset
inner join empleados c
	on b.id_empleado = c.id_empleado
where a.nivel_sensibilidad = 'alto'

/*
EJERCICIO 6 – GOBIERNO DE DATOS INCOMPLETO
Detectar datasets cuyo area responsable no tiene un Data Owner definido.
*/

select a.id_dataset, a.nombre_dataset, a.dominio_dato, a.nivel_sensibilidad, a.id_area, a.estado,
	b.nombre_area, b.data_owner, b.data_steward
from datasets a
inner join areas b
	on a.id_area = b.id_area
where data_owner is null

/*
EJERCICIO 7 – MONITOREO DE CALIDAD DE DATOS
Analizar la cantidad de issues de calidad de datos abiertos, agrupados por severidad.
*/

with cant_abiertos as
	(
	select count(id_issue) issue_abiertos, severidad
	from data_quality_issues
	where estado = 'abierto'
	group by severidad
	)
select *
from cant_abiertos

/*
EJERCICIO 8 – COBERTURA DE CONTROLES DE CALIDAD
Identificar datasets que no tengan issues de calidad registrados.
*/

select a.id_dataset, a.nombre_dataset, a.dominio_dato, a.nivel_sensibilidad, a.id_area, a.estado
from datasets a 
left join data_quality_issues b
	on a.id_dataset = b.id_dataset
where b.id_issue is null

/*
EJERCICIO 9 – CALIDAD DE DATOS POR AREA
Determinar qué areas concentran la mayor cantidad de issues de calidad de datos.
*/

select a.id_area, nombre_area, count(c.id_dataset) cantidad
from areas a
inner join datasets b
	on a.id_area = b.id_area
inner join data_quality_issues c
	on b.id_dataset = c.id_dataset	
group by a.id_area, nombre_area

/*
EJERCICIO 10 – CONTROL DE TRAZABILIDAD
Detectar accesos a datasets que no tengan un registro correspondiente en la auditoria.
*/

select a.id_acceso, a.id_empleado, a.id_dataset, a.nivel_acceso, a.fecha_otorgado
from accesos_datasets a
left join auditoria_cambios b
	on a.id_acceso = b.id_registro
	and tabla_afectada = 'accesos_datasets'
where b.id_auditoria is null

/*
EJERCICIO 11 – ACCESOS OTORGADOS DESPUES DE LA BAJA
Detectar accesos a datasets otorgados después de que el empleado fue dado de baja.
*/

select a.id_empleado, concat(a.nombre, ' ', a.apellido) empleado, a.fecha_ingreso,
	a.fecha_baja, b.id_acceso, b.nivel_acceso, b.fecha_otorgado
from empleados a 
inner join accesos_datasets b
	on a.id_empleado = b.id_empleado
where a.fecha_baja is not null 
and a.fecha_baja < b.fecha_otorgado
/*
EJERCICIO 12 – EMPLEADOS CON EXCESO DE PRIVILEGIOS
Identificar empleados que tengan mas de un acceso con nivel admin.
*/
-- no hay empleados que tengan mas de un nivel de acceso 'admin' 

with accesos as
	(
	select id_acceso, id_empleado, id_dataset, nivel_acceso, fecha_otorgado,
	ROW_NUMBER() over(partition by id_empleado order by fecha_otorgado)rn
	from accesos_datasets
	where nivel_acceso = 'admin'
	)
select a.id_acceso, a.id_empleado, concat(nombre,' ',apellido) nombre_completo, 
	b.fecha_ingreso, b.estado, b.id_area, a.id_dataset, a.nivel_acceso, fecha_otorgado
from accesos a
inner join empleados b
	on a.id_empleado = b.id_empleado
where rn > 1


select *
from accesos_datasets

/*
EJERCICIO 13 – DATASETS SIN ACCESOS REGISTRADOS
Detectar datasets que nunca fueron accedidos por ningun empleado.
*/

select a.id_dataset, a.nombre_dataset, a.dominio_dato, a.nivel_sensibilidad, a.id_area, a.estado
from datasets a
left join accesos_datasets b
	on a.id_dataset = b.id_dataset
where b.id_acceso is null

/*
EJERCICIO 14 – HISTORIAL DE CAMBIOS POR DATASET
Listar el historial de cambios de cada dataset mostrando: tabla, accion, usuario, fecha, rowversion
Ordenado del mas reciente al mas antiguo.
*/

select tabla_afectada, accion, usuario, fecha, rv
from auditoria_cambios
where tabla_afectada = 'datasets'
order by rv desc

/*
EJERCICIO 15 – ULTIMO CAMBIO REALIZADO POR DATASET
Obtener el ultimo cambio registrado para cada dataset.
*/

with ultimo_cambio as
	(
	select id_auditoria, tabla_afectada, id_registro, accion, usuario, fecha, rv,
	ROW_NUMBER() over(partition by id_registro order by fecha desc) as rn
	from auditoria_cambios a
	where tabla_afectada = 'datasets'
	)
select *
from ultimo_cambio
where rn = 1