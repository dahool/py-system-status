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
from peewee import *
from pystatus.app import db

class Process(db.Model):
    name = CharField(max_length=20)
    search_string = CharField(max_length=100)
    
    def __unicode__(self):
        return u'%s' % self.name
    
    class Meta:
        ordering = ('name',)