#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF2A968348913D1D8 (tseaver@palladion.com)
#
Name     : zope.i18nmessageid
Version  : 4.1.0
Release  : 8
URL      : https://pypi.debian.net/zope.i18nmessageid/zope.i18nmessageid-4.1.0.tar.gz
Source0  : https://pypi.debian.net/zope.i18nmessageid/zope.i18nmessageid-4.1.0.tar.gz
Source99 : https://pypi.debian.net/zope.i18nmessageid/zope.i18nmessageid-4.1.0.tar.gz.asc
Summary  : Message Identifiers for internationalization
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.i18nmessageid-python3
Requires: zope.i18nmessageid-python
Requires: Sphinx
Requires: coverage
Requires: nose
Requires: setuptools
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
======================

%package python
Summary: python components for the zope.i18nmessageid package.
Group: Default
Requires: zope.i18nmessageid-python3

%description python
python components for the zope.i18nmessageid package.


%package python3
Summary: python3 components for the zope.i18nmessageid package.
Group: Default
Requires: python3-core

%description python3
python3 components for the zope.i18nmessageid package.


%prep
%setup -q -n zope.i18nmessageid-4.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523311124
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
