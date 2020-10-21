.print Question 8 - bdirksen
--complete and working correctly
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
