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
#     spack install py-ecmwflibs
#
# You can edit this file again by typing:
#
#     spack edit py-ecmwflibs
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyEcmwflibs(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://pypi.org/project/ecmwflibs/0.5.3"
    url = "https://files.pythonhosted.org/packages/72/05/532a3745f49c821c5bd318078511a74334f680fca37e766b8db2d5d16a98/ecmwflibs-0.5.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"
    list_url = "https://pypi.org/project/ecmwflibs/0.5.3/#files"
    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("0.5.3", sha256="ff33494a01bce52c414af1d32723be4d60c17ef7c6e6181b7d8025358f69af87", expand=False)

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    # depends_on("python@2.X:2.Y,3.Z:", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on('python', type=('build', 'run'))
    depends_on("py-wheel", type="build")
    depends_on("py-pip", type="build")
    # depends_on("py-poetry-core", type="build")

    # FIXME: Add additional dependencies if required.
    # depends_on("py-foo", type=("build", "run"))

    def config_settings(self, spec, prefix):
        # FIXME: Add configuration settings to be passed to the build backend
        # FIXME: If not needed, delete this function
        settings = {}
        return settings
