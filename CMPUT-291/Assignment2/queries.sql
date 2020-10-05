/* querry one COMPLETE*/
SELECT uid
FROM ubadges
WHERE bname = 'gold'

INTERSECT

SELECT poster
FROM posts
WHERE pid IN (SELECT pid FROM questions);

/*querry two */
SELECT pid, title
FROM posts
WHERE title LIKE '%relational database%'
OR (pid IN (SELECT pid
FROM tags
WHERE tag LIKE "%relational%")
AND pid IN (SELECT pid
FROM tags
WHERE tag LIKE "%atabase%"));

/*querry three COMPLETE*/
SELECT p1.pid, p1.pdate
FROM posts p1, posts p2, questions, answers
WHERE p1.pid = questions.pid
AND p2.pid = answers.pid
AND answers.qid = p1.pid
AND 3 >= (julianday(p2.pdate) - julianday(p1.pdate))

/*querry four */

/*querry five */

/*querry six */

/*querry seven */

/*querry eight */

/*querry nine */

/*querry ten */
