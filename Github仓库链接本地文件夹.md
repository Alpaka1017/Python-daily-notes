title: Github仓库链接本地文件夹
author: Xueyong Lu
date: 2022-03-22

<div align = "center">
    <h1>Python学习日记</h1>
</div>
<div align = "right">
	<h2>Github仓库链接本地文件夹</h2>
</div>

## 1. 将本地目录链接到远程仓库

* [安装Git](https://git-scm.com/)

* 进入要push的文件夹根目录下：

  ```bash
  cd "myfolder"
  ```

* 初始化一个新的Repository

  ```bash
  git init
  ```

* 将所有文件添加到Github的Repository中，并提交更改

  ```bash
  git add .
  git commit -m "Initial commit"
  ```

  * 如果是将某个特定的文件添加到暂存区

    ```bash
    git add <file>
    ```

  * 如果是直接用`git commit`命令，之后会打开一个编辑框，以输入详细的commit信息

* 在Github上新建一个仓库，并克隆到本地

  ```bash
  git clone https://github.com/your-username/myfolder.git
  ```

* 将本地目录与远程仓库进行关联，并将代码推送到远程仓库

  ```bash
  git remote add origin https://github.com/your-username/myfolder.git
  git push -u origin master
  ```

## 2. Git仓库的发布

* 为要发布的当前分支的最新提交添加一个标签`tag`

  ```bash
  git tag <...>
  ```

* 将标签推送到远程仓库

  ```bash
  git push origin <...>
  ```

* 一次性推送所有标签

  ```bash
  git push --tags
  ```

* 为标签添加注释

  ```bash
  git tag -a <...> -m "Release version 1.0.00"
  ```

## 3. 仓库和分支

* 在版本控制系统（VCS）中，仓库（repository）是存储代码和项目文件的地方，而分支（branch）是指在仓库中创建的一个独立的、与主线（master branch）相互独立的开发分支。

  在**一个仓库中可以创建多个分支**，每个分支都有自己的代码提交历史和版本记录，可以在不影响主线的情况下进行独立的开发和修改。这使得团队成员可以同时处理多个任务，同时协作开发多个功能，而不会相互干扰。

  分支和仓库的关系是，一个仓库中可以包含多个分支，而每个分支都可以看作是仓库的一个子集。因此，一个分支中的代码修改和提交只影响该分支的代码库，而不影响主线或其他分支的代码库。同时，分支之间可以合并，将不同分支的代码合并到一起，实现代码的统一管理和发布。

* 为一个仓库Respository创建一个新的Branch

  ```bash
  git branch [branch-name]
  ```

  * 如：

    ```bash
    git branch feature # 创建一个名为feature的分支
    ```

* 切换分支

  ```bash
  git checkout [branch-name]
  ```

* 合并分支：将**指定分支**的修改**合并到当前分支中**

  ```bash
  git merge [branch]
  ```

* 查看分支：列出当前仓库中的所有**分支**

  ```bash
  git branch
  ```

* 删除分支

  ```bash
  git branch -d [branch-name]
  ```

  * 如：

    ```bash
    git branch -d feature
    ```

* 查看分支合并图

  ```bash
  git log --oneline --graph --decorate --all
  ```

## 4. 其他命令汇总

| `git init`        | 在当前目录中初始化一个新的Git仓库                            |
| ----------------- | ------------------------------------------------------------ |
| `git clone`       | 从远程Git仓库中克隆一个仓库到本地                            |
| `git status`      | 显示当前仓库的状态，即哪些文件被修改、哪些文件被暂存等等     |
| **`git add`**     | 将更改添加到Git仓库的缓存区中，表示这些文件纳入版本控制      |
| **`git commit `** | 将暂存区中的更改提交到Git仓库中，即表示将这些文件保存为一个新的版本 |
| `git push`        | 将本地仓库中的更改推送到远程Git仓库中                        |
| `git pull`        | 将远程Git仓库中的更改拉取到本地仓库中                        |
| `git branch`      | 显示当前仓库中的分支                                         |
| `git checkout`    | 切换到另一个分支或恢复文件到先前版本                         |
| `git merge`       | 合并两个分支中的更改                                         |
| `git log`         | 显示Git仓库中提交的日志                                      |
| `git diff`        | 用于比较不同版本之间的差异                                   |
| `git stash`       | 用于将当前修改暂存起来，便于之后恢复或者应用                 |

