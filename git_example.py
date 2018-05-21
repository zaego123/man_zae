Git鼓励大量使用分支：
查看分支：git branch
创建分支：git branch <name>
切换分支：git checkout <name>
创建+切换分支：git checkout -b <name>
合并某分支到当前分支：git merge <name>
删除分支：git branch -d <name>

要关联一个远程库，使用命令git remote set-url origin git@server-name:path/repo-name.git；
关联后，使用命令git push -u origin master第一次推送master分支的所有内容；
此后，每次本地提交后，只要有必要，就可以使用命令git push origin master推送最新修改；
分布式版本系统的最大好处之一是在本地工作完全不需要考虑远程库的存在，也就是有没有联网都可以正常工作，而SVN在没有联网的时候是拒绝干活的！当有网络的时候，再把本地提交推送一下就完成了同步，真是太方便了！

git reset HEAD <file>#pointer refreshed but not chaged, that change flushed the temp-repository
#if without using parameter<file>,the all files did the same thing
#but the command won't change working-reposiory
#qingkong huanchongqv
git checkout -- <file>
#Git会告诉你，git checkout -- file可以丢弃工作区的修改：
一种是readme.txt自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；
一种是readme.txt已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。
总之，就是让这个文件回到最近一次git commit或git add时的状态。
#like command diff
#update and make it the latest version in repository(including commited and temp)zancunqv he yitijiaoqv

Git允许我们在版本的历史之间穿梭，使用命令git reset --hard commit_id
在Git中，用HEAD表示当前版本，也就是最新的提交1094adb...

git reset --hard HEAD^

git reflog用来记录你的每一次命令(commited)
git diff HEAD -- readme.txt命令可以查看工作区和版本库里面最新版本的区别
diff#it shows the diff between working-dictionary and repository(including the will-be-committed and the committed)

#Three uncommited status in git:
git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   readme.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   readme.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	d.txt
	hosts/

