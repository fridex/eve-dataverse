#!/usr/bin/env python3
#
# Copyright(C) 2019 Christoph Görn
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>


"""This is just a Test."""


import os
import logging

import daiquiri
import requests


from . import EVE_ONLINE_BASE_URL, _cache


_LOGGER = daiquiri.getLogger(__name__)


@_cache.memoize(typed=True, expire=600)
def get_order_history(region_id: int, type_id: int) -> dict:
    payload = {}
    r = requests.get(
        f"{EVE_ONLINE_BASE_URL}/markets/{region_id}/history?datasource=tranquility&type_id={type_id}", params=payload
    )

    return r.json()
