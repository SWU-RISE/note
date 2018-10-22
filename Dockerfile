FROM tutum/lamp:latest RUN
 rm -fr /app && git clone https://github.com/username/customapp.git /app 
#这里替换 https://github.com/username/customapp.git 地址为你自己的项目地址. 你可以在github上面写代码，而不用直接服务器上代码。
EXPOSE 80 3306 
# 暴露两个端口
CMD ["/run.sh"]
