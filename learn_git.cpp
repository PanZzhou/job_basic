#include <bits/stdc++.h>
using namespace std;
int main(){
	mkdir learngit
	cd learngit
	pwd

	git init                          把目录初始化成git可以管理的仓库
	git add readme.txt                把文件添加到仓库，可以同时add多个文件，也可以分多次
	git add .                         add 所有文件
    git commit -m "添加了一个文件"    提交事务并备注，-m参数后的表示备注（多个add，一个commit）    
    git diff                          文件产生冲突时，可以用它来看两个文件的区别。
    
    git log                           显示提交日志，可以看到版本号。按q结束
    git reset --hard HEAD^            回退到上一个版本，HEAD^^表上上，HEAD~100表上100
    git reset --hard commit版本号     设置为某一个版本。

    cat readme.txt                    显示文件内容

    git reflog                        记录了每一次命令，用于回退到未来的版本，与git log对应

    learngit目录为工作区，其中的隐藏目录.git是版本库，可通过ls -au看到
    工作区中的文件通过add命令加载到版本库中的stage暂存区中，再通过commit
    把stage中的所有内容提交到master分支中，其中HEAD指针指向master分支。
    master分支在我们创建版本库时自动创建。

    git status                        查看工作区是否干净，即工作区是否被修改，必须先add在commit，若直接commit，则修改不会被提交
                                      git跟踪和管理的是修改而不是文件（所以可以看到多次add readme.txt）
    
    git checkout -- readme.txt        文件恢复到修改前最近的状态，add后修改则从add时的状态开始算起                               
    git reset HEAD readme.txt         把暂存区的修改撤销掉，并重新放回工作区。可以和上一个命令配合使用   
    
    对于已经commit的readme.txt来说：
    git rm readme.txt 与 git commit   可以吧版本库中的文件删掉
    git rm readme.txt 与 git checkout -- readme.txt   可以在误删文件后吧文件恢复过来

    远程git：
     ssh-keygen -t rsa -C "youremail@example.com"     此为获取ssh ssh-key，之后再在github上设置获取的公钥

    现在github上创建一个新的仓库，如仓库名为tank
    git init                          在要git的本地仓库中执行
    git remote add tank git@github.com:PanZzhou/tank.git            本地仓库与github仓库关联，后一个tank由取得github
    git clone git@github.com:PanZzhou/tank.git                      从远程库克隆
                                                                    仓库名决定，前一个也是自己取，一般为origin
    git push -u tank master              推送内容到远程库中，-u会关联两个master分支，
                                       关联后推送或拉取可以简化命令，如以后的push可写为：git push tank master

    git remote                         查看远程库的信息，如上面的项目会显示tank（前一个tank）
    git remote -v                      会显示推送和抓取的tank的地址
    git push origin master             推送                                 
    
    分支：
    git branch <name>                   创建分支
    git checkout <name>                 切换分支
    git checkout -b <name>              创建并切换分支
    git branch                          查看分支
    git merge <name>                    合并某分支到当前分支（禁用fast forward时，即用--no-ff
                                        数，在合并时会产生提交，从而不会与指定的超前的分支合并）
    git branch -d <name>                删除分支
    分支会有冲突的时候，产生冲突时必须先解决冲突，在文件中会被标明区别，修改后再add一遍即可
     原则：
     1.别在master分支上干活，此分支只用来发布新版本
     2.在新建的dev分支上干活，即多个人在dev分支上有不同的分支

    bug分支：正在dev上干活，此时要处理master上的bug时：
    git stash                            保存dev的工作现场，因为还没提交
    git checkout master                   切换到master分支
    git checkout -b bug_1                 创建并切换到bug_1分支处理bug
    git checkout master                   再次切换到master分支
    git merge --no-ff -m "tishi" bug_1    合并分支到master上，完成bug的修改
    git checkout dev                      回到dev分支
    git stash list                        查看保存的工作现场
    git stash pop                         回到保存的现场
    
    feature分支：添加新功能时使用，与bug分支类似，但当要丢弃一个没有被合并过得分支
    时，可以通过git branch -D <name> 来删除

   在多人协作时，小伙伴从远程库clone时，默认情况下只能看到master分支，如要在dec下开发，
   就必须创建远程tank的dev分支到本地：
   git checkout -b dev tank/dev           创建dev分支到本地。修改项目完成
   gin push tank dev                       推送dev分支到远程dev分支
   多人协作时，多个人对同一远程库文件进行了修改，此时会报错，解决办法就是：
   git pull                                把最新的提交从tank/dev抓取下来，在本地解决冲突再推送
   git branch --set-upstream dev tank/dev  指定两个分支关联
}  
