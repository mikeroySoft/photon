%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name addressable

Name: rubygem-addressable
Version:        2.7.0
Release:        2%{?dist}
Summary:        An easy-to-use client library for making requests from Ruby.
Group:          Development/Libraries
Vendor:         VMware, Inc.
Distribution:   Photon
License:        Apache-2.0
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
%define sha1    addressable=3b46d08ed6a0e2bef1bf16769c4e528c6ebc0a37
BuildRequires:  ruby >= 2.0.0
Requires: rubygem-public_suffix >= 2.0.2, rubygem-public_suffix < 5.0
BuildArch: noarch

%description
Addressable is a replacement for the URI implementation that is part of Ruby's standard library.
It more closely conforms to the relevant RFCs and adds support for IRIs and URI templates.

%prep
%setup -q -c -T

%build

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{SOURCE0}

%files
%defattr(-,root,root,-)
%{gemdir}

%changelog
*   Tue Sep 22 2020 Gerrit Photon <photon-checkins@vmware.com> 2.7.0-2
-   Update rubygem-public_suffix version
*   Thu Jul 16 2020 Gerrit Photon <photon-checkins@vmware.com> 2.7.0-1
-   Automatic Version Bump
*   Thu Aug 22 2019 Stanislav Hadjiiski <hadjiiskis@vmware.com> 2.6.0-1
-   Initial build
