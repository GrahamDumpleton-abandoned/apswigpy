/* vim: set sw=4 expandtab : */

%module(package="apache.apache22") apr

%{
#include "apr.h"
%}

%nodefaultctor;
%nodefaultdtor;

%immutable;

#define PATH_MAX

typedef long apr_off_t;

%include "apr.h"
