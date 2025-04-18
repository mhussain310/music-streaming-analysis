WITH
  listening_times_by_platform AS (
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
  )
SELECT
  streaming_platform,
  listening_time,
  user_count,
  100.0 * user_count / SUM(user_count) OVER (
    PARTITION BY
      streaming_platform
  ) AS user_count_pct
FROM
  listening_times_by_platform