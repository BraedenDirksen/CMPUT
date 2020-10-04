/* querry one */
SELECT uid
FROM ubadges
WHERE bname = 'gold'

INTERSECT

SELECT poster
FROM posts
WHERE pid IN (SELECT pid FROM questions)

/*querry two */