-- complete and working
SELECT DISTINCT posts.pid, title
FROM posts,tags t1, tags t2, questions
WHERE title LIKE '%relational database%'
OR t1.pid = t2.pid
AND posts.pid = t1.pid
AND t1.tag like '%relational%'
AND t2.tag like '%database%'

EXCEPT 

SELECT DISTINCT posts.pid, title
FROM answers, posts
WHERE answers.pid = posts.pid