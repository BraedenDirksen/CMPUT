.print Question 4 - bdirksen
-- giving extra u002 and u016
SELECT DISTINCT poster as user_id
FROM posts
WHERE pid in (SELECT questions.pid FROM questions)
AND 2 < (SELECT count(*)
FROM answers
WHERE posts.pid in( answers.qid)
GROUP BY answers.qid)

