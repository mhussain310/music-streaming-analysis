WITH
  sub_type_per_age_group AS (
    SELECT
      CASE
        WHEN age < 13 THEN 'Child'
        WHEN age < 18 THEN 'Teenager'
        WHEN age < 25 THEN 'Young Adult'
        WHEN age < 45 THEN 'Adult'
        WHEN age < 65 THEN 'Middle-Aged'
        ELSE 'Senior'
      END AS age_group,
      subscription_type,
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
  age_group,
  subscription_type,
  user_count,
  100.0 * user_count / SUM(user_count) OVER (
    PARTITION BY
      age_group
  ) AS user_count_pct
FROM
  sub_type_per_age_group