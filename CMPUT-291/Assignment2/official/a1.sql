SELECT uid
FROM ubadges
WHERE bname = 'gold'

INTERSECT

SELECT poster
FROM posts,questions
WHERE posts.pid = questions.pid