# -*- coding: utf-8 -*-
# pysnap: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from pysnap import Snapshot


snapshots = Snapshot()

snapshots['TestDemo::test_api_me 1'] = {
    'url': '/me'
}
