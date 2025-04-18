WITH
  stream_by_age_group AS (
    SELECT
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
      1
  ),
  total_users AS (
    SELECT
      SUM(DISTINCT (user_count)) AS total_users
    FROM
      stream_by_age_group
  )
SELECT
  age_group,
  user_count,
  100.0 * user_count / total_users AS user_count_pct
FROM
  stream_by_age_group,
  total_users