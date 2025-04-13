SELECT
  streaming_platform,
  listening_time,
  COUNT(DISTINCT (user_id)) AS user_count
FROM
  users
GROUP BY
  1,
  2
ORDER BY
  1,
  2