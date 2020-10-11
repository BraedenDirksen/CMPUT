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