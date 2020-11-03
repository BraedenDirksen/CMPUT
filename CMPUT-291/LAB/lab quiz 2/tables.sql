-- CMPUT 291 Fall 2019 Lab Quiz 2
-- create and populate your database using this file

drop table if exists cats;
drop table if exists food;
drop table if exists favourite;

create table cats(
    name    char(10),
    gender  char(1),
    age     integer,
    breed   char(50),
    color   char(20),
    PRIMARY KEY (name)
);

create table food(
    productID   integer,
    brand       char(10),
    type        char(10),
    flavor      char(10),
    PRIMARY KEY (productID)
);


create table favourite(
    catname     char(10),
    productID   integer,
    PRIMARY KEY (catname, productID),
    FOREIGN KEY (catname) REFERENCES cats(name),
    FOREIGN KEY (productID) REFERENCES food(productID)
);

insert into cats values ('Samba', 'f', 5, 'domestic shorthair', 'brown');
insert into cats values ('Salem', 'm', 5, 'british shorthair', 'grey');
insert into cats values ('Sonny', 'm', 2, 'british shorthair', 'grey');
insert into cats values ('Oreo', 'm', 6, 'bobtail', 'dark grey');
insert into cats values ('Chili', 'm', 10, 'domestic shorthair', 'black');
insert into cats values ('Waltz', 'f', 4, 'domestic shorthair', 'brown');
insert into cats values ('Romeo', 'm', 8, 'british shorthair', 'brown');
insert into cats values ('Riley', 'f', 9, 'domestic shorthair', 'brown');


insert into food values (1, 'purina', 'canned', 'chicken');
insert into food values (2, 'purina', 'dry', 'fish');
insert into food values (3, 'purina', 'canned', 'salmon');
insert into food values (4, 'purina', 'dry', 'chicken');
insert into food values (5, 'hills', 'dry', 'fish');
insert into food values (6, 'hills', 'dry', 'salmon');
insert into food values (7, 'hills', 'dry', 'chicken');
insert into food values (8, 'hills', 'dry', 'fish');
insert into food values (9, 'hills', 'dry', 'chicken');
insert into food values (10, 'freedom', 'dry', 'chicken');
insert into food values (11, 'freedom', 'canned', 'salmon');
insert into food values (12, 'freedom', 'dry', 'fish');
insert into food values (13, 'freedom', 'dry', 'salmon');

insert into favourite values ('Samba', 3);
insert into favourite values ('Samba', 5);
insert into favourite values ('Samba', 7);
insert into favourite values ('Salem', 3);
insert into favourite values ('Salem', 4);
insert into favourite values ('Salem', 6);
insert into favourite values ('Sonny', 2);
insert into favourite values ('Chili', 7);
insert into favourite values ('Oreo', 6);
insert into favourite values ('Waltz', 1);
insert into favourite values ('Waltz', 2);
insert into favourite values ('Waltz', 3);
insert into favourite values ('Riley', 10);
insert into favourite values ('Romeo', 13);