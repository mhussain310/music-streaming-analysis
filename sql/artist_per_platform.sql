WITH
  artist_per_platform AS (
    SELECT
      most_played_artist,
      streaming_platform,
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
  most_played_artist,
  streaming_platform,
  user_count,
  100.0 * user_count / SUM(user_count) OVER (
    PARTITION BY
      most_played_artist
  ) AS user_count_pct
FROM
  artist_per_platform