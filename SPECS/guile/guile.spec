Summary:        GNU Ubiquitous Intelligent Language for Extensions
Name:           guile
Version:        2.2.7
Release:        1%{?dist}
License:        LGPLv3+
URL:            http://www.gnu.org/software/guile/
Source0:        ftp://ftp.gnu.org/pub/gnu/guile/%{name}-%{version}.tar.gz
%define sha1    guile=4e4a5b1d1ccfaee887dc4ff63c088e9452715ab2
Group:          Development/Languages
Vendor:         VMware, Inc.
Distribution:   Photon
BuildRequires:  libltdl-devel
BuildRequires:  libunistring-devel
BuildRequires:  gc-devel
BuildRequires:  libffi-devel
Requires:       libltdl
Requires:       libunistring
Requires:       gc
Requires:       libffi
Requires:       gmp
Requires:       glibc-iconv

%description
GUILE (GNU's Ubiquitous Intelligent Language for Extension) is a library
implementation of the Scheme programming language, written in C.  GUILE
provides a machine-independent execution platform that can be linked in
as a library during the building of extensible programs.

%package        devel
Summary:        Development libraries and header files for guile
Requires:       guile
Requires:       libltdl-devel
Requires:       libunistring-devel

%description    devel
The package contains libraries and header files for
developing applications that use guile.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm %{buildroot}%{_libdir}/*.scm
rm %{buildroot}%{_infodir}/*

%check
make  %{?_smp_mflags} check
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/guile/*
%{_mandir}/man1/*
%{_datadir}/aclocal/*.m4
%{_datadir}/guile/*
%{_libdir}/*.la

%files devel
%defattr(-,root,root)
%{_includedir}/guile/2.2/*.h
%{_includedir}/guile/2.2/libguile/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
*       Mon May 03 2021 Gerrit Photon <photon-checkins@vmware.com> 2.2.7-1
-       Automatic Version Bump
*       Thu Jul 16 2020 Tapas Kundu <tkundu@vmware.com> 2.0.13-3
-       Bump to build with latest libffi
*       Wed May 03 2017 Dheeraj Shetty <dheerajs@vmware.com> 2.0.13-2
-       Adding glibc-iconv to Requires section
*       Wed Jan 18 2017 Dheeraj Shetty <dheerajs@vmware.com> 2.0.13-1
-       Bumped to latest version 2.0.13 to handle CVE-2016-8606
*       Thu Oct 06 2016 ChangLee <changlee@vmware.com> 2.0.11-3
-       Modified %check
*	Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.0.11-2
-	GA - Bump release of all rpms
*	Thu Jun 18 2015 Divya Thaluru <dthaluru@vmware.com> 2.0.11-1
-	Initial build. First version
