============
HTTP LOG
============
*urllib2 httplib2 requests日志小工具*

安装方法
-----------
1. pip install httplog

使用sitecustomize.py
--------------
```python
import sys
sys.setdefaultencoding('utf-8') # set default encoding as 'utf-8'

try:
    import httplog
    httplog.monkey_patch()
except:
    pass
```
