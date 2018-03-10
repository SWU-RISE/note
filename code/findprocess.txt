可以使用：ps -fe | grep filename，
也可以使用：fuser filename查看
然后可以看这个进程跟哪里东西有关联，使用了哪些端口
只查看该进程：ps -ef | grep ID
查看该进程打开的文件：lsof -p ID
查看内存分配：lcat /proc/ID/maps
查看堆栈：pstack 11ID
查看发出的系统调用:strace -p ID
查看调用库函数:ltrace -p ID
