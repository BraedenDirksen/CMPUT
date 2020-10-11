-- not working properly random NULLs
SELECT DISTINCT pdate ,ptag as'most popular tag',aposts as'amount of posts'
    FROM posts
    left JOIN (SELECT pdate, tag as ptag, COUNT(*) as aposts
                FROM posts, tags
                WHERE posts.pid = tags.pid
                group by tags.tag
                ORDER BY count(*) DESC
                ) USING(pdate)
    ORDER BY pdate DESC