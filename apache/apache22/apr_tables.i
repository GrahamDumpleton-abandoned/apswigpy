/* vim: set sw=4 expandtab : */

%module(package="apache.apache22") apr_tables

%{
#include "apr_tables.h"
%}

%nodefaultctor;
%nodefaultdtor;

%immutable;

%feature("python:nondynamic","1");

#define APR_DECLARE(type) type
#define APR_DECLARE_NONSTD(type) type

struct apr_table_t {};

%import "../_apr_tables.i"

/* Follow may not work with some compilers. */
%ignore apr_table_vdo;

%include "apr_tables.h"
