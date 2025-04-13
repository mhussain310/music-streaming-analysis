WITH
  repeat_rate_per_genre AS (
    SELECT
      top_genre,
      AVG(repeat_song_rate_pct) AS avg_repeat_rate_per_genre
    FROM
      users
    GROUP BY
      1
    ORDER BY
      2 DESC
  )
SELECT
  u.top_genre,
  CASE
    WHEN age < 13 THEN 'Child'
    WHEN age < 18 THEN 'Teenager'
    WHEN age < 25 THEN 'Young Adult'
    WHEN age < 45 THEN 'Adult'
    WHEN age < 65 THEN 'Middle-Aged'
    ELSE 'Senior'
  END AS age_group,
  AVG(repeat_song_rate_pct) AS avg_repeat_rate_per_age_group,
  avg_repeat_rate_per_genre
FROM
  users u
  LEFT JOIN repeat_rate_per_genre rrpg ON u.top_genre = rrpg.top_genre
GROUP BY
  1,
  2
ORDER BY
  4 DESC