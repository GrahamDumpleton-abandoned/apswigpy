/* vim: set sw=4 expandtab : */

%module(package="apache.apache22") apr_strings

%{
#include "apr_strings.h"
%}

%nodefaultctor;
%nodefaultdtor;

%immutable;

%feature("python:nondynamic","1");

#define APR_DECLARE(type) type
#define APR_DECLARE_NONSTD(type) type
#define __attribute__(value)

/* Follow may not work with some compilers. */
%ignore apr_pvsprintf;
%ignore apr_vsnprintf;

%include "apr_strings.h"
