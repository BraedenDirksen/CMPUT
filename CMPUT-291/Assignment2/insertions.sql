INSERT INTO users
VALUES (1,'braeden','edmonton',DATE('2020-10-04')),
(2,'danny','edmonton',DATE('2020-10-04')),
(3,'brandon','surrey',DATE('2020-10-04')),
(4,'mathew','regina',DATE('2020-10-04'));

INSERT INTO posts
VALUES (1,DATE('2020-10-04'),'question post','this is a question post',1),
(2,DATE('2020-10-04'),'answer post','this is a answer post',1),
(3,DATE('2020-10-04'),'relational database','this is a answer post',2),
(4,DATE('2020-10-04'),'answer post','this is a answer post 2',1),
(5,DATE('2020-10-04'),'question post','this is a question post',2)
;

INSERT INTO questions
VALUES (1,2),(2,4),(5,NULL);

INSERT INTO answers
VALUES (2,1),(4,1),(3,5);

INSERT INTO badges
VALUES ('gold','gold'),
('silver','silver'),
('bronze','bronze');

INSERT INTO ubadges
VALUES (1,DATE(2020-10-04),'gold'),
(2,DATE(2020-10-04),'gold'),
(4,DATE(2020-10-04),'gold');

INSERT INTO tags
VALUES (2,'relational'),
(2,'database');

INSERT INTO votes
VALUES (5,1,DATE(2020-10-06),1),
(5,1,DATE(2020-10-06),2),
(5,1,DATE(2020-10-06),3),
(5,1,DATE(2020-10-06),4)