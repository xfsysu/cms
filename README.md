# 社团管理系统

### 实现的功能
* 管理人员的注册，登录，[修改密码，忘记重置密码，通过邮箱通知注册]()(未实现）
* 已注册人员可以添加社团，删除社团，查看社团信息，编辑社团信息，社团信息包括：社团logo，社团名字，社团人数统计，
* 可以为社团添加成员，删除成员，编辑成员信息，成员信息包括：成员名字、学号、性别、专业。
*  可以根据成员的学号，姓名，专业进行全搜索（无法进行模糊搜索）

### 运行环境
ubuntu16.04
python 2.7

### 安装依赖
使用virtualenv创建项目运行虚拟环境
```bash
$ pip install virtualenv
$ cd cms/

创建虚拟环境env，并激活
$ virtualenv env
$ source env/bin/active
```
使用pip install -r 安装一些必要的库
```bash
$ pip install -r requestments.txt
```

### 本地运行
```bash
$ python manage.py runserver 默认是8000端口要是8000端口被占用，改用8001或者其他没被占用的端口
```
在浏览器中输入[http://localhost:8000/union]()即可。用户名:admin  密码：admin..123

Django自带后台管理，在浏览器中输入[http://localhost:8000/admin](), 用户名：admin 密码：admin..123