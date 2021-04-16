# simple_rdb_parser

该工具是从 [sripathikrishnan/redis-rdb-tools](https://github.com/sripathikrishnan/redis-rdb-tools) 工具"提取"出来的部分内容，
旨在用最简单的方法对 Redis RDB 文件的进行解析，帮助我们更好的了解 Redis RDB 文件的组成方式。

可以自己根据 parser.py/RdbCallback 里提供的回调接口，自定义 ```main.py``` 里的输出内容和格式，或者用作其他用途，比如数据的恢复和分析等等。

