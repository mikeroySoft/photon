Summary:        multi-platform support library with a focus on asynchronous I/O
Name:           libuv
Version:        1.41.0
Release:        1%{?dist}
URL:            https://codeload.github.com/libuv/libuv
License:        MIT, BSD and ISC
Group:          Development/Tools
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        https://github.com/libuv/libuv/archive/%{name}-%{version}.tar.gz
%define sha1    libuv=5dc9e2e2b6714f2b97bb5993963563dcd0e89f28

%description
libuv is a multi-platform support library with a focus on asynchronous I/O. It was primarily developed for use by Node.js, but it's also used by Luvit, Julia, pyuv, and others.
%package    devel
Summary:    Header and development files for zlib
Requires:   %{name} = %{version}-%{release}
%description    devel
Development libraries for libuv

%prep
%setup -q

%build
./autogen.sh
%configure
make V=1 %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.a' -delete
find %{buildroot} -name '*.la' -delete
install -vdm 755 %{buildroot}/%{_lib}

%check
make  %{?_smp_mflags} check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_includedir}/uv/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
*   Thu May 06 2021 Gerrit Photon <photon-checkins@vmware.com> 1.41.0-1
-   Automatic Version Bump
*   Wed Jun 03 2020 Sujay G <gsujay@vmware.com> 1.34.2-1
-   Initial build. First version
