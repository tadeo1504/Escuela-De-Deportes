"""
create table actividades(
id int primary key,
descripcion varchar(50),
costo int
);

CREATE TABLE login (
correo varchar(20) primary key,
contrase�a varchar(20),
);

create table instructores(
ci int primary key,
nombre varchar(15),
apellido varchar(15)
);

create table turnos(
id int primary key,
hora_inicio time,
hora_final time
);

create table alumnos(
ci int primary key,
nombre varchar(15),
apellido varchar(15),
fecha_naciemiento date
);

create table clase(
ci_instructor int,
id_actividad int,
id_turno int,
dictada date,
id int primary key,
foreign key (id_actividad) references actividades(id),
foreign key (ci_instructor) references instructores(ci),
foreign key (id_turno) references turnos(id)
);

create table alumno_clase(
id_clase int,
ci_alumno int,
id_equipamiento int,
foreign key (id_clase) references clase(id),
foreign key (ci_alumno) references alumnos(ci),
foreign key (id_equipamiento) references equipamiento(id)
);
"""