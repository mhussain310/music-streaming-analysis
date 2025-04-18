WITH
  listening_times_per_sub_type AS (
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
  )
SELECT
  subscription_type,
  listening_time,
  user_count,
  100.0 * user_count / SUM(user_count) OVER (
    PARTITION BY
      subscription_type
  ) AS user_count_pct
FROM
  listening_times_per_sub_type