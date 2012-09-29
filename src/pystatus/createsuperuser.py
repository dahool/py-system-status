#!/usr/bin/env python
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

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import getpass
from pystatus.app import auth

def gather_input(prompt, default):
    if default:
        value = raw_input(prompt + " (%s): " % default)
    else:
        value = raw_input(prompt + ": ")
    if default and value == '': value = default
    if not value: value = gather_input(prompt, default)
    return value
    
def ask_user_info(username, email, password):
    username = gather_input("Username", username)
    email = gather_input("E-mail", email)

    while 1:
        password = getpass.getpass()
        password2 = getpass.getpass('Password (again): ')
        if password != password2:
            sys.stderr.write("Error: Your passwords didn't match.\n")
            password = None
            continue
        if password.strip() == '':
            sys.stderr.write("Error: Blank passwords aren't allowed.\n")
            password = None
            continue
        break
    
    admin = auth.User(username=username, email=email, admin=True, active=True)
    admin.set_password(password)
    return admin
                
def create_user():
    username = None
    password = None
    email = None
    while 1:
        admin = ask_user_info(username, email, password)
        try:
            admin.save()
        except Exception, e:
            sys.stderr.write("Error: %s.\n" % str(e))
        else:
            sys.stdout.write("Created %s.\n" % admin.username)
            break

if __name__ == '__main__':
    create_user()