import pymysql
from flask import Flask,render_template,request
from flask_bootstrap import Bootstrap

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/first",methods=['GET','POST'])
def first():
    userid=request.form.get('userid',type=str)
    print(userid)
    db = pymysql.connect("192.168.57.114","mudou","123456","movies" )
    cursor = db.cursor()
    sql ='''select movies.title,ratings.rating,genomescores.tagId,genomescores.relevance 
    from ratings,genomescores,movies 
    where ratings.userId='%s'
    and genomescores.movieId=movies.movieId
    and movies.movieId=ratings.movieId
    order by ratings.timestamp desc
    limit 3;'''%userid
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
          title = row[0]
          rating=row[1]
          tagid=row[2]
          relevance=row[3]
          #打印结果
          print('title = %s,rating=%s,tagid=%s,relevance=%s'%(title,rating,tagid,relevance))
    db.close()
    return render_template('indexa.html',rs=result)

@app.route("/second",methods=['GET','POST'])
def second():
    keyword=request.form.get('keyword',type=str)
    print(keyword)
    db = pymysql.connect("192.168.57.114","mudou","123456","movies" )
    cursor = db.cursor()
    sql ='''select movieId,title,genres
         from movies
         where movies.title like "%%%s%%";'''%keyword
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
          movieid=row[0]
          title=row[1]
          genres=row[2]
          #打印结果
          print('movieid=%s,title=%s,genres=%s'%(movieid,title,genres))
    db.close()
    return render_template('indexb.html',rs=result)

@app.route("/third",methods=['GET','POST'])
def third():
    tag=request.form.getlist('tag',type=str)
    print(tag)
    #gender=gender.lstrip('[')
    #gender=gender.rstrip(']')
    tag="".join(tag)
    print(tag)
    db = pymysql.connect("192.168.57.114","mudou","123456","movies" )
    cursor = db.cursor()
    sql ='''select distinct movies.title 
            from tags,ratings,movies
            where tags.tag='%s'
            and tags.movieId=ratings.movieId
            and ratings.movieId=movies.movieId
            order by ratings.rating
            limit 20;'''%tag
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
          title= row[0]
          #打印结果
          print('title= %s'%(title))
    db.close() 
    return render_template('indexc.html',rs=result)

@app.route("/fourth",methods=['GET','POST'])
def fourth():
    gender=request.form.getlist('gender',type=str)
    #print(gender)
    gender="".join(gender)
    print(gender)
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
    return render_template('indexd.html',rs=result)
if __name__=='__main__':
    app.run(debug=True,threaded=True)