CREATE DATABASE expressoft;

CREATE TABLE empleado (
  empleado_id int(11) NOT NULL,
  tipo_empleado varchar(50) NOT NULL,
  contraseña varchar(50) NOT NULL,
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
  CONSTRAINT venta_ibfk_1 FOREIGN KEY (empleado_id) REFERENCES empleado (empleado_id)
);
