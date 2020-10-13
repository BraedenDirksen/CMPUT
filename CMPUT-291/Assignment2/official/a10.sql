SELECT DISTINCT uCount.city, user_amount, gold_amount, avgMonthly_questions_per_user, votes_per_month
    FROM( SELECT users.city, COUNT(*) AS user_amount
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
        SELECT users.city, avg(Monthly_questions_per_user) AS avgMonthly_questions_per_user
            FROM (SELECT DISTINCT uid, count(*) AS Monthly_questions_per_user
                FROM questioninfo
                WHERE uid in (SELECT q.uid FROM questioninfo q)
                GROUP BY uid) as mqpu, users
            WHERE users.uid = mqpu.uid
                ) AS monthlyquestions ON uCount.city = monthlyquestions.city
    LEFT JOIN(
        SELECT city, votes_per_month
            FROM users, (SELECT DISTINCT uid, sum(voteCnt) AS votes_per_month
                FROM questioninfo
                GROUP BY uid) as u
            WHERE users.uid = u.uid
            ) AS mv ON mv.city = uCount.city
