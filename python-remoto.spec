#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-remoto
Version  : 1.2.1
Release  : 3
URL      : https://github.com/alfredodeza/remoto/archive/refs/tags/1.2.1.tar.gz
Source0  : https://github.com/alfredodeza/remoto/archive/refs/tags/1.2.1.tar.gz
Summary  : Execute remote commands or processes.
Group    : Development/Tools
License  : MIT
Requires: python-remoto-license = %{version}-%{release}
Requires: python-remoto-python = %{version}-%{release}
Requires: python-remoto-python3 = %{version}-%{release}
Requires: execnet
BuildRequires : buildreq-distutils3
BuildRequires : execnet
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
remoto
======
A very simplistic remote-command-executor using connections to hosts (``ssh``,
local, containers, and several others are supported) and Python in the remote
end.

%package license
Summary: license components for the python-remoto package.
Group: Default

%description license
license components for the python-remoto package.


%package python
Summary: python components for the python-remoto package.
Group: Default
Requires: python-remoto-python3 = %{version}-%{release}

%description python
python components for the python-remoto package.


%package python3
Summary: python3 components for the python-remoto package.
Group: Default
Requires: python3-core
Provides: pypi(remoto)
Requires: pypi(execnet)

%description python3
python3 components for the python-remoto package.


%prep
%setup -q -n remoto-1.2.1
cd %{_builddir}/remoto-1.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632953279
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-remoto
cp %{_builddir}/remoto-1.2.1/LICENSE %{buildroot}/usr/share/package-licenses/python-remoto/19d4c4d7eb56dd0372b859a4b8637d5aaebd6af7
cp %{_builddir}/remoto-1.2.1/debian/copyright %{buildroot}/usr/share/package-licenses/python-remoto/d33ae607a85cc800949526df38a4d0e97b7cd300
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-remoto/19d4c4d7eb56dd0372b859a4b8637d5aaebd6af7
/usr/share/package-licenses/python-remoto/d33ae607a85cc800949526df38a4d0e97b7cd300

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
