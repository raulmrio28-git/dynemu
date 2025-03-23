r"""Wrapper for bindings.h

Generated with:
C:\Users\Daffin Backup\AppData\Roaming\Python\Python312\Scripts\ctypesgen -ldynemu_shared bindings.h -o bindings\python\dynemu.py --insert-file=bindings.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["dynemu_shared"] = load_library("dynemu_shared")

# 1 libraries
# End libraries

# No modules

uint8_t = c_ubyte# C:/Strawberry/c/x86_64-w64-mingw32/include/stdint.h: 36

uint16_t = c_ushort# C:/Strawberry/c/x86_64-w64-mingw32/include/stdint.h: 38

uint32_t = c_uint# C:/Strawberry/c/x86_64-w64-mingw32/include/stdint.h: 40

uint64_t = c_ulonglong# C:/Strawberry/c/x86_64-w64-mingw32/include/stdint.h: 42

u8 = uint8_t# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 3

u16 = uint16_t# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 4

u32 = uint32_t# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 5

u64 = uint64_t# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 6

Emulator = None# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 7

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 9
for _lib in _libs.values():
    if not _lib.has("dynemu_open", "cdecl"):
        continue
    dynemu_open = _lib.get("dynemu_open", "cdecl")
    dynemu_open.argtypes = []
    dynemu_open.restype = POINTER(Emulator)
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 10
for _lib in _libs.values():
    if not _lib.has("dynemu_delete", "cdecl"):
        continue
    dynemu_delete = _lib.get("dynemu_delete", "cdecl")
    dynemu_delete.argtypes = [POINTER(Emulator)]
    dynemu_delete.restype = None
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 11
for _lib in _libs.values():
    if not _lib.has("dynemu_mmap", "cdecl"):
        continue
    dynemu_mmap = _lib.get("dynemu_mmap", "cdecl")
    dynemu_mmap.argtypes = [POINTER(Emulator), u32, u32]
    dynemu_mmap.restype = None
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 12
for _lib in _libs.values():
    if not _lib.has("dynemu_upload_file", "cdecl"):
        continue
    dynemu_upload_file = _lib.get("dynemu_upload_file", "cdecl")
    dynemu_upload_file.argtypes = [POINTER(Emulator), String, c_int64, u32]
    dynemu_upload_file.restype = c_size_t
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 13
for _lib in _libs.values():
    if not _lib.has("dynemu_upload_fls_memory", "cdecl"):
        continue
    dynemu_upload_fls_memory = _lib.get("dynemu_upload_fls_memory", "cdecl")
    dynemu_upload_fls_memory.argtypes = [POINTER(Emulator), POINTER(u8)]
    dynemu_upload_fls_memory.restype = u8
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 14
for _lib in _libs.values():
    if not _lib.has("dynemu_upload_memstub", "cdecl"):
        continue
    dynemu_upload_memstub = _lib.get("dynemu_upload_memstub", "cdecl")
    dynemu_upload_memstub.argtypes = [POINTER(Emulator), u32, u32, u32, u8]
    dynemu_upload_memstub.restype = None
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 15
for _lib in _libs.values():
    if not _lib.has("dynemu_upload_memstub_nooffset", "cdecl"):
        continue
    dynemu_upload_memstub_nooffset = _lib.get("dynemu_upload_memstub_nooffset", "cdecl")
    dynemu_upload_memstub_nooffset.argtypes = [POINTER(Emulator), u32, u32, u8]
    dynemu_upload_memstub_nooffset.restype = None
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 16
for _lib in _libs.values():
    if not _lib.has("dynemu_read_u8", "cdecl"):
        continue
    dynemu_read_u8 = _lib.get("dynemu_read_u8", "cdecl")
    dynemu_read_u8.argtypes = [POINTER(Emulator), u32]
    dynemu_read_u8.restype = u8
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 17
for _lib in _libs.values():
    if not _lib.has("dynemu_read_u16", "cdecl"):
        continue
    dynemu_read_u16 = _lib.get("dynemu_read_u16", "cdecl")
    dynemu_read_u16.argtypes = [POINTER(Emulator), u32, u8]
    dynemu_read_u16.restype = u16
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 18
for _lib in _libs.values():
    if not _lib.has("dynemu_read_u32", "cdecl"):
        continue
    dynemu_read_u32 = _lib.get("dynemu_read_u32", "cdecl")
    dynemu_read_u32.argtypes = [POINTER(Emulator), u32, u8]
    dynemu_read_u32.restype = u32
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 19
for _lib in _libs.values():
    if not _lib.has("dynemu_read_u64", "cdecl"):
        continue
    dynemu_read_u64 = _lib.get("dynemu_read_u64", "cdecl")
    dynemu_read_u64.argtypes = [POINTER(Emulator), u32, u8]
    dynemu_read_u64.restype = u64
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 20
for _lib in _libs.values():
    if not _lib.has("dynemu_write_u8", "cdecl"):
        continue
    dynemu_write_u8 = _lib.get("dynemu_write_u8", "cdecl")
    dynemu_write_u8.argtypes = [POINTER(Emulator), u32, u8]
    dynemu_write_u8.restype = None
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 21
for _lib in _libs.values():
    if not _lib.has("dynemu_write_u16", "cdecl"):
        continue
    dynemu_write_u16 = _lib.get("dynemu_write_u16", "cdecl")
    dynemu_write_u16.argtypes = [POINTER(Emulator), u32, u16, u8]
    dynemu_write_u16.restype = None
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 22
for _lib in _libs.values():
    if not _lib.has("dynemu_write_u32", "cdecl"):
        continue
    dynemu_write_u32 = _lib.get("dynemu_write_u32", "cdecl")
    dynemu_write_u32.argtypes = [POINTER(Emulator), u32, u32, u8]
    dynemu_write_u32.restype = None
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 23
for _lib in _libs.values():
    if not _lib.has("dynemu_write_u64", "cdecl"):
        continue
    dynemu_write_u64 = _lib.get("dynemu_write_u64", "cdecl")
    dynemu_write_u64.argtypes = [POINTER(Emulator), u32, u64, u8]
    dynemu_write_u64.restype = None
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 24
for _lib in _libs.values():
    if not _lib.has("dynemu_read_bytes", "cdecl"):
        continue
    dynemu_read_bytes = _lib.get("dynemu_read_bytes", "cdecl")
    dynemu_read_bytes.argtypes = [POINTER(Emulator), u32, POINTER(u8), u32]
    dynemu_read_bytes.restype = None
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 25
for _lib in _libs.values():
    if not _lib.has("dynemu_write_bytes", "cdecl"):
        continue
    dynemu_write_bytes = _lib.get("dynemu_write_bytes", "cdecl")
    dynemu_write_bytes.argtypes = [POINTER(Emulator), u32, POINTER(u8), u32]
    dynemu_write_bytes.restype = None
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 26
for _lib in _libs.values():
    if not _lib.has("dynemu_execute", "cdecl"):
        continue
    dynemu_execute = _lib.get("dynemu_execute", "cdecl")
    dynemu_execute.argtypes = [POINTER(Emulator), u32, u8]
    dynemu_execute.restype = u32
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 27
for _lib in _libs.values():
    if not _lib.has("dynemu_read_reg", "cdecl"):
        continue
    dynemu_read_reg = _lib.get("dynemu_read_reg", "cdecl")
    dynemu_read_reg.argtypes = [POINTER(Emulator), u8]
    dynemu_read_reg.restype = u32
    break

# D:\\Daffin\\TheNewMobileTools\\subtask\\c_subproj\\dynarmic_qmg_decoder\\bindings.h: 28
for _lib in _libs.values():
    if not _lib.has("dynemu_write_reg", "cdecl"):
        continue
    dynemu_write_reg = _lib.get("dynemu_write_reg", "cdecl")
    dynemu_write_reg.argtypes = [POINTER(Emulator), u8, u32]
    dynemu_write_reg.restype = None
    break

# Begin inserted files
# Begin "bindings.py"

from ctypes import *

class Dynemu():
    def __init__(self):
        self._dynemu = dynemu_open()
    
    def __del__(self):
        dynemu_delete(self._dynemu)
        
    def memory_map(self, vaddr: int, size: int):
        dynemu_mmap(self._dynemu, vaddr, size)
        
    def upload_file(self, filename: str, dest: int, size: int):
        return dynemu_upload_file(self._dynemu, filename, dest, size)
        
    def upload_fls_memory(self, data: bytes|bytearray):
        temp = (c_ubyte * len(data)).from_buffer(bytearray(data))
        return dynemu_upload_fls_memory(self._dynemu, temp)
        
    def upload_memstub(self, dest: int=-1, mem_start: int=0xa0000000, mem_size: int=0x2000000, is_big: bool=False):
        if dest == -1:
            dynemu_upload_memstub_nooffset(self._dynemu, mem_start, mem_size, is_big)
            
        else:
            dynemu_upload_memstub(self._dynemu, dest, mem_start, mem_size, is_big)
        
    def read_u8(self, vaddr: int):
        return dynemu_read_u8(self._dynemu, vaddr)
    
    def read_u16(self, vaddr: int, is_big: bool=False):
        return dynemu_read_u16(self._dynemu, vaddr, is_big)
    
    def read_u32(self, vaddr: int, is_big: bool=False):
        return dynemu_read_u32(self._dynemu, vaddr, is_big)
    
    def read_u64(self, vaddr: int, is_big: bool=False):
        return dynemu_read_u64(self._dynemu, vaddr, is_big)
    
    def write_u8(self, vaddr: int, value: int):
        return dynemu_write_u8(self._dynemu, vaddr, value)
    
    def write_u16(self, vaddr: int, value: int, is_big: bool=False):
        return dynemu_write_u16(self._dynemu, vaddr, value, is_big)
    
    def write_u32(self, vaddr: int, value: int, is_big: bool=False):
        return dynemu_write_u32(self._dynemu, vaddr, value, is_big)
    
    def write_u64(self, vaddr: int, value: int, is_big: bool=False):
        return dynemu_write_u64(self._dynemu, vaddr, value, is_big)
        
    def read_bytes(self, vaddr: int, size: int):
        temp = (c_ubyte * size)()
        dynemu_read_bytes(self._dynemu, vaddr, temp, size)
        return bytes(temp)
    
    def write_bytes(self, vaddr: int, data: bytes|bytearray):
        temp = (c_ubyte * len(data)).from_buffer(bytearray(data))
        dynemu_write_bytes(self._dynemu, vaddr, temp, len(data))
        
    def execute(self, pc: int, is_big: bool=False):
        return dynemu_execute(self._dynemu, pc, is_big)
        
    def get_reg(self, reg: int):
        return dynemu_read_reg(self._dynemu, reg)
    
    def set_reg(self, reg: int, value: int):
        dynemu_write_reg(self._dynemu, reg, value)
        
    
# End "bindings.py"

# 1 inserted files
# End inserted files

# No prefix-stripping

