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