INSERT INTO users
VALUES (1,'braeden','edmonton',DATE('2020-10-04')),
(2,'danny','edmonton',DATE('2020-10-04')),
(3,'brandon','surrey',DATE('2020-10-04')),
(4,'mathew','regina',DATE('2020-10-04'));

INSERT INTO posts
VALUES (1,DATE(2020-10-04),'question post','this is a question post',1),
(2,DATE(2020-10-04),'answer post','this is a answer post',2);

INSERT INTO questions
VALUES (1,2);

INSERT INTO answers
VALUES (2,1);

INSERT INTO badges
VALUES ('gold','gold'),
('silver','silver'),
('bronze','bronze');

INSERT INTO ubadges
VALUES (1,DATE(2020-10-04),'gold'),
(2,DATE(2020-10-04),'gold'),
(4,DATE(2020-10-04),'gold')