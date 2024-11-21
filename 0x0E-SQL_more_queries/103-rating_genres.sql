-- List all genres in hbtn_0d_tvshows_rate by their rating sum
SELECT tv_genres.name, SUM(ratings.rating) AS rating
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN ratings ON tv_show_genres.show_id = ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
