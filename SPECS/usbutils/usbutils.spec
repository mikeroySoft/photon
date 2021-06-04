Summary:       USB Utils
Name:          usbutils
Version:       013
Release:       1%{?dist}
License:       GPLv2+
URL:           http://linux-usb.sourceforge.net
Group:         Applications/System
Vendor:        VMware, Inc.
Distribution:  Photon
Source0:       https://www.kernel.org/pub/linux/utils/usb/usbutils/%{name}-%{version}.tar.xz
%define sha1   usbutils=c96072746f5be2e69e1c3243728256c93285fc1e
Source1:       usb.ids
BuildRequires: libusb-devel
BuildRequires: pkg-config
BuildRequires: systemd
Requires:      libusb
BuildRequires: systemd-devel

%description
The USB Utils package contains an utility used to display information
about USB buses in the system and the devices connected to them.

%prep
%setup -q -n %{name}-%{version}

%build
sh autogen.sh
%configure --prefix=/usr \
            --datadir=/usr/share/misc \
            --disable-zlib &&
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_datadir}/misc/
install -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/misc/

%files
%defattr(-,root,root,-)
%{_bindir}/usb-devices
%{_bindir}/lsusb
%{_bindir}/lsusb.py
%{_bindir}/usbhid-dump
%{_mandir}/*/*
%{_datadir}/misc/usb.ids

%changelog
*   Thu Apr 29 2021 Gerrit Photon <photon-checkins@vmware.com> 013-1
-   Automatic Version Bump
*   Thu Jul 09 2020 Gerrit Photon <photon-checkins@vmware.com> 012-1
-   Automatic Version Bump
*   Mon Sep 10 2018 Michelle Wang <michellew@vmware.com>  010-1
-   Update version to 010.
*   Fri Nov 18 2016 Anish Swaminathan <anishs@vmware.com>  008-4
-   Change systemd dependency
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 008-3
-   GA - Bump release of all rpms
*   Tue May 10 2016 Nick Shi <nshi@vmware.com> - 008-2
-   Update Source0 to the correct link
*   Fri May 06 2016 Nick Shi <nshi@vmware.com> - 008-1
-   Initial version
