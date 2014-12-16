#!/usr/bin/env python
#
# Copyright 2012 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""EPoll-based IOLoop implementation for Linux systems."""
from __future__ import absolute_import, division, print_function, with_statement

import select

# To use rosbridge version of tornado 
import rosbridge_tools.tornado as tornado
from tornado.ioloop import PollIOLoop


class EPollIOLoop(PollIOLoop):
    def initialize(self, **kwargs):
        super(EPollIOLoop, self).initialize(impl=select.epoll(), **kwargs)
