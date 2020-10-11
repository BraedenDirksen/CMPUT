
DROP VIEW IF EXISTS questioninfo;

CREATE VIEW questioninfo(pid,uid,theaid,voteCnt,ansCnt) AS
    SELECT DISTINCT questions.pid,poster,qinfo.theaid, voteCnt, ansCnt
        FROM questions
        LEFT JOIN
            (SELECT questions.pid,poster,theaid
            FROM posts, questions, answers, votes
            WHERE posts.pid = questions.pid
            GROUP BY questions.pid) AS qinfo
            ON qinfo.pid = questions.pid
        LEFT JOIN
            (SELECT questions.pid,count(*) AS ansCnt
            FROM answers, questions
            WHERE answers.qid = questions.pid
            GROUP BY questions.pid) AS ans
            ON ans.pid = questions.pid
        LEFT JOIN
            (SELECT questions.pid,count(*) AS voteCnt
            FROM votes, questions
            WHERE votes.pid = questions.pid
            GROUP BY questions.pid) AS vote
            ON vote.pid = questions.pid