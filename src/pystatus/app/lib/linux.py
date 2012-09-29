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
from . import SystemStatus, DiskUsage, ProcessInfo

def time_to_int(v):
    vs = v.split(':')
    return int(vs[0]+vs[1])

class LinuxSystemStatus(SystemStatus):
    
    commands = {
                'cpu': 'w | grep load | grep -v grep',
                'memory': 'free -o',
                'disk': 'df -h -x tmpfs -x rootfs -x devtmpfs',
                'proc': 'ps auxw | grep "%s" | grep -v grep',
                }
    
    def current_cpu_usage(self):
        return self.execute('cpu')[0].strip()
    
    def current_memory_usage(self):
        res = self.execute('memory')
        mem = res[1].split()
        swap = res[2].split()
        data = {'total': mem[1], 'used': mem[2], 'free': mem[3],
                'swaptotal': swap[1], 'swapused': swap[2], 'swapfree': swap[3]}
        return data
    
    def disk_usage(self):
        dres = []
        cres = self.execute('disk')
        for crow in cres[1:]:
            cinfo = crow.split()
            d = DiskUsage()
            d.dev = cinfo[0]
            d.size = cinfo[1]
            d.used = cinfo[2]
            d.avail = cinfo[3]
            d.usep = cinfo[4]
            d.mount = cinfo[5]
            dres.append(d)
        return dres
    
    def get_process_status(self, search):
        res = self.execute('proc', search)
        p = ProcessInfo()
        if len(res) > 0:
            part = res[0].split()
            p.count = len(res)
            p.cpu = float(part[2])
            p.pids = part[1]
            p.memory = float(part[3])
            p.time = part[9]
            for pi in res[1:]:
                part = pi.split()
                if float(part[2]) > p.cpu: p.cpu = float(part[2])
                p.memory += float(part[3])
                p.pids += ", " + part[1]
                if time_to_int(part[9]) > time_to_int(p.time): p.time = part[9]
        return p