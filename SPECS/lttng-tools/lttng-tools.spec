Summary: LTTng is an open source tracing framework for Linux.
Name:    lttng-tools
Version: 2.12.3
Release: 1%{?dist}
License: GPLv2 and LGPLv2
URL: https://lttng.org/download/
Source: %{name}-%{version}.tar.bz2
%define sha1 lttng-tools=b9fa95ae8a4f7e09f78336242d3d43612a4efb2c
Group:      Development/Tools
Vendor:     VMware, Inc.
Distribution:  Photon

BuildRequires: libxml2-devel >= 2.7.6
BuildRequires: nss-devel
BuildRequires: m4
BuildRequires: elfutils-devel
BuildRequires: popt-devel
BuildRequires: userspace-rcu-devel >= 0.8.0
BuildRequires: lttng-ust-devel >= 2.9.0
Requires:      userspace-rcu
Requires:      elfutils
Requires:      nss
Requires:      libxml2
%description
LTTng is an open source tracing framework for Linux.

%prep
%setup -q

%build
autoreconf -fiv
%configure

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -delete

%files
%{_bindir}/*
%{_includedir}/*
%{_lib}/*
%{_datadir}/*
%exclude %{_libdir}/debug

%changelog
*   Tue Apr 13 2021 Gerrit Photon <photon-checkins@vmware.com> 2.12.3-1
-   Automatic Version Bump
*   Wed Aug 19 2020 Gerrit Photon <photon-checkins@vmware.com> 2.12.2-1
-   Automatic Version Bump
*   Mon Jun 22 2020 Gerrit Photon <photon-checkins@vmware.com> 2.12.1-1
-   Automatic Version Bump
*   Tue Mar 24 2020 Alexey Makhalov <amakhalov@vmware.com> 2.10.5-2
-   Fix compilation issue with glibc >= 2.30.
*   Wed Sep 05 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 2.10.5-1
-   Update to version 2.10.5
*   Fri Mar 31 2017 Michelle Wang <michellew@vmware.com> 2.9.4-1
-   Update package version
*   Tue Jul 26 2016 Divya Thaluru <dthaluru@vmware.com> 2.7.1-3
-   Added userspace-rcu-devel as build time dependent package
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.7.1-2
-   GA - Bump release of all rpms
*   Thu Jan 28 2016 Xiaolin Li <xiaolinl@vmware.com> 2.7.1-1
-   Updated to version 2.7.1
*   Tue Nov 24 2015 Xiaolin Li <xiaolinl@vmware.com> 2.7.0-1
-   Initial build.  First version
