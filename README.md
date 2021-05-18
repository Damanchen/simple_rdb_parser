# simple_rdb_parser

## 说明
该工具是从 [sripathikrishnan/redis-rdb-tools](https://github.com/sripathikrishnan/redis-rdb-tools) 工具"提取"出来的部分内容，
旨在用最简单的方法对 Redis RDB 文件的进行解析，帮助我们更好的了解 Redis RDB 文件的组成方式。

## 简单使用
```
# 先安装 python-lzf工具，加快解析速度(用到该工具对RDB文件中某些压缩部分进行解压)
pip install python-lzf

# 下载
git clone https://github.com/Damanchen/simple_rdb_parser.git

# 进入目录
cd simple_rdb_parser

# 这样就可以解析 /path/top/dump.rdb RDB文件了
python main /path/top/dump.rdb
```

注意：我这边着重测试的是关于 module数据段的解析，所以除了 module 相关的其他数据类型的输出就比较随意。有需要的话，可以自己根据 parser.py/RdbCallback 里提供的回调接口，自定义 ```main.py``` 里的输出内容和格式，进一步学习Redis的RDB文件，或者用作其他用途，比如数据的恢复和分析等等。

