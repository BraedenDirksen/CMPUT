
.print Question 9 - bdirksen
-- complete and working correctly
CREATE VIEW questioninfo(pid,uid,theaid,voteCnt,ansCnt) AS
    SELECT qinfo.pid,poster,qinfo.theaid, IFNULL(voteCnt,0) voteCnt, IFNULL(ansCnt,0) ansCnt
        FROM
            (SELECT DISTINCT posts.pid, poster,theaid
            FROM posts, questions
            WHERE posts.pid IN(SELECT pid FROM questions)
            AND posts.pid = questions.pid
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