SELECT poster as user_id
FROM posts, questions
WHERE posts.pid = questions.pid
AND 2 < (SELECT count(*)
FROM answers
WHERE posts.pid = answers.qid)