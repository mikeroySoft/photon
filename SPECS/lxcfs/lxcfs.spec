Summary:     Linux Containers File System
Name:        lxcfs
Version:     4.0.8
Release:     1%{?dist}
URL:         https://linuxcontainers.org/lxcfs/downloads/
Source0:     %{name}-%{version}.tar.gz
License:     LGPL 2.1+
Group:       System Environment/Libraries
%define sha1 %{name}=a3d56725f8f9997ba6663840a5802fad99a737d5
Vendor:		 VMware, Inc.
Distribution:  Photon
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: fuse-devel
BuildRequires: systemd
Requires:      fuse

%description
LXCFS is a simple userspace filesystem designed to work around some current limitations of the Linux kernel.

%prep
%setup -q

%build
%configure \
	--with-init-script=systemd
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/%{_sharedstatedir}/%{name}

%post
%systemd_post lxcfs.service

%preun
%systemd_preun lxcfs.service

%postun
%systemd_postun lxcfs.service

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{_sharedstatedir}/%{name}
/lib/systemd/system/%{name}.service
%{_bindir}/lxcfs
%config(noreplace) %{_datarootdir}/lxc/config/common.conf.d/00-%{name}.conf
%{_datarootdir}/%{name}/lxc.mount.hook
%{_datarootdir}/%{name}/lxc.reboot.hook
%{_libdir}/%{name}/liblxcfs.la
%{_libdir}/%{name}/liblxcfs.so

%changelog
* Mon May 03 2021 Gerrit Photon <photon-checkins@vmware.com> 4.0.8-1
- Automatic Version Bump
* Tue Apr 13 2021 Gerrit Photon <photon-checkins@vmware.com> 4.0.7-1
- Automatic Version Bump
* Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 4.0.5-1
- Automatic Version Bump
* Wed Apr 22 2020 Anish Swaminathan <anishs@vmware.com>  4.0.3-1
- Initial release.
