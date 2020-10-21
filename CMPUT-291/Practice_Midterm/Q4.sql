--tables
CREATE TABLE movies(
    title text,
    category CHAR(15),
    rent_type INTEGER,
    primary key (title)
);
CREATE TABLE classes(
    rent_type INTEGER,
    price FLOAT,
    primary key (rent_type),
    foreign key (rent_type) references movies
);
CREATE TABLE rents(
    customer char(25),
    title text,
    checkout DATE,
    [return] DATE,
    primary key (customer, title),
    foreign key (title) references movies
);
--queries part a
SELECT customers
FROM rents r1, rents r2, movies m1, movies m2
WHERE r1.title = m1.title
AND r2.title = m2.title
and m1.category = 'action'
AND m2.category = 'family'
AND r1.customer = r2.customer
--queries part b
SELECT title, price
FROM movies, classes
WHERE movies.rent_type = classes.rent_type
AND title = '%star%'
ORDER BY price
--queries part c
SELECT m1.category, m2.category
FROM movies m1, movies m2, rents r1, rents r2
WHERE m1.title = r1.title AND m2.title = r2.title
AND m1.category != m2.category AND r1.customer = r2.customer
group by m1.category, m2.category
having count(Distinct r1.customer) >= 5
--queries part d
SELECT rent_type, count(DISTINCT movies.title), count(*)
FROM movies, rents
WHERE movies.title = rents.title
group by rent_type







SELECT movies.rent_type, z, y
FROM movies
LEFT JOIN(SELECT rent_type, count(DISTINCT movies.title) as z, count(*) as y
FROM movies, rents
WHERE movies.title = rents.title
group by rent_type) as x on x.rent_type = movies.rent_type


select rent_type, count(distinct title), count(*)
from classes 
left outer join movies using (rent_type) 
left outer join rents using (title)
group by rent_type;