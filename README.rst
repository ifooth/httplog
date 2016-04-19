============
HTTP LOG
============
*urllib2 httplib2 requests日志小工具*

安装方法
-----------
1. pip install httplog

使用
--------------
```python
try:
    import httplog
    httplog.monkey_patch()
except:
    pass
```
