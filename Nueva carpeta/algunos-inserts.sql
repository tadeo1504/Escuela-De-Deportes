INSERT INTO login (correo, contrase�a) VALUES
('tadeo@example.com', 'password123'),
('pedrito@example.com', 'contrase�a123');

INSERT INTO actividades (id, descripcion, costo) VALUES
(1, 'Esqu�', 100),
(2, 'Snowboard', 120);
	
INSERT INTO instructores (ci, nombre, apellido) VALUES
(12345678, 'Carlos', 'P�rez'),
(87654321, 'Laura', 'Garc�a');

INSERT INTO turnos (id, hora_inicio, hora_final) VALUES
(1, '09:00:00', '11:00:00'),
(2, '11:30:00', '13:30:00');

INSERT INTO equipamiento (id, id_actividad, descripcion, costo) VALUES
(1, 1, 'Esqu�s completos', 50),
(2, 2, 'Tabla de snowboard', 60);

INSERT INTO alumnos (ci, nombre, apellido, fecha_nacimiento) VALUES
(23456789, 'Ana', 'Mart�nez', '2005-04-15'),
(98765432, 'Luis', 'Rodr�guez', '2006-07-22');

INSERT INTO clase (id, ci_instructor, id_actividad, id_turno, dictada) VALUES
(1, 12345678, 1, 1, '2024-10-22'),
(2, 87654321, 2, 2, '2024-10-23');

INSERT INTO alumno_clase (id_clase, ci_alumno, id_equipamiento) VALUES
(1, 23456789, 1),
(2, 98765432, 2);
