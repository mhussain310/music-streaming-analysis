WITH
  genre_preference_by_country AS (
    SELECT
      country,
      top_genre,
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
  country,
  top_genre,
  user_count,
  100.0 * user_count / SUM(user_count) OVER (
    PARTITION BY
      country
  ) AS user_count_pct
FROM
  genre_preference_by_country