## 说明
	本项目为演示案例，采用前后端分离实现，后端使用的是Python的Django框架，前端使用的是Vue，数据库为MySQL

## 实现思路
- 利用网易云API获取部分数据
- 基于标签进行歌单详情页的推荐、歌曲详情页的推荐、歌手详情页的推荐
- 基于用户的协同过滤算法给用户推荐用户、个用户推荐歌曲
- 基于物品的协同过滤算法给用户推荐歌手
- 基于内容的推荐算法给用户推荐歌单
- 个性化排行榜
- 为你推荐（不同用户行为不同看到的为你推荐也不同）
- 我的足迹，展示用户在站内的行为

## 后端依赖
- Python版本为3.6
- Python包和对应的版本在MusicRecSys/MusicRec/z-others/files/requirement.txt文件中
- 安装依赖为 pip install -r requirement.txt

## 前端说明
- 依赖Node.js，版本为10.13

## 运行说明
- mysql新建musicrec数据库，将MusicRecSys/MusicRec/z-others/files/musicrec.sql 文件导入
- 修改 MusicRecSys/MusicRec/MusicRec/settings.py 文件中的ALLOWED_HOSTS为本地IP地址和本地mysql配置信息
- 修改 MusicRecSys/MusicRec-Vue/config/index.js 中的 serverUrl
- 修改 MusicRecSys/MusicRec-Vue/src/assets/js/linkBase.js 中的 serverUrl
- 进入 MusicRecSys/MusicRec 执行python manage.py runserver 0.0.0.0:8000
- 进入 MusicRecSys/MusicRec-Vue 执行npm install /  npm run dev
- 浏览器输入 http://127.0.0.1:8001 访问

## 相关说明
- 后台访问地址：http://127.0.0.1:8000/admin/  (admin，admin)
- Navicat 破解版 （链接：https://pan.baidu.com/s/1dYtKQxnoSZywuRfgCOfPRQ  提取码：qw8k） 
- git lfs 上传管理大文件
    - 执行 git lfs install 开启lfs功能
    - 使用 git lfs track 命令进行大文件追踪 例如git lfs track "*.png" 追踪所有后缀为png的文件
    - 使用 git lfs track 查看现有的文件追踪模式
    - 提交代码需要将gitattributes文件提交至仓库. 它保存了文件的追踪记录
    - 提交后运行git lfs ls-files 可以显示当前跟踪的文件列表
    - 将代码 push 到远程仓库后（git lfs push），LFS 跟踪的文件会以『Git LFS』的形式显示:
clone 时 使用'git clone' 或 git lfs clone均可

作者：amosbake
链接：https://www.jianshu.com/p/493b81544f80
來源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
# About Me
ID：Thinkgamer

Email：Thinkgamer@163.com

微信：
<br>
<div align="center"><img src="https://raw.githubusercontent.com/Thinkgamer/books/master/0%E3%80%81Picture/wx.png" width="200" /></div>
<br>
微信公众号：【数据与算法联盟】
<br>
<div align="center"><img src="https://raw.githubusercontent.com/Thinkgamer/books/master/0%E3%80%81Picture/gzh.jpg" width="230"></div>

注明：禁止用作商业用途
-----
