SELECT
  CASE
    WHEN age < 13 THEN 'Child'
    WHEN age < 18 THEN 'Teenager'
    WHEN age < 25 THEN 'Young Adult'
    WHEN age < 45 THEN 'Adult'
    WHEN age < 65 THEN 'Middle-Aged'
    ELSE 'Senior'
  END AS age_group,
  AVG(minutes_streamed_per_day) AS avg_mins_streamed_per_day
FROM
  users
GROUP BY
  1
ORDER BY
  2 DESC