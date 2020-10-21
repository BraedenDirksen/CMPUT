.print Question 10 - bdirksen
--complete mostly working
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
