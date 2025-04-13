SELECT
  streaming_platform,
  AVG(minutes_streamed_per_day) AS avg_mins_streamed_per_day
FROM
  users
GROUP BY
  1
ORDER BY
  2 DESC