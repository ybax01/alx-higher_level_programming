-- List all shows from hbtn_0d_tvshows_rate by their rating sum
SELECT tv_shows.title, SUM(ratings.rating) AS rating
FROM tv_shows
JOIN ratings ON tv_shows.id = ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
