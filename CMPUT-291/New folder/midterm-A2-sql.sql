-- Fill your name and CCID, and add your answers to each question.
-- YOUR-NAME (YOUR-CCID)

-- Add your SQL queries for each question here.
-- Q1
SELECT users.uid, name
FROM users, loans
WHERE users.uid = loans.uid
AND retDAte IS NULL;
-- Q2
SELECT users.city, COUNT(*)
FROM users
WHERE users.uid IN (SELECT loans.uid FROM loans)
GROUP BY users.city;
-- Q3
SELECT title, author
FROM books, loans
WHERE books.bid = loans.bid
GROUP BY title,author
HAVING count(*) > 3;
-- Q4
SELECT author
FROM books, loans
WHERE books.bid = loans.bid
group by author
having count(*) = (SELECT count(*) from books b1 where b1.author = books.author group by b1.author);

