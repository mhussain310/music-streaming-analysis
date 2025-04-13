SELECT
  streaming_platform,
  subscription_type,
  COUNT(DISTINCT (user_id)) AS user_count
FROM
  users
GROUP BY
  1,
  2
ORDER BY
  1 asc,
  3 DESC