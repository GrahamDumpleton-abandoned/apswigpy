/* vim: set sw=4 expandtab : */

%module(package="apache.apache22") http_vhost

%{
#include "httpd.h"
#include "http_config.h"
#include "http_vhost.h"
%}

%nodefaultctor;
%nodefaultdtor;

%immutable;

%feature("python:nondynamic","1");

#define AP_DECLARE(type) type

%include "http_vhost.h"
