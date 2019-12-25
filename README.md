1. 生成Docker镜像，在src/requirements.txt中添加自己需要的模块，运行build.sh即可；
2. 生成的镜像名字为: ssh_docker_python_dev:${TIMENOW}，镜像的登录账号、密码可以在start.sh脚本中修改；
3. 启动该镜像，该镜像的暴露端口为15731，启动镜像的命令为：

```bash
docker run -d -p 49154:22 -p 15731:15731 镜像名字 
```

4. 测试镜像的SSH服务是否启动以及Python3.7.0是否安装：

输入命令：

```bash
ssh -p 49154 user@127.0.0.1
```
密码为newpass， 进入镜像后输入python3看Python3.7.0是否安装。

5. 用PyCharm（专业版）连接该镜像进行开发：

- 启动该镜像，命令参考第3步；
- 在设置中将Project Interpreter选择SSH interpreter，然后输入ip, port, 账号、密码即可，注意本地项目路径与Docker容器内的项目路径的对应关系。

6. jieba_test.py用于测试开发环境中的jieba模块是否安装成功。