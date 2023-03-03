CREATE SCHEMA IF NOT EXISTS expressoft;

USE expressoft;

CREATE TABLE empleados (
  empleado_id int(11) NOT NULL,
  tipo_empleado varchar(50) NOT NULL,
  contrasenia varchar(50) NOT NULL,
  nombre varchar(50) NOT NULL,
  apellido_paterno varchar(50) NOT NULL,
  apellido_materno varchar(50) NOT NULL,
  estatus boolean NOT NULL,
  telefono int(12) NOT NULL,
  email varchar(50) NOT NULL,
  PRIMARY KEY (empleado_id)
);

CREATE TABLE venta (
  venta_id int(11) NOT NULL,
  total decimal(10,2) NOT NULL,
  fecha date NOT NULL,
  hora time NOT NULL,
  empleado_id int(11) NOT NULL,
  PRIMARY KEY (venta_id),
  FOREIGN KEY (empleado_id) REFERENCES empleados (empleado_id)
);

INSERT INTO empleados (empleado_id, tipo_empleado, contrasenia, nombre, apellido_paterno, apellido_materno, estatus, telefono, email) VALUES
(1, 'Administrador', '123', 'Juan', 'Perez', 'Lopez', 1, 1234567890, 'hola@gmail.com');
INSERT INTO empleados (empleado_id, tipo_empleado, contrasenia, nombre, apellido_paterno, apellido_materno, estatus, telefono, email) VALUES
(2, 'Gerente', '123', 'Maria', 'Perez', 'Lopez', 1, 1234567891, 'hola2@gmail.com');
INSERT INTO empleados (empleado_id, tipo_empleado, contrasenia, nombre, apellido_paterno, apellido_materno, estatus, telefono, email) VALUES
(3, 'Empleado', '123', 'Pedro', 'Perez', 'Lopez', 1, 1234567892, 'hola3@gmail.com');