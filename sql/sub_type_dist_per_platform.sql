WITH
  sub_type_dist_per_platform AS (
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
  )
SELECT
  streaming_platform,
  subscription_type,
  user_count,
  100.0 * user_count / SUM(user_count) OVER (
    PARTITION BY
      streaming_platform
  ) AS user_count_pct
FROM
  sub_type_dist_per_platform