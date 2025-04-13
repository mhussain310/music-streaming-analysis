SELECT
  subscription_type,
  SUM(number_of_songs_liked) AS total_songs_liked
FROM
  users
GROUP BY
  1
ORDER BY
  2 DESC