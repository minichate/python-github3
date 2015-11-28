#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request
from pygithub3.resources.users import User


class List(Request):

    uri = 'repos/{user}/{repo}/commits/{sha}'
    resource = User

class Get(Request):

    uri = 'repos/{user}/{repo}/commits/{sha}/status'

class Add(Request):

    uri = 'repos/{user}/{repo}/commits/{sha}/statuses'
