SELECT DISTINCT posts.poster as user_id, question_amount, answer_amount, vote_out_amount, vote_in_amount
    FROM posts

    LEFT JOIN (SELECT poster, count(pid) as answer_amount
                FROM posts
                WHERE pid in (SELECT pid FROM answers)
                GROUP BY poster) as a
    on posts.poster = a.poster

    LEFT JOIN (SELECT poster, count(pid) as question_amount
                FROM posts
                WHERE pid in (SELECT pid FROM questions)
                GROUP BY poster) as q
    on posts.poster = q.poster

    LEFT JOIN (SELECT uid, count(uid) as vote_out_amount
                FROM votes
                WHERE uid in (SELECT uid FROM users)
                GROUP BY uid) as v_out
    on posts.poster = v_out.uid

    LEFT JOIN (SELECT poster, count(*) as vote_in_amount
                FROM posts, votes
                where posts.pid = votes.pid
                group by posts.poster) as v_in
    on posts.poster = v_in.poster