WITH
  listening_times_by_country AS (
    SELECT
      country,
      listening_time,
      COUNT(DISTINCT (user_id)) AS user_count
    FROM
      users
    GROUP BY
      1,
      2
  )
SELECT
  country,
  listening_time,
  user_count,
  100.0 * user_count / SUM(user_count) OVER (
    PARTITION BY
      country
  ) AS user_count_pct
FROM
  listening_times_by_country