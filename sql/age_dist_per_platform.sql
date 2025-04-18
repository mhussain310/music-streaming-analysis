WITH
  age_dist_per_platform AS (
    SELECT
      streaming_platform,
      CASE
        WHEN age < 13 THEN 'Child'
        WHEN age < 18 THEN 'Teenager'
        WHEN age < 25 THEN 'Young Adult'
        WHEN age < 45 THEN 'Adult'
        WHEN age < 65 THEN 'Middle-Aged'
        ELSE 'Senior'
      END AS age_group,
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
  age_group,
  user_count,
  100.0 * user_count / SUM(user_count) OVER (
    PARTITION BY
      streaming_platform
  ) AS user_count_pct
FROM
  age_dist_per_platform