SELECT DISTINCT users.city, user_amount, gold_amount--, avgMonthly_questions_per_user, votes_per_month
    FROM users
    LEFT JOIN(
        SELECT users.city, COUNT(*) AS user_amount
            FROM users
            WHERE users.city in(SELECT u1.city FROM users u1)
            GROUP BY users.city
        ) AS uCount ON ucount.city = users.city
    LEFT JOIN(
        SELECT users.city, COUNT(*) AS gold_amount
            FROM users, badges, ubadges
            WHERE users.uid = ubadges.uid
            AND ubadges.bname = badges.bname
            AND badges.type = 'gold'
            GROUP BY users.city
        ) AS goldCount ON goldCount.city = users.city
    LEFT JOIN(
        SELECT users.city, avg(Monthly_questions) AS avgMonthly_questions_per_user
            FROM (SELECT DISTINCT uid, count(*) AS Monthly_questions_per_user
                FROM questioninfo
                WHERE uid in (SELECT q.uid FROM questioninfo q)
                GROUP BY uid), users
            WHERE
                ) AS monthlyquestions ON users.city = monthlyquestions.city
