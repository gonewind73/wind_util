'''
Created on 2018年5月30日

@author: heguofeng
'''
import logging

def set_debug(debug_level=logging.INFO, filename="",filter=lambda record:True):
    console = logging.StreamHandler()
    console_filter = logging.Filter()
    console_filter.filter = filter
    console.addFilter(console_filter)
    if filename:
        logging.basicConfig(level=debug_level,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=filename,
                filemode='w',
                )
    else:
        logging.basicConfig(level=debug_level,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                handlers = [console,]
                )
    