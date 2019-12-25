#!/usr/bin/env bash

TIMENOW=`date +%y.%m.%d.%H%M`

# 进行docker镜像打包
docker build -f python_dev.build -t ssh_docker_python_dev:${TIMENOW} .
