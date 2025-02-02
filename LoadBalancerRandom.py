import random
from __future__ import annotations
from typing import TYPE_CHECKING
from LoadBalancer import LoadBalancer

if TYPE_CHECKING: #only for typechecking
    from Environment import Environment 
    from Request import Request

from Server import Server

class LoadBalancerRandom(LoadBalancer):
    """
    Loadbalancer assigning to servers random
    """
    def __init__(self, nServers, environment: Environment):
        super().__init__(nServers=nServers,environment=environment)
        self.currentServer = random.randint(0,nServers)
    
    def handleRequestArrival(self, request: Request):
        """
        Round robin assignment
        """
        self.serverList[self.currentServer].assignRequest(request=request)
        self.currentServer = random.randint(0,self.nServers)
        
        nQueue = sum([server.queue.size for server in self.serverList])
        self.environment.logData("totalInQueue", nQueue)
    
    def onPeriodEnd(self):
        """
        This method will be called on the end of each period, this is the place where the next period number of servers is determined
        """
        return
        #raise NotImplementedError
