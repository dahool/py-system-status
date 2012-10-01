# -*- coding: utf-8 -*-
"""Copyright (c) 2012 Sergio Gabriel Teves
All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
"""
Created on 29/09/2012
"""
import platform
import datetime
from pystatus.app.models import Process
from .commands import get_command_output

class DiskUsage:
    dev = None
    size = None
    used = None
    avail = None
    usep = None
    mount = None
    
    def __unicode__(self):
        return u"dev: %s, size %s, used %s, avail %s, usep %s, mount %s" % (self.dev,
                                                                  self.size,
                                                                  self.used,
                                                                  self.avail,
                                                                  self.usep,
                                                                  self.mount)
class ProcessInfo:
    name = None
    time = '-'
    count = 0
    cpu = '-'
    memory = '-'
    pids = None
    
    def __unicode__(self):
        return u"name %s, time %s, count %s, cpu %s, mem %s, pids %s" % (self.name,
                                                                         self.time,
                                                                         self.count,
                                                                         self.cpu,
                                                                         self.memory,
                                                                         self.pids)
    
class SystemStatus:
    
    commands = {}
    
    @property
    def hostname(self):
        return platform.node()
    
    @property
    def time(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    @property
    def uname(self):
        return " ".join(platform.uname())
    
    def execute(self, cmd, *args):
        if args:
            return get_command_output(self.commands[cmd] % args)
        return get_command_output(self.commands[cmd])
        
    def current_cpu_usage(self):
        raise NotImplementedError
    
    def current_memory_usage(self):
        raise NotImplementedError
   
    def disk_usage(self):
        raise NotImplementedError
    
    def watched_process(self):
        res = []
        for proc in Process.select():
            p = self.get_process_status(proc.search_string)
            p.name = proc.name
            res.append(p)
        return res
    
    def get_process_status(self, search):
        raise NotImplementedError
    
class DummyStatus(SystemStatus):

    def current_cpu_usage(self):
        return "19:02:06 up 1 day,  4:49,  1 user,  load average: 0.01, 0.04, 0.05"
    
    def current_memory_usage(self):
        data = {'free': 500, 'total': 1000, 'swaptotal': 500, 'swapfree': 200, 'used': 100, 'swapused': 50}
        return data
    
    def disk_usage(self):
        d = DiskUsage()
        d.dev = '/dev/sda1'
        d.size = '20g'
        d.used = '5g'
        d.avail = '6'
        d.usep = '18%'
        d.mount = '/'
        disks = [d,]
        return disks
    
    def get_process_status(self, search):
        return ProcessInfo()
        