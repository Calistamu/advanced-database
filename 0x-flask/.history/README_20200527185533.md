---
date: 2020-05-27
---

# Project: Flask-Bootstrap Based Web Application Development

## Q&A

### 为什么选择Flask？

1. 首先明确，FLask是一种`web framework`，而一个web应用至少应当包括`web server`和`web framework`；前者承担端口监听和接受请求的任务，而后者承担路由，业务逻辑等任务。
2. 相比于Django，Flask是一个轻量型的框架，更适合快速开发
3. Flask同时对sql、bootstrap有着较好的支持

### 为什么选择Bootstrap？

1. 某种意义上看，Bootstrap是一种面向后端程序员的前端开发框架，适合于缺少前端开发经验的后端人员快速制作一个看得过眼的Web页面
2. Bootstrap有着大量现成模板

### 与数据库连接？

- 一般Python中与数据库连接的方式是多样的，例如`Sqlite`、`pymysql`、`SQLAlchemy`等
- 这里选择了与FLask兼容性较好的`SQLAlchemy`

### I/O模型选择

0. 对于web应用而言，大部分时候的性能瓶颈并不是在程序应用本身，而在于I/O与sql请求。例如在一个同步阻塞I/O模型下，如果前一个请求没能完成网络传输或sql请求，那么后面的线程都会被阻塞，这大大降低了效率
1. 对于**CPython**来说，由于GIL(全局解释器锁)的存在，限制了并行能力。因此我们能有的选择大致上分两种：**同步非阻塞I/O**与**异步I/O协程**。同步非阻塞I/O主要通过主程序形成消息队列轮询确认I/O完成与否，而异步I/O在I/O完成后由协程返回。相对于前者，后者的并发性要更好

### 优化？

- 更深入地看，整个web应用分为以下几个部分：

<img src="./img/1.png" height=350px>

- 优化目标：Flask自带的web server和wsgi性能羸弱，一般用于测试。
- 优化部署：
  - Nginx：高性能 Web 服务器+负载均衡；
  - gunicorn：高性能 WSGI 服务器；
  - gevent：把 Python 同步代码变成异步协程的库；

### 性能测试？

- 压力测试：siege工具