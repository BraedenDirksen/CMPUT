CREATE TABLE users(
    uid INTEGER,
    name TEXT,
    city TEXT,
    crdate DATE,
    PRIMARY KEY (uid)
);
CREATE TABLE badges(
    bname TEXT,
    type TEXT,
    PRIMARY KEY (bname)
);
CREATE TABLE ubadges(
    uid INTEGER NOT NULL,
    bdate DATE,
    bname TEXT,
    PRIMARY KEY (uid),
    FOREIGN KEY (uid) REFERENCES users(uid)
);
CREATE TABLE posts(
    pid INTEGER,
    pdate DATE,
    title TEXT,
    body TEXT,
    poster INTEGER,
    PRIMARY KEY (pid),
    FOREIGN KEY (poster) REFERENCES users(uid)
);
CREATE TABLE tags(
    pid INTEGER NOT NULL,
    tag TEXT,
    PRIMARY KEY (pid),
    FOREIGN KEY (pid) REFERENCES posts(pid)
);
CREATE TABLE votes(
    pid INTEGER NOT NULL,
    vno INTEGER,
    vdate DATE,
    uid INTEGER NOT NULL,
    PRIMARY KEY (pid,uid),
    FOREIGN KEY (uid) REFERENCES users(uid),
    FOREIGN KEY (pid) REFERENCES posts(pid)
);
CREATE TABLE questions(
    pid INTEGER NOT NULL,
    theaid INTEGER,
    PRIMARY KEY (pid),
    FOREIGN KEY (pid) REFERENCES posts(pid),
    FOREIGN KEY (theaid) REFERENCES answers(pid)
);
CREATE TABLE answers(
    pid INTEGER NOT NULL,
    qid INTEGER,
    PRIMARY KEY (pid,qid),
    FOREIGN KEY (pid) REFERENCES posts(pid),
    FOREIGN KEY (qid) REFERENCES questions(pid)
)
