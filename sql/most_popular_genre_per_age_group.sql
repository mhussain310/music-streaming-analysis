WITH
  age_group_with_genre_preferences AS (
    SELECT
      CASE
        WHEN age < 13 THEN 'Child'
        WHEN age < 18 THEN 'Teenager'
        WHEN age < 25 THEN 'Young Adult'
        WHEN age < 45 THEN 'Adult'
        WHEN age < 65 THEN 'Middle-Aged'
        ELSE 'Senior'
      END AS age_group,
      top_genre,
      COUNT(DISTINCT (user_id)) AS user_count
    FROM
      users
    GROUP BY
      1,
      2
    ORDER BY
      2,
      1
  ),
  max_count_per_age_group AS (
    SELECT
      age_group,
      MAX(user_count) AS max_count
    FROM
      age_group_with_genre_preferences
    GROUP BY
      1
  ),
  total_user_per_age_group AS (
    SELECT
      age_group,
      SUM(user_count) AS total_user_per_age_group
    FROM
      age_group_with_genre_preferences
    GROUP BY
      1
  )
SELECT
  mag.age_group,
  top_genre,
  max_count,
  total_user_per_age_group,
  100.0 * max_count / total_user_per_age_group AS max_count_pct
FROM
  max_count_per_age_group mag
  INNER JOIN total_user_per_age_group tag ON mag.age_group = tag.age_group
  INNER JOIN age_group_with_genre_preferences agp ON mag.max_count = agp.user_count
  AND mag.age_group = agp.age_group