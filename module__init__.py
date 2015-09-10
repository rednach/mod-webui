#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (C) 2009-2012:
#    Gabes Jean, naparuba@gmail.com
#    Gerhard Lausser, Gerhard.Lausser@consol.de
#    Gregory Starck, g.starck@gmail.com
#    Hartmut Goebel, h.goebel@goebel-consult.de
#
# This file is part of Shinken.
#
# Shinken is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Shinken is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Shinken.  If not, see <http://www.gnu.org/licenses/>.

import os

import krillmodule
from shinken.log import logger

# Debug
import lib.bottle as bottle
bottle.debug(True)

# Look at the webui module root dir too
webuimod_dir = os.path.abspath(os.path.dirname(__file__))
htdocs_dir = os.path.join(webuimod_dir, 'htdocs')

properties = {
    'daemons': ['broker', 'scheduler'],
    'type': 'webui',
    'phases': ['running'],
    'external': True,
    }

def get_instance(plugin):
    # Only add template if we CALL webui
    bottle.TEMPLATE_PATH.append(os.path.join(webuimod_dir, 'views'))
    bottle.TEMPLATE_PATH.append(webuimod_dir)

    instance = krillmodule.Krillui_broker(plugin)
    logger.info("[WebUI] got an instance for plugin: %s", plugin.get_name())
    return instance
