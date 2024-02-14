# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-dtcv2-util
#
# You can edit this file again by typing:
#
#     spack edit py-dtcv2-util
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyDtcv2Util(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://test.pypi.org/project/dtcv2-util"
    url = "https://test-files.pythonhosted.org/packages/4b/75/9956049142e7d07eaa7bde7baccf6fcb9beec7d3bc21466c165386808ebe/dtcv2_util-0.0.60-py3-none-any.whl"
    list_url = "https://test.pypi.org/project/dtcv2-util/#files"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    # license("UNKNOWN", checked_by="github_user1")

    version("0.0.60", sha256="c8a27488103d62f48ad739c576a223ab5c23f3972a0ce2037fb99bf756aa6fcc", expand=False)

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    depends_on("python@3.8", type=("build", "run"))
    depends_on("py-pip", type="build")
    depends_on("py-wheel", type="build")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    # depends_on("py-setuptools", type="build")
    # depends_on("py-hatchling", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")

    # FIXME: Add additional dependencies if required.
    #depends_on("py-netcdf4", type= "run")
    #depends_on("py-xarray", type="run")
    

    def config_settings(self, spec, prefix):
        # FIXME: Add configuration settings to be passed to the build backend
        # FIXME: If not needed, delete this function
        settings = {}
        return settings
