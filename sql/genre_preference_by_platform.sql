SELECT
  streaming_platform,
  top_genre,
  COUNT(DISTINCT (user_id)) AS user_count
FROM
  users
GROUP BY
  1,
  2
ORDER BY
  2,
  1