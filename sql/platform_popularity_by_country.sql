WITH
  platform_rankings_per_country AS (
    SELECT
      country,
      streaming_platform,
      COUNT(DISTINCT user_id) AS user_count,
      RANK() OVER (
        PARTITION BY
          country
        ORDER BY
          COUNT(DISTINCT user_id) DESC
      ) AS platform_rank
    FROM
      users
    GROUP BY
      1,
      2
  )
SELECT
  country,
  streaming_platform,
  user_count,
  platform_rank,
  100.0 * user_count / SUM(user_count) OVER (
    PARTITION BY
      country
  ) AS user_count_pct
FROM
  platform_rankings_per_country