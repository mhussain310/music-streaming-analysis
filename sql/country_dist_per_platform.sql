WITH
  country_dist_per_platform AS (
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
  )
SELECT
  streaming_platform,
  country,
  user_count,
  100.0 * user_count / SUM(user_count) OVER (
    PARTITION BY
      streaming_platform
  ) AS user_count_pct
FROM
  country_dist_per_platform