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
/*
u001 6 10 20 37 *
u002 3 6 16 19 *
u003 1 3 10 9 *
u004 3 4 11 13 *
u005 3 4 10 7 *
u006 0 2 9 3 *
u007 0 1 7 6 *
u008 1 0 6 0 *
u009 0 1 9 0 *
u010 0 0 8 0
u011 0 0 2 0
u012 0 0 1 0
u014 0 0 1 0
u015 0 0 4 0
u016 2 3 8 28 *
*/