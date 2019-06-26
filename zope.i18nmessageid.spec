#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.i18nmessageid
Version  : 4.3.1
Release  : 21
URL      : https://files.pythonhosted.org/packages/d8/0b/2b09daacbe377581125e181b5db32156db1dc4accbeb6efbbdcdb22377f0/zope.i18nmessageid-4.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/d8/0b/2b09daacbe377581125e181b5db32156db1dc4accbeb6efbbdcdb22377f0/zope.i18nmessageid-4.3.1.tar.gz
Summary  : Message Identifiers for internationalization
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.i18nmessageid-license = %{version}-%{release}
Requires: zope.i18nmessageid-python = %{version}-%{release}
Requires: zope.i18nmessageid-python3 = %{version}-%{release}
Requires: setuptools
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
``zope.i18nmessageid``
======================
.. image:: https://img.shields.io/pypi/v/zope.i18nmessageid.svg
:target: https://pypi.python.org/pypi/zope.i18nmessageid/
:alt: Latest Version

%package license
Summary: license components for the zope.i18nmessageid package.
Group: Default

%description license
license components for the zope.i18nmessageid package.


%package python
Summary: python components for the zope.i18nmessageid package.
Group: Default
Requires: zope.i18nmessageid-python3 = %{version}-%{release}

%description python
python components for the zope.i18nmessageid package.


%package python3
Summary: python3 components for the zope.i18nmessageid package.
Group: Default
Requires: python3-core

%description python3
python3 components for the zope.i18nmessageid package.


%prep
%setup -q -n zope.i18nmessageid-4.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1561568974
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zope.i18nmessageid
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/zope.i18nmessageid/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zope.i18nmessageid/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
