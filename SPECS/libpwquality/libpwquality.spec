%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}

Summary:        It provides common functions for password quality checking
Name:           libpwquality
Version:        1.4.4
Release:        1%{?dist}
License:        BSD or GPLv2+
URL:            https://github.com/libpwquality/libpwquality
Group:          System Environment/Libraries
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        https://github.com/libpwquality/libpwquality/releases/download/libpwquality-%{version}/libpwquality-%{version}.tar.bz2
%define sha1    libpwquality=94e3f2eb67ccff1823e727d6770c3f39acbd954d

BuildRequires:  cracklib-devel
BuildRequires:  Linux-PAM-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       cracklib
Requires:       Linux-PAM

%description
The libpwquality package provides common functions for password quality
checking and also scoring them based on their apparent randomness.
The library also provides a function for generating random passwords
with good pronounceability.

%package        devel
Summary:        Header and development files
Requires:       %{name} = %{version}-%{release}
%description    devel
It contains the libraries and header files to create applications

%package -n python3-pwquality
Summary:        Python bindings for the libpwquality library
Requires:       %{name} = %{version}-%{release}
Requires:       python3

%description -n python3-pwquality
pwquality Python module that provides Python bindings
for the libpwquality library.

%prep
%setup -q

%build
%configure \
	--with-securedir=%{_libdir}/security \
	--with-pythonsitedir=%{python3_sitearch} \
	--with-python-binary=%{__python3} \
	--disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/security/pwquality.conf
%{_libdir}/*.so.*
%{_libdir}/security/pam_pwquality.so
%exclude %{_libdir}/libpwquality.la
%exclude %{_libdir}/security/pam_pwquality.la
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_datadir}/locale/*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*

%files -n python3-pwquality
%defattr(-,root,root)
%{python3_sitearch}/*.so
%{python3_sitearch}/*.egg-info

%changelog
*   Tue Apr 13 2021 Gerrit Photon <photon-checkins@vmware.com> 1.4.4-1
-   Automatic Version Bump
*   Fri Sep 25 2020 Ankit Jain <ankitja@vmware.com> 1.4.2-1
-   Initial version

