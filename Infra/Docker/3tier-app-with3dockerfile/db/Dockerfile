# Use a MySQL base image
FROM mysql:latest

# Copy the database initialization script
# COPY init.sql /docker-entrypoint-initdb.d/

# Expose the database on port 3306
EXPOSE 3306

# Run the database
CMD ["mysqld"]

# docker image 
# docker build -t my-db . <-db폴더로 이동 후 입력

# docker 실행(mysql은 pw설정 필요)
# docker run --name my-db -e MY_SQL_ROOT_PASSWORD=1q2w3e4r -d -p 3306:3306 mysql:latest