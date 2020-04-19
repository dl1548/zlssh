#!/usr/bin python
# -*- encoding: utf-8 -*-
'''
@File    :   ssh_tools.py
'''

#!/usr/bin python
# -*- encoding: utf-8 -*-
'''
@File    :   ssh_tools.py
'''


import os
import time
import json
import random
import hashlib

from .models import Record
from zlssh.settings import RECORD_DIR


def unique():
    ctime = str(time.time())
    salt = str(random.random())
    m = hashlib.md5(bytes(salt, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()

def get_key_obj(pkeyobj, pkey_file=None, pkey_obj=None, password=None):
    if pkey_file:
        with open(pkey_file) as fo:
            try:
                pkey = pkeyobj.from_private_key(fo, password=password)
                return pkey
            except:
                pass
    else:
        try:
            pkey = pkeyobj.from_private_key(pkey_obj, password=password)
            return pkey
        except:
            pkey_obj.seek(0)


# type标识本次写入的是header头还是IO流
# 记录操作历史
def record_log(type, data, connect_time, filename,host='',user='',):
    if not os.path.isdir(RECORD_DIR):
        os.makedirs(RECORD_DIR)

    if type == 'header':
        # Record.objects.create(
        #     host=Record.objects.get(host=host),
        #     user=user,
        #     filename=filename
        # )

        with open(RECORD_DIR + filename, 'w') as f:
            f.write(json.dumps(data) + '\n')
    else:
        iodata = [time.time() - connect_time, 'o', data]
        with open(RECORD_DIR + filename, 'a', buffering=1) as f:
            f.write((json.dumps(iodata) + '\n'))