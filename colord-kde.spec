Name:           colord-kde
Version:        0.3.0
Release:        3%{?dist}
Summary:        Colord support for KDE

License:        GPLv2+
URL:            http://www.kde.org/
Source0:        http://download.kde.org/stable/colord-kde/%{version}/src/%{name}-%{version}.tar.bz2

# upstreamable patch - X-KDE-ParentApp has to be set to kcontrol to be visible

BuildRequires:  cmake kdelibs-devel colord-devel

# need kcmshell4 from kde-runtime at least (from kcm_touchpad SPEC)
Requires: kde-runtime%{?_kde4_version: >= %{_kde4_version}}

# colord is a dbus daemon
Requires: colord

%description
KDE support for colord including KDE Daemon module and System Settings module.


%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%doc COPYING MAINTAINERS TODO
%{_kde4_libdir}/kde4/*.so
%{_kde4_sharedir}/kde4/services/kded/colord.desktop
%{_kde4_sharedir}/kde4/services/kcm_colord.desktop
%{_kde4_bindir}/colord-kde-icc-importer
%{_kde4_datadir}/applications/kde4/colordkdeiccimporter.desktop

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.3.0-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.3.0-2
- Mass rebuild 2013-12-27

* Mon May 27 2013 Lukáš Tinkl <ltinkl@redhat.com> - 0.3.0-1
- New upstream version 0.3.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 05 2012 Jaroslav Reznik <jreznik@redhat.com> - 0.2.0-1
- update to version 0.2.0

* Thu Mar 22 2012 Jaroslav Reznik <jreznik@redhat.com> - 0.1.0-2
- fix kcmshell4 visibility by setting X-KDE-ParentApp

* Wed Mar 21 2012 Jaroslav Reznik <jreznik@redhat.com> - 0.1.0-1
- initial try
