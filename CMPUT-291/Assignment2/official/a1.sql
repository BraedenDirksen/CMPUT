--complete and working
SELECT uid
FROM ubadges, badges
WHERE ubadges.bname = badges.bname
AND badges.type = 'gold'

INTERSECT

SELECT poster
FROM posts,questions
WHERE posts.pid = questions.pid