Summary:        C library that provide processing for data in the UTF-8 encoding
Name:           utf8proc
Version:        2.6.1
Release:        1%{?dist}
License:        MIT
Group:          System Environment/Libraries
Url:            https://github.com/JuliaStrings/utf8proc
# Source0:  https://github.com/JuliaStrings/utf8proc/archive/v%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
%define sha1 %{name}-%{version}=f21b3263081adfcbe102cfea8cd4cb02e71f0efc
Vendor:         VMware, Inc.
Distribution:   Photon
BuildRequires:  cmake

%description
utf8proc is a small, clean C library that provides Unicode normalization, case-folding, and other operations for data in the UTF-8 encoding.

%package        devel
Summary:        Development libraries and headers for utf8proc
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The utf8proc-devel package contains libraries, header files and documentation
for developing applications that use utf8proc.

%prep
%setup -q

%build
mkdir -p build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_BUILD_TYPE=Release        \
      -DBUILD_SHARED_LIBS=ON            \
      ..
make %{?_smp_mflags}

%install
cd build
make DESTDIR=%{buildroot} install

%check
make check

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc lump.md LICENSE.md NEWS.md README.md
%{_libdir}/libutf8proc.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/utf8proc.h
%{_libdir}/libutf8proc.so

%changelog
*       Thu Apr 29 2021 Gerrit Photon <photon-checkins@vmware.com> 2.6.1-1
-       Automatic Version Bump
*       Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 2.5.0-1
-       Automatic Version Bump
*       Tue Sep 18 2018 Ankit Jain <ankitja@vmware.com> 2.2.0-1
-       Initial Version.
