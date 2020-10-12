.print Question 7 - bdirksen
-- COMPLETE should work needs further testing
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