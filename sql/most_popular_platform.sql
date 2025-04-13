WITH
  total_users AS (
    SELECT
      COUNT(user_id) AS total_users
    FROM
      users
  )
SELECT
  streaming_platform,
  COUNT(user_id) AS user_count,
  100.0 * COUNT(user_id) / total_users AS user_count_pct
FROM
  users,
  total_users
GROUP BY
  1
ORDER BY
  2 DESC,
  1 ASC;