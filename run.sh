 #!/bin/bash
 echo 'welcome to use leetcode_spider'
 echo 'author: Dreamgoing'

 if [ ! -f "env" ]; then
     echo 'env'
 else
    virtualenv env
 fi

 source ./env/bin/activate
 pip install -r requirements.txt
 python spider.py
