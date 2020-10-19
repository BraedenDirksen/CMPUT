DROP TABLE IF EXISTS apartments;
DROP TABLE IF EXISTS suites;
DROP TABLE IF EXISTS tenants;

PRAGMA foreign_keys = ON;

CREATE TABLE apartments (
  aID	INTEGER,
  address	TEXT,
  numberOfSuites
  INTEGER,
  builtYear	INTEGER,
  PRIMARY KEY (aID)
);

CREATE TABLE suites (
  sID     INTEGER,
  type     TEXT,
  unitNumber     INTEGER,
  price INTEGER,
  aID      INTEGER,
  PRIMARY KEY (sID),
  FOREIGN KEY (aID) REFERENCES apartments
);

CREATE TABLE tenants (
  tID    INTEGER,
  name     TEXT,
  yearOfOccup INTEGER,
  sID     INTEGER,
  PRIMARY KEY (tID),
  FOREIGN KEY (sID) REFERENCES suites

);

-- apartments
INSERT INTO apartments VALUES (0, 'Whyte Ave', 10, 1980);
INSERT INTO apartments VALUES (1, 'Bonnie Doon', 6, 1985);
INSERT INTO apartments VALUES (2, 'Jasper Ave', 8, 1975);

-- suites
INSERT INTO suites VALUES (0, '2 bedrooms', 101, 1100 , 0);
INSERT INTO suites VALUES (1, '1 bedroom', 102, 900 , 0);
INSERT INTO suites VALUES (2, '1 bedrooms', 103, 900 , 0);
INSERT INTO suites VALUES (3, '1 bedrooms', 104, 900 , 0);
INSERT INTO suites VALUES (4, '2 bedrooms', 105, 1100 , 0);
INSERT INTO suites VALUES (5, '2 bedrooms', 201, 1200 , 0);
INSERT INTO suites VALUES (6, '2 bedrooms', 202, 1200 , 0);
INSERT INTO suites VALUES (7, '1 bedroom', 203, 1100 , 0);
INSERT INTO suites VALUES (8, '1 bedroom', 204, 1100 , 0);
INSERT INTO suites VALUES (9, '2 bedrooms', 205, 1200 , 0);

INSERT INTO suites VALUES (10, '2 bedrooms', 101, 1150 , 1);
INSERT INTO suites VALUES (11, 'bachelor', 102, 850 , 1);
INSERT INTO suites VALUES (12, '1 bedrooms', 201, 1200 , 1);
INSERT INTO suites VALUES (13, '1 bedrooms', 202, 1200 , 1);
INSERT INTO suites VALUES (14, 'bachelor', 301, 1000 , 1);
INSERT INTO suites VALUES (15, 'bachelor', 302, 1000 , 1);

INSERT INTO suites VALUES (16, '2 bedrooms', 101, 1300 , 2);
INSERT INTO suites VALUES (17, 'bachelor', 102, 950 , 2);
INSERT INTO suites VALUES (18, '1 bedrooms', 201, 1200 , 2);
INSERT INTO suites VALUES (19, '1 bedrooms', 202, 1200 , 2);
INSERT INTO suites VALUES (20, 'bachelor', 301, 850 , 2);
INSERT INTO suites VALUES (21, '1 bedroom', 302, 1200 , 2);
INSERT INTO suites VALUES (22, '2 bedrooms', 401, 1300 , 2);
INSERT INTO suites VALUES (23, 'bachelor', 402, 1050 , 2);

-- tenants
INSERT INTO tenants VALUES (0, 'McDavid', 2004, 0);
INSERT INTO tenants VALUES (1, 'Neal', 2002, 1);
INSERT INTO tenants VALUES (2, 'Bear', 2000, 3);
INSERT INTO tenants VALUES (3, 'Smith', 2000, 4);
INSERT INTO tenants VALUES (4, 'Hopkins', 2001, 7);
INSERT INTO tenants VALUES (5, 'Kassian', 1998, 9);

INSERT INTO tenants VALUES (6, 'Yamamto', 2003, 10);
INSERT INTO tenants VALUES (7, 'Bouchard', 2001, 11);
INSERT INTO tenants VALUES (8, 'Graunlund', 1996, 12);
INSERT INTO tenants VALUES (9, 'Haas', 1999, 13);
INSERT INTO tenants VALUES (10, 'Sheahan', 2000, 14);
INSERT INTO tenants VALUES (11, 'Koshinen', 2004, 15);

INSERT INTO tenants VALUES (12, 'Persson', 2000, 16);
INSERT INTO tenants VALUES (13, 'Watson', 2000, 16);
INSERT INTO tenants VALUES (14, 'Fries', 2000, 16);
INSERT INTO tenants VALUES (15, 'Khaira', 2003, 18);
INSERT INTO tenants VALUES (16, 'Archibald', 1995, 20);
INSERT INTO tenants VALUES (17, 'Chiasson', 2005, 21);
INSERT INTO tenants VALUES (18, 'Russel', 2002, 23);
INSERT INTO tenants VALUES (19, 'Jackson', 2002, 23);