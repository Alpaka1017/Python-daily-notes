<sub>Title: Git入门<br>Author:<a href="https://github.com/Alpaka1017?tab=repositories" target="_blank">Xueyong Lu  <i class="fa fa-github" aria-hidden="true"></i></a></br><small>First Edition: April- 2023</small></sub>

<div align = "center">
    <h1>Python学习日记 - Part 01</h1>
</div>
<div align = "right">
	<h2>Git入门</h2>
</div>


📘<<[Part 01](./Python_Part_01-Git入门.md) | [Part 02](./Python_Part_02-Reg_Ex.md)]>> 



## 1. 将本地目录链接到远程仓库

* [安装Git](https://git-scm.com/)

* [可视化Git指令学习](https://oschina.gitee.io/learn-git-branching/)

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
| **`git add`**     | **将更改添加到Git仓库的缓存区中，表示这些文件纳入版本控制**  |
| **`git commit `** | **将暂存区中的更改提交到Git仓库中，即表示将这些文件保存为一个新的版本** |
| **`git push`**    | **将本地仓库中的更改推送到远程Git仓库中**                    |
| `git pull`        | 将远程Git仓库中的更改拉取到本地仓库中                        |
| `git branch`      | 显示当前仓库中的分支                                         |
| `git checkout`    | 切换到另一个分支或恢复文件到先前版本                         |
| `git merge`       | 合并两个分支中的更改                                         |
| `git log`         | 显示Git仓库中提交的日志                                      |
| `git diff`        | 用于比较不同版本之间的差异                                   |
| `git stash`       | 用于将当前修改暂存起来，便于之后恢复或者应用                 |

## 5. 常见问题及解决

### 5.1 Git索引错误

* `Updating the Git index failed.  A rescan will be automatically started to resynchronize git-gui.`

* 这种情况通常发生在使用 Git GUI 进行操作时，由于 Git index 状态与 Git 仓库的状态不一致导致的

* 解决办法：

  1. 关闭 Git GUI，确保没有其他程序正在访问 Git 仓库

  2. 打开终端或命令提示符，进入 Git 仓库所在的目录

  3. 运行以下命令以清除 Git index：

     ```bash
     git rm --cached -r .
     ```

     * 清除文件索引，而不会清除文件本身

  4. 运行以下命令以重新添加所有文件和子目录：

     ```bash
     git add .
     ```

  5. 运行以下命令以提交更改：

     ```bash
     git commit -m "Resynchronize Git index"
     ```

  6. 重新启动 Git GUI，并尝试再次进行操作

### 5.2 删除Repository

* `remote origin already exists`

* 确认已经删除了原来的仓库，并且在本地新建了一个空的仓库，或者重新Clone了一个新的远程仓库到本地

* 在本地仓库所在目录下执行下面命令，删除本地仓库与原来远程仓库的连接

  ```bash
  git remote remove origin
  ```

* 确认当前本地仓库的远程配置信息：

  ```bash
  git remote -v
  ```

* 将本地的仓库链接到新的远程仓库

  ```bash
  git remote add origin <新的远程仓库的URL>
  ```

* 将本地代码推送到新的远程仓库中：

  ```bash
  git push -u origin master
  ```

### 5.3 更改默认branch

* Repository → Settings → Options → Default branch → Change → Update (~~main~~)

* 回到本地仓库，将本地仓库与更新后的默认分支(master)链接：

  ```bash
  git remote set-head origin master
  ```

* 推送本地仓库的变更到远程仓库中：

  ```bash
  git push grigin master
  ```

  

### 5.4 Push空文件夹到远程

* 在空文件夹下创建一个空文件，运行bash：

  ```bash
  touch image/.gitkeep
  ```

* 将空文件夹添加到Git Repository中：

  ```bash
  git add image/.gitkeep
  ```

* 提交更改并推送到远程Repository中：

  ```bash
  git commit -m "Least change"
  git push origin <branch-name>
  ```




### 5.5 提交失败之后怎么再次提交（文件大小超过限制）

* 基本逻辑：`Github`在提交时，先会生成一系列文件的**哈希值**作为提交记录，然后会在`git add .`将所有更改提交到暂存区

* 在本地删除这个错误的文件、并且通过以下命令删除在暂存区的此文件

  ```bash
  git rm --cached <Path/ File name>
  ```

* 最重要的一步：清除掉此文件在提交记录中的哈希索引

  * 列出当前文件提交记录的哈希值

    ```bash
    git rev-list --objects --all | grep <Path/ File name>
    ```

  * 删除当前错误文件的哈希值

    ```bash
    git filter-branch --tree-filter 'rm -f <Path/ File name>' HEAD
    ```

* 尝试再次提交

### 5.6 删除远程仓库中不需要的文件以及其提交记录

* 删除命令

  ```bash
  git rm --cached <file.format>
  ```

* 添加注释

  ```bash
  git commit -m"Remove xxx"
  ```

* 提交更改

  ```bash
  git push origin <Branch>
  ```

### 5.7 添加`.gitignore`文件以忽略指定文件的提交

* 在本地仓库根目录下添加以下文件：
  ***`.gitignore`***

* 添加要指定忽略的目录或者文件

  ```bash
  venvPyQt6/
  __pycache__/
  font/
  image/
  ```

* 添加相对路径
  ```bash
  /image/assets/
  ```

  * 在本地仓库的根目录下创建`.gitignore`文件，词条命令是忽略`./image/assets/`目录以及其所有的子目录/文件

  * 或者在`./image`文件夹下添加一个`.gitignore`文件，添加

    ```bash
    /assets/
    ```

    以实现与上面相同的效果

* 在添加了`.gitignore`文件之后，确保执行适当的命令，以使指定要忽略更新的目录生效

  ```bash
  git add .gitignore
  ```

  和

  ```bash
  git commit -m "Update .gitignore
  ```

  

📘<<[Part 01](./Python_Part_01-Git入门.md) | [Part 02](./Python_Part_02-Reg_Ex.md)]>> 
