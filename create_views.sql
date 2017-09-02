CREATE VIEW popularlog AS
		SELECT path, count(*) AS viewed
		FROM log
		WHERE status='200 OK'
		AND path LIKE '/article/%'
		GROUP BY path
		ORDER BY viewed DESC;

CREATE VIEW daily_request AS
		SELECT count(*) AS num,
		time::date AS daily
		FROM log
		GROUP BY daily
		ORDER BY daily DESC;
CREATE VIEW daily_error AS
		SELECT count(*) AS err_num,
		time::date AS daily
		FROM log
		WHERE log.status like '4%'
		GROUP BY daily
		ORDER BY daily DESC;
