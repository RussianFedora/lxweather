%global gitcommit 7255fb4
%global gitcommit_full 7255fb4f77d9ea3c0bf542a7cf16e63a60367ab6

Name:           lxweather
Version:        0.0.1
Release:        1%{?dist}
Summary:        A lightweight GTK+ weather application

License:        GPLv2+
URL:            https://github.com/psipika/lxweather
Source0:        https://github.com/psipika/lxweather/tarball/%{gitcommit_full}

BuildRequires:  lxpanel-devel
BuildRequires:  libxml2-devel


%description
It is a lightweight GTK+-2.0 application which provides weather
conditions and forecast information for a specified location or locations.

%package lxpanel-plugin
Summary:        Weather plugin for lxpanel
Requires:       lxpanel

%description lxpanel-plugin
Weather plugin for LXDE's lxpanel.

%prep
%setup -q -n psipika-%{name}-%{gitcommit}


%build
export LDFLAGS="-lpthread"
%configure
make %{?_smp_mflags}


%install
%make_install
find %{buildroot} -regex '.*.\(l\)?a' -delete
mkdir -p %{buildroot}%{_libdir}/lxpanel/plugins/
ln -s %{_libdir}/libweather.so %{buildroot}%{_libdir}/lxpanel/plugins/weather.so

%post -n %{name} -p /sbin/ldconfig

%postun -n %{name} -p /sbin/ldconfig

%post lxpanel-plugin -p /sbin/ldconfig

%postun lxpanel-plugin -p /sbin/ldconfig


%files
%doc AUTHORS COPYING COPYRIGHT README
%{_bindir}/lxweather

%files lxpanel-plugin
%{_libdir}/libweather.so*
%{_libdir}/lxpanel/plugins/weather.so

%changelog
* Mon Jun 03 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.0.1-1.R
- Initial release
