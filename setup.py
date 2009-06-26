#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   GPX to Google Maps converter setup script
#   Copyright (C) 2009  Marc Poulhiès
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
from distutils.core import setup

setup (
    name = "gpx2googlemaps",
    description = "GPX to Google Maps converter",
    long_description = """
Converts a GPX file to an image composed
of maps from Google Maps
""",
    version = "0.1",
    author = 'Tom Payne',
    author_email = 'twpayne@gmail.com',
    url = "http://github.com/twpayne/gpx2googlemaps",
    maintainer = 'Marc Poulhiès',
    maintainer_email = 'dkm@kataplop.net',
    license = "GPL",
    packages=['gpx2gmaps'],
    scripts=["gpx2googlemaps"],
    )

