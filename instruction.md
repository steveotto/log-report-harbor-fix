Analyze the Apache-style access log located at `/app/access.log` and write the results as a JSON object to `/app/report.json`.

The completed report must satisfy these success criteria:

1. `total_requests` is an integer equal to the number of non-empty access-log entries.
2. `unique_ips` is an integer equal to the number of distinct client IP addresses appearing as the first field of an access-log entry.
3. `top_path` is a string containing the request path that appears most often in the log.
4. The output is valid JSON containing exactly the keys `total_requests`, `unique_ips`, and `top_path`.
