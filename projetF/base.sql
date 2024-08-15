DROP TABLE IF EXISTS absences CASCADE;
DROP TABLE IF EXISTS emplois_du_temps CASCADE;
DROP TABLE IF EXISTS etudiant CASCADE;
DROP TABLE IF EXISTS salles CASCADE;
DROP TABLE IF EXISTS fields CASCADE;
DROP TABLE IF EXISTS classes CASCADE;
DROP TABLE IF EXISTS ouvertures_porte CASCADE;


CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL
);

CREATE TABLE fields (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL
);

CREATE TABLE salles (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL
);

CREATE TABLE etudiant (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    cin VARCHAR(8) NOT NULL,
    email TEXT NOT NULL,
    classes INTEGER NOT NULL,
    fields INTEGER NOT NULL,
    password TEXT NOT NULL,
    FOREIGN KEY (classes) REFERENCES classes(id),
    FOREIGN KEY (fields) REFERENCES fields(id)
);

CREATE TABLE emplois_du_temps (
    id SERIAL PRIMARY KEY,
    classe_id INTEGER NOT NULL,
    periode VARCHAR(50) NOT NULL,
    matiere VARCHAR(50) NOT NULL,
    fields_id INTEGER NOT NULL,
    salles_id INTEGER NOT NULL,
    FOREIGN KEY (salles_id) REFERENCES salles(id),
    FOREIGN KEY (fields_id) REFERENCES fields(id),
    FOREIGN KEY (classe_id) REFERENCES classes(id)
);

CREATE TABLE absences (
    id SERIAL PRIMARY KEY,
    etudiant_id INTEGER NOT NULL,
    emploi_du_temps_id INTEGER NOT NULL,
    salle_id INTEGER NOT NULL,
    presence VARCHAR(20) NOT NULL,
    date_absence TIMESTAMP NOT NULL,
    carte_rfid VARCHAR(20) NOT NULL,
    cin VARCHAR(20) NOT NULL,
    FOREIGN KEY (etudiant_id) REFERENCES etudiant(id),
    FOREIGN KEY (emploi_du_temps_id) REFERENCES emplois_du_temps(id),
    FOREIGN KEY (salle_id) REFERENCES salles(id)
);

CREATE TABLE ouvertures_porte (
    id SERIAL PRIMARY KEY,
    carte_rfid VARCHAR(20) NOT NULL,
    date_ouverture TIMESTAMP NOT NULL,
    salles_id INTEGER NOT NULL,
    FOREIGN KEY (salles_id) REFERENCES salles(id)
);


INSERT INTO salles (nom) VALUES 
('Salle A'),
('Salle B'),
('Salle C'),
('Salle D'),
('Salle E'),
('Salle F'),
('Salle G'),
('Salle H'),
('Salle K'),
('Salle L'),
('Salle M'),
('Salle N');

INSERT INTO fields (nom) VALUES 
('ISI'),
('SI'),
('IT'),
('IG');

INSERT INTO classes (nom) VALUES 
('1'),
('2'),
('3');

INSERT INTO emplois_du_temps (classe_id, periode, matiere, fields_id, salles_id) VALUES
(1, 'Lundi 08:30-10:00', 'Algèbre', 1, 1),
(1, 'Lundi 10:00-11:30', 'Mécanique', 1, 7),
(1, 'Lundi 14:00-15:30', 'Base de données', 1, 4),
(1, 'Lundi 15:30-17:00', 'Analyse', 1, 8),
(1, 'Mardi 08:30-10:00', 'Algorithmique', 1, 2),
(1, 'Mardi 10:00-11:30', 'Électronique', 1, 4),
(1, 'Mardi 14:00-15:30', 'Probabilité', 1, 2),
(1, 'Mardi 15:30-17:00', 'Électromagnétisme', 1, 4),
(1, 'Mercredi 08:30-10:00', 'PHP', 1, 2),
(1, 'Mercredi 10:00-11:30', 'JS', 1, 6),
(1, 'Mercredi 14:00-15:30', 'Java', 1, 9),
(1, 'Mercredi 15:30-17:00', 'CSS', 1, 4),
(1, 'Jeudi 08:30-10:00', 'Python', 1, 5),
(1, 'Jeudi 10:00-11:30', 'TP JS', 1, 10),
(1, 'Jeudi 14:00-15:30', 'TP PHP', 1, 6),
(1, 'Jeudi 15:30-17:00', 'TD Analyse', 1, 9),
(1, 'Vendredi 08:30-10:00', 'TP Java', 1, 1),
(1, 'Vendredi 10:00-11:30', 'TD Java', 1, 5),
(1, 'Vendredi 14:30-16:00', 'TD Algèbre', 1, 2),
(1, 'Vendredi 15:30-17:00', 'TP Mécanique', 1, 4),
(1, 'Samedi 08:30-10:00', 'English', 1, 11),
(1, 'Samedi 10:00-11:30', 'Culture', 1, 8),
(1, 'Samedi 14:00-15:30', '', 1, 9),
(1, 'Samedi 15:00-17:00', '', 1, 7);
