SELECT
  top_genre,
  AVG(repeat_song_rate_pct) AS avg_repeat_rate
FROM
  users
GROUP BY
  1
ORDER BY
  2 DESC