

create table instructores(
ci int primary key,
nombre varchar(15),
apellido varchar(15)
);

create table turnos(
id int primary key,
hora_inicio int,
hora_final int
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
dictada bit,
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
foreign key (ci_alumno) references alumnos(ci)
);