WITH
  genre_preference_by_platform AS (
    SELECT
      streaming_platform,
      top_genre,
      COUNT(DISTINCT (user_id)) AS user_count
    FROM
      users
    GROUP BY
      1,
      2
    ORDER BY
      2 ASC,
      3 DESC
  )
SELECT
  streaming_platform,
  top_genre,
  user_count,
  100.0 * user_count / SUM(user_count) OVER (
    PARTITION BY
      top_genre
  ) AS user_count_pct
FROM
  genre_preference_by_platform