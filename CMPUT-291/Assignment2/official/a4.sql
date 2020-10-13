-- giving extra u002 and u016
SELECT DISTINCT poster as user_id
FROM posts
WHERE pid in (SELECT questions.pid FROM questions)
AND 2 < (SELECT count(*)
FROM answers
WHERE posts.pid IN (SELECT qid FROM answers)
GROUP BY answers.qid);

SELECT DISTINCT poster, count(*)
FROM answers, posts
WHERE posts.pid in (select qid from answers)
GROUP BY answers.qid