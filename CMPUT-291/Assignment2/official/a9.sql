<<<<<<< HEAD


=======
-- complete and working correctly
>>>>>>> 5437e69d6c06cffadc1e262e56b3f40e4d923556
CREATE VIEW questioninfo(pid,uid,theaid,voteCnt,ansCnt) AS
    SELECT qinfo.pid,poster,qinfo.theaid, voteCnt, ansCnt
        FROM
            (SELECT DISTINCT posts.pid, poster,theaid
            FROM posts, questions
            WHERE posts.pid IN(SELECT pid FROM questions)
            AND pdate BETWEEN datetime('now', '-1 month') AND datetime('now', 'localtime')
            GROUP BY posts.pid) AS qinfo
        LEFT JOIN
            (SELECT questions.pid,count(*) AS ansCnt
            FROM answers, questions
            WHERE answers.qid = questions.pid
            GROUP BY questions.pid) AS ans
            ON ans.pid = qinfo.pid
        LEFT JOIN
            (SELECT questions.pid,count(*) AS voteCnt
            FROM votes, questions
            WHERE votes.pid = questions.pid
            GROUP BY questions.pid) AS vote
            ON vote.pid = qinfo.pid