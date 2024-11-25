CREATE TABLE actividades (
    id INT PRIMARY KEY IDENTITY(1,1),
    descripcion VARCHAR(50),
    costo INT
);

CREATE TABLE login (
    id INT IDENTITY(1,1) PRIMARY KEY,
    username NVARCHAR(50) NOT NULL UNIQUE,
    password NVARCHAR(255) NOT NULL
);

CREATE TABLE instructores (
    ci INT PRIMARY KEY,
    nombre VARCHAR(15),
    apellido VARCHAR(15)
);

CREATE TABLE turnos (
    id INT PRIMARY KEY IDENTITY(1,1),
    hora_inicio TIME,
    hora_final TIME
);

CREATE TABLE alumnos (
    ci INT PRIMARY KEY,
    nombre VARCHAR(15),
    apellido VARCHAR(15),
    fecha_nacimiento DATE
);

CREATE TABLE clase (
    id INT PRIMARY KEY IDENTITY(1,1),
    ci_instructor INT,
    id_actividad INT,
    id_turno INT,
    dictada DATE,
    FOREIGN KEY (ci_instructor) REFERENCES instructores(ci),
    FOREIGN KEY (id_actividad) REFERENCES actividades(id),
    FOREIGN KEY (id_turno) REFERENCES turnos(id)
);

CREATE TABLE equipamiento (
    id INT PRIMARY KEY IDENTITY(1,1),
    id_actividad INT,
    descripcion VARCHAR(30),
    costo INT,
    FOREIGN KEY (id_actividad) REFERENCES actividades(id)
);

CREATE TABLE alumno_clase (
    id_clase INT,
    ci_alumno INT,
    id_equipamiento INT,
    PRIMARY KEY (id_clase, ci_alumno, id_equipamiento),
    FOREIGN KEY (id_clase) REFERENCES clase(id),
    FOREIGN KEY (ci_alumno) REFERENCES alumnos(ci),
    FOREIGN KEY (id_equipamiento) REFERENCES equipamiento(id)
);
