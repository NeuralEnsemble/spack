# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Junit4(MavenPackage):
    """A programmer-oriented testing framework for Java."""

    homepage = "https://github.com/junit-team/junit4/wiki"
    url      = "https://github.com/junit-team/junit4/archive/r4.13.tar.gz"

    version('4.13', sha256='c4e8f5681ad387a386a5aebe05ed4b73ffbfff963e154fbc4d77090f230777c7')
    version('4.12', sha256='9a5b458258c6537df0d2df7122a06895a26b9c7c8061e5991a0be81d76b10d24')

    depends_on('java@5:', type=('build', 'run'))
    depends_on('maven@3.0.4:', type='build')
