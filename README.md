

数据库

mysql -hrds9xpp1484ti2j7r39f.mysql.rds.aliyuncs.com -uhyena_admin -phqTvdrzkbP3lr5hg

redis
IP：10.25.174.54

端口： 6379

库：5

gunicorn -w 4 -b 127.0.0.1:5100 main:app --access-logfile /data/hyena/logs/access.logs --error-logfile /data/hyena/logs/error.logs &