# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_trie')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_trie')
    _trie = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_trie', [dirname(__file__)])
        except ImportError:
            import _trie
            return _trie
        try:
            _mod = imp.load_module('_trie', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _trie = swig_import_helper()
    del swig_import_helper
else:
    import _trie
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _trie.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _trie.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _trie.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _trie.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _trie.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _trie.SwigPyIterator_equal(self, x)

    def copy(self):
        return _trie.SwigPyIterator_copy(self)

    def next(self):
        return _trie.SwigPyIterator_next(self)

    def __next__(self):
        return _trie.SwigPyIterator___next__(self)

    def previous(self):
        return _trie.SwigPyIterator_previous(self)

    def advance(self, n):
        return _trie.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _trie.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _trie.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _trie.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _trie.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _trie.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _trie.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _trie.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class map_string_int(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, map_string_int, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, map_string_int, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _trie.map_string_int_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _trie.map_string_int___nonzero__(self)

    def __bool__(self):
        return _trie.map_string_int___bool__(self)

    def __len__(self):
        return _trie.map_string_int___len__(self)

    def __getitem__(self, key):
        return _trie.map_string_int___getitem__(self, key)

    def __delitem__(self, key):
        return _trie.map_string_int___delitem__(self, key)

    def has_key(self, key):
        return _trie.map_string_int_has_key(self, key)

    def keys(self):
        return _trie.map_string_int_keys(self)

    def values(self):
        return _trie.map_string_int_values(self)

    def items(self):
        return _trie.map_string_int_items(self)

    def __contains__(self, key):
        return _trie.map_string_int___contains__(self, key)

    def key_iterator(self):
        return _trie.map_string_int_key_iterator(self)

    def value_iterator(self):
        return _trie.map_string_int_value_iterator(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __setitem__(self, key, x):
        return _trie.map_string_int___setitem__(self, key, x)

    def __init__(self, *args):
        this = _trie.new_map_string_int(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def empty(self):
        return _trie.map_string_int_empty(self)

    def size(self):
        return _trie.map_string_int_size(self)

    def swap(self, v):
        return _trie.map_string_int_swap(self, v)

    def begin(self):
        return _trie.map_string_int_begin(self)

    def end(self):
        return _trie.map_string_int_end(self)

    def rbegin(self):
        return _trie.map_string_int_rbegin(self)

    def rend(self):
        return _trie.map_string_int_rend(self)

    def clear(self):
        return _trie.map_string_int_clear(self)

    def get_allocator(self):
        return _trie.map_string_int_get_allocator(self)

    def count(self, x):
        return _trie.map_string_int_count(self, x)

    def erase(self, *args):
        return _trie.map_string_int_erase(self, *args)

    def find(self, x):
        return _trie.map_string_int_find(self, x)

    def lower_bound(self, x):
        return _trie.map_string_int_lower_bound(self, x)

    def upper_bound(self, x):
        return _trie.map_string_int_upper_bound(self, x)
    __swig_destroy__ = _trie.delete_map_string_int
    __del__ = lambda self: None
map_string_int_swigregister = _trie.map_string_int_swigregister
map_string_int_swigregister(map_string_int)

class vector_float(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector_float, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector_float, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _trie.vector_float_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _trie.vector_float___nonzero__(self)

    def __bool__(self):
        return _trie.vector_float___bool__(self)

    def __len__(self):
        return _trie.vector_float___len__(self)

    def __getslice__(self, i, j):
        return _trie.vector_float___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _trie.vector_float___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _trie.vector_float___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _trie.vector_float___delitem__(self, *args)

    def __getitem__(self, *args):
        return _trie.vector_float___getitem__(self, *args)

    def __setitem__(self, *args):
        return _trie.vector_float___setitem__(self, *args)

    def pop(self):
        return _trie.vector_float_pop(self)

    def append(self, x):
        return _trie.vector_float_append(self, x)

    def empty(self):
        return _trie.vector_float_empty(self)

    def size(self):
        return _trie.vector_float_size(self)

    def swap(self, v):
        return _trie.vector_float_swap(self, v)

    def begin(self):
        return _trie.vector_float_begin(self)

    def end(self):
        return _trie.vector_float_end(self)

    def rbegin(self):
        return _trie.vector_float_rbegin(self)

    def rend(self):
        return _trie.vector_float_rend(self)

    def clear(self):
        return _trie.vector_float_clear(self)

    def get_allocator(self):
        return _trie.vector_float_get_allocator(self)

    def pop_back(self):
        return _trie.vector_float_pop_back(self)

    def erase(self, *args):
        return _trie.vector_float_erase(self, *args)

    def __init__(self, *args):
        this = _trie.new_vector_float(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _trie.vector_float_push_back(self, x)

    def front(self):
        return _trie.vector_float_front(self)

    def back(self):
        return _trie.vector_float_back(self)

    def assign(self, n, x):
        return _trie.vector_float_assign(self, n, x)

    def resize(self, *args):
        return _trie.vector_float_resize(self, *args)

    def insert(self, *args):
        return _trie.vector_float_insert(self, *args)

    def reserve(self, n):
        return _trie.vector_float_reserve(self, n)

    def capacity(self):
        return _trie.vector_float_capacity(self)
    __swig_destroy__ = _trie.delete_vector_float
    __del__ = lambda self: None
vector_float_swigregister = _trie.vector_float_swigregister
vector_float_swigregister(vector_float)

class vector_int(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector_int, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector_int, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _trie.vector_int_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _trie.vector_int___nonzero__(self)

    def __bool__(self):
        return _trie.vector_int___bool__(self)

    def __len__(self):
        return _trie.vector_int___len__(self)

    def __getslice__(self, i, j):
        return _trie.vector_int___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _trie.vector_int___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _trie.vector_int___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _trie.vector_int___delitem__(self, *args)

    def __getitem__(self, *args):
        return _trie.vector_int___getitem__(self, *args)

    def __setitem__(self, *args):
        return _trie.vector_int___setitem__(self, *args)

    def pop(self):
        return _trie.vector_int_pop(self)

    def append(self, x):
        return _trie.vector_int_append(self, x)

    def empty(self):
        return _trie.vector_int_empty(self)

    def size(self):
        return _trie.vector_int_size(self)

    def swap(self, v):
        return _trie.vector_int_swap(self, v)

    def begin(self):
        return _trie.vector_int_begin(self)

    def end(self):
        return _trie.vector_int_end(self)

    def rbegin(self):
        return _trie.vector_int_rbegin(self)

    def rend(self):
        return _trie.vector_int_rend(self)

    def clear(self):
        return _trie.vector_int_clear(self)

    def get_allocator(self):
        return _trie.vector_int_get_allocator(self)

    def pop_back(self):
        return _trie.vector_int_pop_back(self)

    def erase(self, *args):
        return _trie.vector_int_erase(self, *args)

    def __init__(self, *args):
        this = _trie.new_vector_int(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _trie.vector_int_push_back(self, x)

    def front(self):
        return _trie.vector_int_front(self)

    def back(self):
        return _trie.vector_int_back(self)

    def assign(self, n, x):
        return _trie.vector_int_assign(self, n, x)

    def resize(self, *args):
        return _trie.vector_int_resize(self, *args)

    def insert(self, *args):
        return _trie.vector_int_insert(self, *args)

    def reserve(self, n):
        return _trie.vector_int_reserve(self, n)

    def capacity(self):
        return _trie.vector_int_capacity(self)
    __swig_destroy__ = _trie.delete_vector_int
    __del__ = lambda self: None
vector_int_swigregister = _trie.vector_int_swigregister
vector_int_swigregister(vector_int)

class vector_vector_int(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector_vector_int, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector_vector_int, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _trie.vector_vector_int_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _trie.vector_vector_int___nonzero__(self)

    def __bool__(self):
        return _trie.vector_vector_int___bool__(self)

    def __len__(self):
        return _trie.vector_vector_int___len__(self)

    def __getslice__(self, i, j):
        return _trie.vector_vector_int___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _trie.vector_vector_int___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _trie.vector_vector_int___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _trie.vector_vector_int___delitem__(self, *args)

    def __getitem__(self, *args):
        return _trie.vector_vector_int___getitem__(self, *args)

    def __setitem__(self, *args):
        return _trie.vector_vector_int___setitem__(self, *args)

    def pop(self):
        return _trie.vector_vector_int_pop(self)

    def append(self, x):
        return _trie.vector_vector_int_append(self, x)

    def empty(self):
        return _trie.vector_vector_int_empty(self)

    def size(self):
        return _trie.vector_vector_int_size(self)

    def swap(self, v):
        return _trie.vector_vector_int_swap(self, v)

    def begin(self):
        return _trie.vector_vector_int_begin(self)

    def end(self):
        return _trie.vector_vector_int_end(self)

    def rbegin(self):
        return _trie.vector_vector_int_rbegin(self)

    def rend(self):
        return _trie.vector_vector_int_rend(self)

    def clear(self):
        return _trie.vector_vector_int_clear(self)

    def get_allocator(self):
        return _trie.vector_vector_int_get_allocator(self)

    def pop_back(self):
        return _trie.vector_vector_int_pop_back(self)

    def erase(self, *args):
        return _trie.vector_vector_int_erase(self, *args)

    def __init__(self, *args):
        this = _trie.new_vector_vector_int(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _trie.vector_vector_int_push_back(self, x)

    def front(self):
        return _trie.vector_vector_int_front(self)

    def back(self):
        return _trie.vector_vector_int_back(self)

    def assign(self, n, x):
        return _trie.vector_vector_int_assign(self, n, x)

    def resize(self, *args):
        return _trie.vector_vector_int_resize(self, *args)

    def insert(self, *args):
        return _trie.vector_vector_int_insert(self, *args)

    def reserve(self, n):
        return _trie.vector_vector_int_reserve(self, n)

    def capacity(self):
        return _trie.vector_vector_int_capacity(self)
    __swig_destroy__ = _trie.delete_vector_vector_int
    __del__ = lambda self: None
vector_vector_int_swigregister = _trie.vector_vector_int_swigregister
vector_vector_int_swigregister(vector_vector_int)

class Trie(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Trie, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Trie, name)
    __repr__ = _swig_repr
    __swig_setmethods__["children"] = _trie.Trie_children_set
    __swig_getmethods__["children"] = _trie.Trie_children_get
    if _newclass:
        children = _swig_property(_trie.Trie_children_get, _trie.Trie_children_set)
    __swig_setmethods__["backoff"] = _trie.Trie_backoff_set
    __swig_getmethods__["backoff"] = _trie.Trie_backoff_get
    if _newclass:
        backoff = _swig_property(_trie.Trie_backoff_get, _trie.Trie_backoff_set)
    __swig_setmethods__["log_prob"] = _trie.Trie_log_prob_set
    __swig_getmethods__["log_prob"] = _trie.Trie_log_prob_get
    if _newclass:
        log_prob = _swig_property(_trie.Trie_log_prob_get, _trie.Trie_log_prob_set)
    __swig_setmethods__["character"] = _trie.Trie_character_set
    __swig_getmethods__["character"] = _trie.Trie_character_get
    if _newclass:
        character = _swig_property(_trie.Trie_character_get, _trie.Trie_character_set)

    def __init__(self):
        this = _trie.new_Trie()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def load_arpa(self, filename, vocab):
        return _trie.Trie_load_arpa(self, filename, vocab)

    def get_distro(self, context, num_batches, vocab_size, batch_size, timesteps, pointer, distro):
        return _trie.Trie_get_distro(self, context, num_batches, vocab_size, batch_size, timesteps, pointer, distro)
    __swig_destroy__ = _trie.delete_Trie
    __del__ = lambda self: None
Trie_swigregister = _trie.Trie_swigregister
Trie_swigregister(Trie)

# This file is compatible with both classic and new-style classes.


