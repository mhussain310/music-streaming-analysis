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
  ),
  most_popular_platform_per_country AS (
    SELECT
      country,
      streaming_platform,
      user_count
    FROM
      platform_rankings_per_country
    WHERE
      platform_rank = 1
  )
SELECT
  streaming_platform,
  COUNT(streaming_platform) AS num_countries_ranked_1st
FROM
  most_popular_platform_per_country
GROUP BY
  1
ORDER BY
  2 desc,
  1 ASC