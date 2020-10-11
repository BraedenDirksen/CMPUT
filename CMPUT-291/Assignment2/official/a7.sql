SELECT DISTINCT pdate ,ptag as'most popular tag',aposts as'amount of posts'
FROM posts
INNER JOIN (SELECT pdate, tag as ptag, COUNT(*) as aposts
            FROM posts, tags
            WHERE posts.pid = tags.pid
            group by tags.tag
            ORDER BY count(*) DESC
            LIMIT 1) USING(pdate)