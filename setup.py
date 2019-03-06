# encoding:utf-8
import codecs
import os
import platform
import re
import shutil
import sys

#for setup
from setuptools       import setup
from Cython.Build     import cythonize,   build_ext
from Cython.Distutils import Extension as Cython_Extension
 
CTP_Version="6.3.11"
PRJ_NAME="python_ctp"

arch = platform.architecture()
if arch != "64bit":
    myArch = "64"
elif arch != "32bit":
    myArch = "32"
else:
    raise EnvironmentError("The architecture of platform is error.")

BASE_DIR       = os.path.dirname(os.path.abspath(__file__))
MYCTP_PRJ      = os.path.join(BASE_DIR,  "python_ctp")
CTP_LIB        = os.path.join(BASE_DIR,  "ctp" , CTP_Version)

C2CYTHON_HEADER = os.path.join(MYCTP_PRJ, "c2cython")
CYTHON2C_HEADER = os.path.join(MYCTP_PRJ, "cython2c")
 
package_data = []
extra_link_args = None
extra_compile_args = None

if sys.platform == "linux":
    CTP_LIB       = os.path.join(CTP_LIB, "linux" + myArch)
    package_data.append("*.so")
    extra_compile_args = ["-Wall"]
    extra_link_args = ['-Wl,-rpath,$ORIGIN']

elif sys.platform == "win32":
    CTP_LIB = os.path.join(CTP_LIB, "windows" + myArch)
    extra_compile_args = ["/GR", "/EHsc"]
    extra_link_args = []
    package_data.append("*.dll") 

CTP_HEADER     = CTP_LIB    

common_args = {
    "cython_include_dirs": [CYTHON2C_HEADER, C2CYTHON_HEADER],
    "include_dirs": [CTP_HEADER, C2CYTHON_HEADER],
    "library_dirs": [CTP_LIB],
    "language": "c++",
    "extra_compile_args": extra_compile_args,
    "extra_link_args": extra_link_args,
}

ext_modules = [
    Cython_Extension(name=PRJ_NAME + ".MdApi",
                     sources=[ PRJ_NAME + "/MdApi.pyx"],
                     libraries=["thostmduserapi"],
                     **common_args),
    Cython_Extension(name=PRJ_NAME + ".TraderApi",
                     sources=[PRJ_NAME + "/TraderApi.pyx"],
                     libraries=["thosttraderapi"],
                     **common_args)
]


setup(
    name=PRJ_NAME,
    version=CTP_Version,
    description=CTP_Version,
    long_description=codecs.open("README.md", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    license="LGPLv3",
    keywords="SimNow,CTP,Future,SHFE,Shanghai Future Exchange",
    author="liu.changsheng",
    author_email="mail_lcs@126.com",
    url="https://github.com/datamgr/python_CTP",
    include_dirs=[CTP_HEADER, CYTHON2C_HEADER],
    platforms=["win32", "linux"],
    packages=[PRJ_NAME],
    package_data={"": package_data},
    python_requires=">=3.5",
    # cython: binding=True
    # binding = true for inspect get callargs
    ext_modules=cythonize(ext_modules,
                          compiler_directives={'language_level': 3,"binding": True}
                          ),
    cmdclass={'build_ext': build_ext},
    classifiers=[
        "Development Status ::  - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: POSIX",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries"
    ]
)