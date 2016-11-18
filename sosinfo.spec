Summary: Archey-like system information tool for StotinkaOS
Summary(bg): Archey подобно приложение за показване на системна информация в терминал за StotinkaOS
Name: sosinfo
Version: 1.2
Release: 1%{?dist}
URL: https://github.com/StotinkaOS/sosinfo
License: GPLv3
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-root
Requires: bash
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

%description
%{summary}.

%description -l bg
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/bin

install -m 755 %{name} ${RPM_BUILD_ROOT}%{_bindir}
install -Dpm 644 COPYING ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/COPYING 

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%attr(755,root,root) 
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/licenses/%{name}/COPYING

%changelog
* Fri Nov 18 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 1.2-1
- Update to 1.2

* Sun Aug 16 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 1.1-1
- Rebuild for StotinkaOS 7
- Update to 1.1
