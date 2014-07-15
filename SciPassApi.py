
import time
import ipaddr
import pprint

class SciPassApi:
  """SciPass API for signaling when a flow is known good or bad"""
  def __init__(  self ):
    self.whiteListHandlers = []
    self.blackListHandlers = []
    self.whiteList = []
    self.blackList = []

  def registerWhiteListHandler(self, handler):
    self.whiteListHandlers.append(handler)

  def registerBlackListHandler(self, handler):
    self.blackListHandlers.append(handler)

  def good_flow(self, obj):
    #turn this into a 
    #presumes that we get a nw_src, nw_dst, tcp_src_port, tcp_dst_port
    #we need to do verification here or conversion depending on what we get from the sensors
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(obj)
    self._fireWhiteListHandlers(obj)
    results = {}
    result.success = 1
    return result

  def bad_flow(self, obj):
    #presumes that we get a nw_src, nw_dst, tcp_src_port, tcp_dst_port
    #we need to do verification here or conversion depending on what we get from the sensors
    self._fireBlackListHandler(obj)
    results = {}
    result.success = 1
    return result

  def get_bad_flow(self):
    return self.whiteList

  def get_good_flow(self):
    return self.blackList

  #just call any and all handlers we have
  def _fireBlackListHandlers(self,match):
    self.blackList.append(match)
    for handler in self.blackListHandlers:
      handler(nw_src = match['nw_src'], 
              nw_dst = match['nw_dst'],
              nw_src_mask = match['nw_src_mask'],
              nw_dst_mask = match['nw_dst_mask'],
              tp_src = match['tp_src'],
              tp_dst = match['tp_dst'])
    
  #just call any and all handlers we have
  def _fireWhiteListHandlers(self,match):
    self.whiteList.append(match)
    for handler in self.whiteListHandlers:
      handler(nw_src = match['nw_src'],
              nw_dst = match['nw_dst'],
              nw_src_mask = match['nw_src_mask'],
              nw_dst_mask = match['nw_dst_mask'],
              tp_src = match['tp_src'],
              tp_dst = match['tp_dst'])