
SELECT DISTINCT uid, count(*) AS Monthly_questions
FROM questioninfo
WHERE uid in (SELECT q.uid FROM questioninfo q)
GROUP BY uid