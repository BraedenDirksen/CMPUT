


with RECURSIVE select *
from posts
where posts.title like '%what%'
or posts.body like '%what%'
or posts.pid in (select pid from tags where tags.tag like '%what%')