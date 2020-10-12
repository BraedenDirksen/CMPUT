.echo on
--Question 1
SELECT uid
FROM ubadges, badges
WHERE ubadges.bname = badges.bname
AND badges.type = 'gold'

INTERSECT

SELECT poster
FROM posts,questions
WHERE posts.pid = questions.pid
--Question 2
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
--Question 3
SELECT p1.pid, p1.pdate
FROM posts p1, posts p2, questions, answers
WHERE p1.pid = questions.pid
AND p2.pid = answers.pid
AND answers.qid = p1.pid
AND 3 >= (julianday(p2.pdate) - julianday(p1.pdate))
--Question 4
SELECT DISTINCT poster as user_id
FROM posts
WHERE pid in (SELECT questions.pid FROM questions)
AND 2 < (SELECT count(*)
FROM answers
WHERE posts.pid in( answers.qid)
GROUP BY answers.qid)
--Question 5
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
--Question 6
SELECT DISTINCT tags.tag, vote_amount, post_amount
    FROM tags
    LEFT JOIN(select DISTINCT tag, COUNT(*) as vote_amount from votes, tags
            WHERE tags.pid = votes.pid
            group by tag) as v
    ON v.tag = tags.tag
    LEFT JOIN 
        (SELECT tag, COUNT(*) as post_amount FROM posts, tags
        WHERE posts.pid = tags.pid
        group by tag) as p
        ON p.tag = tags.tag
    ORDER by vote_amount DESC
    LIMIT 3
--Question 7
SELECT DISTINCT posts.pdate ,ptag as most_popular_tag, aposts AS amount_of_posts
    FROM posts
    left JOIN (SELECT pdate, tag as ptag, COUNT(*) as aposts
                FROM posts, tags
                WHERE posts.pid = tags.pid
                group by tags.tag
                ORDER BY count(*) DESC
                ) x on x.pdate = posts.pdate
    WHERE most_popular_tag IS NOT NULL
    OR amount_of_posts IS NOT NULL
    ORDER BY posts.pdate DESC
--Question 8
SELECT x.user_id, x.question_amount, x.answer_amount, x.vote_out_amount, x.vote_in_amount
FROM (SELECT users.uid as user_id, question_amount, answer_amount, vote_out_amount, vote_in_amount
        FROM users

        LEFT JOIN (SELECT uid, count(uid) as vote_out_amount
                    FROM votes
                    WHERE uid in (SELECT uid FROM users)
                    GROUP BY uid) as v_out
        on users.uid = v_out.uid

        LEFT JOIN (SELECT poster, count(pid) as answer_amount
                    FROM posts
                    WHERE pid in (SELECT pid FROM answers)
                    GROUP BY poster) as a
        on users.uid = a.poster

        LEFT JOIN (SELECT poster, count(pid) as question_amount
                    FROM posts
                    WHERE pid in (SELECT pid FROM questions)
                    GROUP BY poster) as q
        on users.uid = q.poster

        LEFT JOIN (SELECT poster, count(*) as vote_in_amount
                    FROM posts, votes
                    where posts.pid = votes.pid
                    group by posts.poster) as v_in
        on users.uid = v_in.poster) x
WHERE x.question_amount IS NOT NULL
OR x.answer_amount IS NOT NULL
OR x.vote_out_amount IS NOT NULL
OR x.vote_in_amount IS NOT NULL
--Question 9
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
--Question 10
SELECT uCount.city, user_amount,IFNULL(gold_amount, 0) gold_amount, IFNULL(avgMonthly_questions_per_user,0) avgMonthly_questions_per_user,IFNULL(votes_last_month,0) votes_last_month
    FROM(SELECT users.city, COUNT(*) AS user_amount
            FROM users
            WHERE users.city in(SELECT u1.city FROM users u1)
            GROUP BY users.city
        ) AS uCount
    LEFT JOIN(
        SELECT users.city, COUNT(*) AS gold_amount
            FROM users, badges, ubadges
            WHERE users.uid = ubadges.uid
            AND ubadges.bname = badges.bname
            AND badges.type = 'gold'
            GROUP BY users.city
        ) AS goldCount ON goldCount.city = uCount.city
    LEFT JOIN(
        SELECT users.city, avg(Monthly_questions_per_user) as avgMonthly_questions_per_user
            FROM(SELECT users.city, q.uid, count(*) AS Monthly_questions_per_user
                    FROM questioninfo q, users
                    WHERE q.uid in (SELECT q.uid FROM questioninfo q)
                    AND users.uid = q.uid
                    GROUP BY users.uid) x, users
            WHERE x.city = users.city
            group by users.city) AS monthlyquestions ON uCount.city = monthlyquestions.city
    LEFT JOIN(
        SELECT DISTINCT city, votes_last_month
            FROM users, (SELECT DISTINCT uid, sum(voteCnt) AS votes_last_month
                FROM questioninfo
                GROUP BY uid) as u
            WHERE users.uid = u.uid
            ) AS mv ON mv.city = uCount.city
