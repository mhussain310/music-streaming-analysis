SELECT
  streaming_platform,
  country,
  COUNT(DISTINCT (user_id)) AS user_count
FROM
  users
GROUP BY
  1,
  2
ORDER BY
  1 asc,
  3 DESC