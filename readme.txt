版本说明：
版本号：v0.5

暂时还没有采用版本管理软件，目前手工进行版本管理。
该版本的功能：
1. 在首页中实现了用户登录和鉴权，已经鉴权的用户在下次登录时免登录（通过设置cookie的时间进行控制）
2. 完成了知识库模块的第一个版本，重点功能包括：
   1）未通过鉴权的用户可以看所有的帖子，但不能增加。
   2）通过鉴权的用户可以发布帖子，包括一个附件文件。
   3）实现了对摘要的搜索功能，如果要匹配关键字，需要以空格进行分隔。
   4）对帖子暂时不能修改和删除。
3. 系统方面，实现了：
   1）与数据库的交互均计入日志。
   
   
 下一版本的考虑：
 1. 实现用户的自注册和管理员审批功能。
 2. 实现知识库的帖子的修改和删除功能。