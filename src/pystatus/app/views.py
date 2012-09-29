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
import os
from flask import request, redirect, url_for, render_template, flash
from flask_peewee.utils import get_object_or_404, object_list

from . import auth, application
from .models import *

@application.route('/')
@auth.login_required
def homepage():
    user = auth.get_logged_in_user()
    if os.name == "posix":
        from .lib import linux
        status = linux.LinuxSystemStatus()
    else:
        from .lib import DummyStatus
        status = DummyStatus()
    return render_template('index.html', status=status, user=user)