SELECT
  subscription_type,
  listening_time,
  COUNT(DISTINCT (user_id)) AS user_count
FROM
  users
GROUP BY
  1,
  2
ORDER BY
  1 ASC,
  3 DESC