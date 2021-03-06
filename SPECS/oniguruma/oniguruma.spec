Name:           oniguruma
Version:        6.9.7
Release:        1%{?dist}
License:        BSD
Summary:        Regular expressions library
Group:          System Environment/Libraries
Vendor:         VMware, Inc.
Distribution:   Photon
URL:            https://github.com/kkos/oniguruma/
Source0:        https://github.com/kkos/oniguruma/releases/download/v%{version}/onig-%{version}.tar.gz
%define sha1    onig=ce95a3c3ae653ad423f2868b843a46b64bdb878c
%description
Oniguruma is a regular expressions library.
The characteristics of this library is that different character encoding
for every regular expression object can be specified.
(supported APIs: GNU regex, POSIX and Oniguruma native)

%package devel
Summary:        Library providing headers and libraries to libonig
Group:          Development/Libraries
Requires:       oniguruma = %{version}-%{release}

%description devel
Development files for libonig

%prep
%setup -q
%build
autoreconf -vfi
%configure                    \
        --disable-silent-rules \
        --disable-static       \
        --with-rubydir=%{_bindir}
make

%install
make install \
        DESTDIR=%{buildroot}  \
        INSTALL="install -c -p"
find %{buildroot}/%{_libdir} -name '*.la' -delete

%check
make  check
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libonig.so.*

%files devel
%defattr(-,root,root,-)
%doc    AUTHORS
%license        COPYING
%doc    README
%doc    index.html
%lang(ja)       %doc    README_japanese
%lang(ja)       %doc    index_ja.html
%{_bindir}/onig-config
%{_libdir}/libonig.so
%{_includedir}/onig*.h
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Wed Apr 14 2021 Gerrit Photon <photon-checkins@vmware.com> 6.9.7-1
- Automatic Version Bump
* Tue Apr 13 2021 Gerrit Photon <photon-checkins@vmware.com> 6.9.6-1
- Automatic Version Bump
* Tue Jun 30 2020 Gerrit Photon <photon-checkins@vmware.com> 6.9.5-1
- Automatic Version Bump
* Mon Jul 15 2019 Dweep Advani <dadvani@vmware.com> 6.9.0-2
- Fixed CVE-2019-13224
* Mon Sep 10 2018 Him Kalyan Bordoloi <bordoloih@vmware.com> 6.9.0-1
- Upgrade to 6.9.0
- Created devel package
* Tue Aug 22 2017 Chang Lee <changlee@vmware.com> 6.5.0-1
- Initial version
