
INSERT INTO login (correo, contrase�a) VALUES
('tadeo@example.com', 'password123'),
('pedrito@example.com', 'contrase�a123');

	
INSERT INTO instructores (ci, nombre, apellido) VALUES
(12345678, 'Carlos', 'P�rez'),
(87654321, 'Laura', 'Garc�a');


INSERT INTO alumnos (ci, nombre, apellido, fecha_nacimiento) VALUES
(23456789, 'Ana', 'Mart�nez', '2005-04-15'),
(98765432, 'Luis', 'Rodr�guez', '2006-07-22');


-- Insert para la tabla actividades
INSERT INTO actividades (descripcion, costo)
VALUES 
('Snowboard', 1500),
('Ski', 1200),
('Moto de nieve', 2000);

-- Insert para la tabla turnos
INSERT INTO turnos ( hora_inicio, hora_final) 
VALUES ( '08:00', '10:00');

-- Insert para la tabla clase
INSERT INTO clase ( ci_instructor, id_actividad, id_turno, dictada) 
VALUES ( '543543', 1, 1, '2024-11-14');

-- Insert para la tabla equipamiento
INSERT INTO equipamiento (id_actividad, descripcion, costo)
VALUES 
(1, 'Antiparras', 500),
(1, 'Cascos', 800),
(1, 'Tablas de snowboard', 2500),
(2, 'Esquíes', 3000),
(2, 'Antiparras', 500),
(2, 'Cascos', 800),
(3, 'Trajes térmicos', 1500),
(3, 'Botas para moto de nieve', 2000);

