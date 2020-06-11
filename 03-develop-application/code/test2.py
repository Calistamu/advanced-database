import pymysql
gender="Female"
db = pymysql.connect("192.168.57.114","mudou","123456","movies" )
cursor = db.cursor()
sql ='''select title
            from users,ratings,movies
            where users.gender='%s'
            and users.userId=ratings.userId
            and movies.movieId=ratings.movieId
            order by ratings.rating
            limit 20;'''%gender
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    title= row[0]
          #打印结果
    print('title= %s'%(title))
db.close()
