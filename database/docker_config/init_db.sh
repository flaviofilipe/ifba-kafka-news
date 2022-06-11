echo "Creating database..."
psql -q -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" < docker-entrypoint-initdb.d/notices.sql