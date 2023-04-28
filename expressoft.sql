CREATE SCHEMA IF NOT EXISTS expressoft;

USE expressoft;

CREATE TABLE empleados (
  empleado_id varchar(50) NOT NULL,
  tipo_empleado ENUM('gerente', 'administrador', 'empleado') NOT NULL,
  contrasenia varchar(50) NOT NULL,
  nombre varchar(50) NOT NULL,
  apellido_paterno varchar(50) NOT NULL,
  apellido_materno varchar(50) NOT NULL,
  estatus boolean NOT NULL,
  telefono varchar(15) NOT NULL,
  email varchar(50) NOT NULL,
  PRIMARY KEY (empleado_id)
);

CREATE TABLE venta (
  venta_id int(11) AUTO_INCREMENT,
  total decimal(10,2) NOT NULL,
  fecha date NOT NULL,
  hora time NOT NULL,
  empleado_id varchar(50) NOT NULL,
  archivo_id int(11) NOT NULL,
  PRIMARY KEY (venta_id)
);

CREATE TABLE archivos_ventas (
  archivo_id int(11) AUTO_INCREMENT NOT NULL,
  nombre_archivo varchar(50) UNIQUE,
  fecha date NOT NULL,
  empleado_id varchar(50) NOT NULL,
  PRIMARY KEY (archivo_id)
);

CREATE TABLE metas (
  id INT(11) AUTO_INCREMENT,
  descripcion VARCHAR(50) NOT NULL,
  meta_ventas DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO metas (descripcion, meta_ventas) VALUES
('Metas diarias individuales', 1000.00),
('Metas mensuales individuales', 30000.00),
('Metas anuales individuales', 360000.00),
('Metas diarias totales', 10000.00),
('Metas mensuales totales', 300000.00),
('Metas anuales totales', 3600000.00);

INSERT INTO empleados (empleado_id, tipo_empleado, contrasenia, nombre, apellido_paterno, apellido_materno, estatus, telefono, email) VALUES
('1', 'Administrador', '123', 'Juan', 'Perez', 'Lopez', 1, 1234567890, 'hola@gmail.com');
INSERT INTO empleados (empleado_id, tipo_empleado, contrasenia, nombre, apellido_paterno, apellido_materno, estatus, telefono, email) VALUES
('2', 'Gerente', '123', 'Maria', 'Perez', 'Lopez', 1, 1234567891, 'hola2@gmail.com');
INSERT INTO empleados (empleado_id, tipo_empleado, contrasenia, nombre, apellido_paterno, apellido_materno, estatus, telefono, email) VALUES
('3', 'Empleado', '123', 'Pedro', 'Perez', 'Lopez', 1, 1234567892, 'hola3@gmail.com');

