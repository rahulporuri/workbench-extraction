# (C) Copyright 2021 Enthought, Inc., Austin, TX
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in LICENSE.txt and may be redistributed only under
# the conditions described in the aforementioned license. The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
#
# Thanks for using Enthought open source!

from setuptools import setup, find_packages

if __name__ == "__main__":
    __version__ = "0.0.0"

    setup(
        name="enworkbench",
        version=__version__,
        license="BSD",
        packages=find_packages(),
        platforms=["Windows", "Linux", "Mac OS-X"],
        python_requires=">=3.6",
        zip_safe=True,
    )
