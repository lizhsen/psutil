# -*- coding: utf-8 -*-

import psutil


def get_netrk_info():

    psutil.net_io_counters()
    print psutil.net_io_counters()
    return psutil.net_io_counters()

def get_memory_used():
    psutil.virtual_memory()
    memory_info = psutil.virtual_memory()
    memory_used = ( memory_info.total * memory_info.percent / 100 ) / 1024 / 1024/1024
    print "memused is ****"+ str(memory_used) +"**********"
    return memory_used


get_netrk_info()
get_memory_used()
