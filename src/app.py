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

from marshmallow import pprint

from dataverse import universe, regions, constellations, markets, __version__

daiquiri.setup(level=logging.DEBUG)
_LOGGER = daiquiri.getLogger("eve_dataverse")

allRegions = []
allConstellations = []
allTypes = []


def harvest_region_data():
    _LOGGER.info("harvesting Region data...")

    schema = regions.RegionSchema()

    region_ids = regions.get_regions()

    for region_id in region_ids:
        region = regions.get_region(region_id)

        if region is not None:
            allRegions.append(region)

    _LOGGER.debug("writing Regions to JSON file...")
    with open("regions.json", "w") as outfile:
        outfile.write(schema.dumps(allRegions, many=True))


def harvest_constellation_data():
    _LOGGER.info("harvesting Constellation data...")

    schema = constellations.ConstellationSchema()

    for region in allRegions:
        for constellation_id in region.constellations:
            constellation = constellations.get_constellation(constellation_id)

            if constellation is not None:
                allConstellations.append(constellation)

    _LOGGER.debug("writing Constellations to JSON file...")
    with open("constellations.json", "w") as outfile:
        outfile.write(schema.dumps(allConstellations, many=True))


def harvest_type_data():
    _LOGGER.info("harvesting Type data...")

    schema = universe.TypeSchema()

    type_ids = universe.get_types()

    for type_id in type_ids:
        type_object = universe.get_type(type_id)

        if type_object is not None:
            allTypes.append(type_object)

    _LOGGER.debug("writing Types to JSON file...")
    with open("types.json", "w") as outfile:
        outfile.write(schema.dumps(allTypes, many=True))


if __name__ == "__main__":
    _LOGGER.info(f"This is Eve Online Dataverse v{__version__}.")
    _LOGGER.debug("DEBUG mode is enabled!")

    harvest_region_data()
    harvest_constellation_data()

    # region_id 10000030
    _LOGGER.info("harvesting Market data...")
