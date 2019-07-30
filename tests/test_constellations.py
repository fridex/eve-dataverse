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


import pytest

import dataverse


class TestConstellations(object):
    def test_get_constellation(self):
        d = dataverse.constellations.get_constellation(20000001)

        assert isinstance(d, dataverse.universe.Constellation)
        assert d.constellation_id == 20000001
        assert d.name == "San Matar"
        assert 30000001 in d.systems
