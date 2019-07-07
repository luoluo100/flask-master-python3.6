# 基于flask的博客系统搭建(md文件换行，后缀两空格)
- 1.激活virtualenv环境，`. venv/bin/activate`。安装所有requirements.txt中的模块,`pip install -r requirements.txt`。因为网络的原因可能会其中某几个会安装失败，多安装几次就好。
- 2.导入坏境变量，需要导入以下三个变量
  * export MAIL_USERNAME=<your email@example.com>(开启了smtp服务的邮箱账号，程序里默认使用163邮箱，可以修改成其它类型邮箱)
  * export MAIL_PASSWORD=<password>(不一定是你的邮箱密码，比如163邮箱开启smtp服务会让你设置一个密码，该密码即为password,qq邮箱开启smtp会提示给你一个密码)
  * export FLASK_ADMIN=<admin email>(默认是管理者邮箱，用该邮箱创建账号就是管理者)
- 3.安装数据库迁移。输入以下命令
  * `python manage.py db init` (使用init命令创建迁移仓库)
  * `python manage.py db migrate -m "initial migration"`(migrate命令用来自动创建迁移脚本)
  * `python manage.py db upgrade`(更新数据库，第一次使用该命令会新建一个数据库)
- 4.部署程序，`python manage.py deploy`
- 5.在本地运行程序,`python manage.py runserver`打开http://127.0.0.1:5000端口查看, 按Ctrl+C退出程序。
- 6.测试：`python manage.py test`
- 7.创建角色，Terminal下：  
    `python manage.py shell`  
    `Role.insert_roles()`  
    `Role.query.all()`  
- 8.赋予角色权限，直接在数据库users表里修改，创建角色时一般默认role_id为1(普通用户)，修改成2（协管）或 3（管理员）
- 9.完成项目后，导出包：  
    在项目目录下，Shift+右键，选择在此处打开命令窗口，`pip freeze > package`