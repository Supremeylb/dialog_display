#!/usr/bin/env python
#  -*- coding:utf-8 -*-

import os
import time
import logging

DEFAULT_LOGGER_FORMATTER = logging.Formatter('%(message)s,%(levelname)s,"%(asctime)s"')
DEFAULT_LOGGER_LEVEL = logging.INFO

class teks_logger(object):

  def __init__(self, name, formatter, filehandler, level):
    self.logger = logging.getLogger(name)
    handler = filehandler
    if not handler:
      work_dir = os.path.split(os.path.realpath(__file__))[0]
      handler = logging.FileHandler(work_dir + "/logs/%s_%s.log" % (name, str(int(time.time()))))
    handler.setFormatter(formatter)
    self.logger.addHandler(handler)
    self.logger.setLevel(level)  
    
  def debug(self, message):
    self.logger.debug(message)

  def info(self, message):
    self.logger.info(message)

  def warn(self, message):
    self.logger.warn(message)

  def error(self, message):
    self.logger.error(message)

  def critical(self, message):
    self.logger.critical(message)
    
#################################################################

if __name__ == "__main__":

  logger = teks_logger("hkia_dialogs", \
                       DEFAULT_LOGGER_FORMATTER, \
                       None, \
                       DEFAULT_LOGGER_LEVEL)
                       
  logger.debug('nn,一个debug信息')
  logger.info('hh,一个info信息')
  logger.warn('ggg,一个warning信息')
  logger.error('ff,一个error信息')
  logger.critical('qq,一个致命critical信息')
                       