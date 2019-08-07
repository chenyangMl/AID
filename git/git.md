代码管理工具--GIT
===================
© ANTCODE

# 1.GIT简介
- 定义
    git是一个开源的分布式版本控制系统，用于高效的管理各种大小项目和文件.即代码管理工具
- 作用
   - >防止代码丢失，做代码备份
   - >项目的版本管理和控制，可以通过设置节点进行跳转
   - >支持建立各自的开发环境的分支，互不影响，方便合并 (eg: 多人合作开发项目)
   
- 代码管理工具Git特点
>* git是开源的，多在*nix下使用，可以管理各种文件
>* git是分布式的项目管理工具(svn是集中式的)
>* git数据管理更多样化，分享速度快，数据安全
>* git 拥有更好的分支支持，方便多人协调


# 2.GIT使用
- 安装
    - `sudo apt-get install git`
- git基本概念

* 工作区：项目所在操作目录，实际操作项目的区域
* 暂存区: 用于记录工作区的工作（修改）内容
* 仓库区: 用于备份工作区的内容
* 远程仓库: 远程主机上的GIT仓库

![git and github ](./git.png)

## 2.1 git初始配置
- >`主要需要配置用户名和邮箱，便于伯乐发现和联系你`
- 配置命令: `$ git config`
    >* 配置所有用户： git config --system [选项]
    >> 配置文件位置:  /etc/gitconfig

    >* 配置当前用户： git config --global [选项]
    >> 配置文件位置:  ~/.gitconfig

    >* 配置当前项目： git config  [选项]
    >> 配置文件位置:  project/.git/config

- 配置用户
    sudo git config --system user.name ANTCODE
- 配置邮箱
    git config --global user.email 12345678@163.com
- 查看配置信息
    git config --list
-> 注意: 通常情况下使用 --global配置用户和邮箱即可
    
## 2.2 git 基本命令
- > git init `初始化一个git项目`
- > git status `查看本地仓库状态`
- > git add [file...] `将本地工作区文件记录到暂存区`
  >
  > > 支持提交多个文件(空格间隔)，全部文件(使用*提交，除了隐藏文件以外)隐藏文件需要指定文件名提交
- > git rm --cached [file] `撤销记录到暂存区的文件`
- > git commit [file] -m [message] `将暂存区文件提交到本地仓库`
  >
  > > 说明: -m表示添加一些同步信息，描述同步内容
- > git log --pretty=oneline `查看commit日志`

- > git diff [file] `对比工作区和仓库文件的差异`
- > git checkout  -- [file]  `--是为了防止误操作，不加--表示从本地仓库拉回到本地工作区`

- > git mv [file] [path] `移动文件`
- > git rm [file] `删除文件`
  >
> > git commit -m [message] `rm 和 mv 只是操作了工作区内容，提交后会同步操作到仓库`
  
    
## 2.3 版本管理命令
- 使用场景： 有效持续的管理项目版本

1.退回到上一个commit节点
 > `git reset --hard HEAD^`
 > 注意 ： 一个^表示回退1个版本，依次类推。当版本回退之后工作区会自动和当前commit版本保持一致

2.退回到指定commit节点
> `git reset --hard` [commit_id]

3.查看所有操作记录
> `git reflog`
>注意:最上面的为最新记录，可以利用commit_id去往任何操作位置

4.创建标签
- > 虽然可以通过commit来实现commit节点的跳转，但重要节点通常采用打标签的形式来记录。如重要的版本节点。
- > 标签：在项目重要的commit位置添加快照，保存当时的工作状态，一般用于版本的迭代。
> 命令：`git  tag  [tag_name] [commit_id] -m  [message]`
    说明: commit_id可以不写则默认标签表示最新的commit_id位置，message也可以不写，但是最好添加。
```
e.g. 在最新的commit处添加标签v1.0
git tag v1.0 -m '版本1'
```

5. 查看标签

- >`git tag` 查看标签列表
- >`git show [tag_name]` 查看标签详细信息

6. 去往某个标签节点

> `git reset --hard [tag] `

7. 删除标签

>` git tag -d  [tag]`

```text

实际应用过程中，通过在重要节点设置标签，然后我们可以在重要的版本节点间来回的切换来管理项目.

```
## 2.4 保存工作区
- 使用场景: 在项目开发中遇到技术难点时,需要在工作区尝试多种方案，不确定是否为最终提交版本

1.保存工作区未提交内容
- > `git stash save [message]` 说明: 将工作区未提交的修改封存，让工作区回到修改前的状态

2. 查看工作区列表
- > `git stash list` 说明:最新保存的工作区在最上面

3. 应用某一个工作区

- > `git stash  apply  [stash@{n}]` 
4. 删除工作区
- > `git stash drop [stash@{n}] ` 删除某一个工作区
- > `git stash clear`  删除所有保存的工作区


## 2.5 分支管理
- >定义: 分支即每个人在原有代码（分支）的基础上建立自己的工作环境，
       单独开发，互不干扰。完成开发工作后再进行分支
1. 查看分支情况
> `git branch` 说明: 前面带*的表示当前的工作分支

2. 创建分支
> `git branch [branch_name]` 说明:基于a分支创建b分支,此时b分支会拥有a分支全部内容。
因此在创建分支时应保证工作区处于‘干净’状态

3. 切换分支
> `git checkout [branch_name]`

4. 合并分支
> `git merge [branch]`
- >冲突问题是合并分支过程中最为棘手的问题
  >> 1. 当分支合并时，原分支和以前发生了变化就会产生冲突
  >> 2. 当合并分支时添加新的模块（文件），这种冲突可以自动解决，只需自己决定commit操作即可。
  >> 3. 当合并分支时两个分支修改了同一个文件，则需要手动解决冲突。

5. 删除分支
> `git branch -d [branch_name]` 删除分支
> `git branch -D [branch_name]` 删除没有被合并的分支


## 2.6 远程仓库
> 远程仓库: 远程仓库即非本地仓库以外的仓库(即远程主机上的git仓库)实际上git是分布式结构，
每台主机的git仓库结构类似，只是把别人主机上的git仓库称为远程仓库。即
### 2.6.0 创建共享仓库
在别人主机通过git init 初始化一个git仓库，相对本人主机即为远程仓库，但这样的远程仓库只是普通的仓库，
不能实现资源共享,要实现资源共享需要将普通的远程仓库设置为共享仓库。

> 在git仓库中bare属性为True的共享仓库可以很好的和远程仓库进行交互
创建步骤：

- 选择共享仓库目录，将该目录属主设置为当前用户

```
mkdir gitrepo
chown tarena:tarena gitrepo
```

- 将该目录初始化为git共享目录，下例中tedu为自己取的项目名称，.git为通用结尾后缀

```
cd gitrepo
git init --bare tedu.git
```

- 将git配置目录与项目目录设置为相同的属主

```
chown -R tarena:tarena tedu.git
```


### 2.6.1 从远程向本地拉取项目和更新内容
> 1. `git clone [远程共享git仓库地址]` 从远程克隆整个项目，并自动建立与远程仓库名为origin的远程连接.
> 1. `git pull` 拉取远程共享仓库中最新的内容，合并到当前内容。
> 1. `git fetch origin [branch_name]` 从远程共享仓库拉取分支


### 2.6.2 本地向远程仓库push文件

1. 在本地git仓库与远程的共享git仓库建立连接
> `git remote add [name] [远程共享git仓库地址]` 说明： 传输协议可以是ssh , https, file...
>
> > eg 这里使用https连接: git remote add origin https://github.com/XXXXXX/AID.git

2. 从本地git仓库push文件到远程共享git仓库
> `git push -u [name] [branch_name]` 说明: 默认是以分支为单位进行push提交的,-u表示第一次提交分支间建立连接
    - >> eg push主分支内容: git push -u origin master
    - >> 当本地仓库内容修改了，可以直接通过git push origin matser同步到远程共享仓库

3. 查看当前远程连接名
> `git remote`

4. 查看当前所在分支名
> 查看所有分支 `git branch -a` 说明: 前面带*表示当前分支

5. 删除远程仓库中的分支
> `git push origin :[远程分支名]`说明： 该命令会删除远程共享仓库中的分支，不会删除本地仓库中的分支.

6. 其他推送方式
> `git push --force origin [branch_name]` 用于本地版本比远程仓库版本低的时候



# 3. Github使用

> github就是一个远程共享git仓库管理社区，所以我们可以通过git工具将代码上传到github的共享仓库中。
社区中的项目都是开源项目.

## 3.1 基于https传输的使用方法

1. 从远程共享git仓库克隆项目 `git clone [项目的网络地址]`
> eg 从github上克隆项目: `git clone https://github.com/chenyangMl/AID.git`

2. 从远程共享仓库获取项目更新内容 `git pull`
3.  从远程共享仓库拉取分支 `git fetch origin [branch_name]`

4. 从本地上传代码 `git push -u origin master`

## 3.2 基于ssh传输的使用方法

使用ssh来生成秘钥连接github,并在你的github项目中配置秘钥，这样能够避免每次提交都需要输入用户名和密码.
适合小组共同开发管理项目.
1. 本地创建 ssh秘钥
在信任的计算机上使用命令`$ ssh-keygen`创建秘钥. 秘钥文件在 `/home/tarena/.ssh/`
其中包含私钥: id_rsa , 公钥:id_rsa.pub, 复制公钥中的内容.

2. 在github中添加的信任的主机公钥
> 登录github--> setting --> SSH and GPG keys --> New SSH key -->粘贴复制的公钥-->保存。
保存后github会向你的注册邮箱发送通知邮件。

3. 使用 ssh 建立远程连接
> `git remote add origin git@github.com:chenyangMl/AID.git`

4. 向远程进行push时不需要输入用户名和密码
> ` git push -u origin [branch]`
> `git push` 建立连接后直接push即可
