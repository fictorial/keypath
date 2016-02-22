keypath
=======

Simple Python utilities for getting/setting values along a "key path" which is
just a string with attributes joined on a period (.).  If an item along the
path is a tuple or list, the corresponding key path component must be an
integer index.

::

    py.test --doctest-modules keypath
