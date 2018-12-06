# http://github.com/hashicorp/scada-client

%global goipath         github.com/hashicorp/scada-client
%global commit          84989fd23ad4cc0e7ad44d6a871fd793eb9beb0a


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.14%{?dist}
Summary:        Implements a Golang client to the HashiCorp SCADA system 
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/armon/go-metrics)
BuildRequires: golang(github.com/hashicorp/go-multierror)
BuildRequires: golang(github.com/hashicorp/net-rpc-msgpackrpc)
BuildRequires: golang(github.com/hashicorp/yamux)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
files="$(find . -iname '*.pem')"
%goinstall glide.lock glide.yaml $files

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.git84989fd
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20150829git84989fd
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git84989fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git84989fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git84989fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git84989fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git84989fd
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git84989fd
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git84989fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.4.git84989fd
- Bump to upstream 84989fd23ad4cc0e7ad44d6a871fd793eb9beb0a
  related: #1250476

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.gitc26580c
- Update to spec-2.1
  related: #1250476

* Thu Aug 06 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.gitc26580c
- Update spec file to spec-2.0
  resolves: #1250476

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitc26580c
- First package for Fedora
  resolves: #1212113

