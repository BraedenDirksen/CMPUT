.print Question 5 - bdirksen
--complete working correctly
SELECT poster
FROM posts, questions
WHERE posts.pid = questions.pid

INTERSECT

SELECT poster
FROM posts, answers
WHERE posts.pid = answers.pid

INTERSECT

SELECT poster
FROM posts, votes
WHERE posts.pid = votes.pid
AND 3 < 
(SELECT count(poster)
FROM posts, votes
WHERE posts.pid = votes.pid)