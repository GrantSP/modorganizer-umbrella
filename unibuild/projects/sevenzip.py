# Copyright (C) 2015 Sebastian Herbord. All rights reserved.
#
# This file is part of Mod Organizer.
#
# Mod Organizer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mod Organizer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mod Organizer.  If not, see <http://www.gnu.org/licenses/>.


from unibuild import Project
from unibuild.modules import urldownload


# newer versions are beta as of now. They have slightly (?) different api as well
sevenzip_version = "9.20"

# sevenzip is not built here as we only use its source
Project("7zip") \
    .depend(urldownload.URLDownload("http://www.7-zip.org/a/7z{}.tar.bz2".format(sevenzip_version.replace(".", ""))))
""" alternative download from sourceforge, but doesn't seem to contain the 9.20 source

    sourceforge.Release("sevenzip",
                                "7-Zip/{0}/7z{1}-src.7z".format(sevenzip_version,
                                                                         sevenzip_version.replace(".", ""))))

"""

