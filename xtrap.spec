Name: xtrap
Version: 1.0.2
Release: %mkrel 2
Summary: XTrap sample clients 
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxtrap-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
CHECK

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xtrapin
%{_bindir}/xtrapproto
%{_bindir}/xtrapreset
%{_bindir}/xtrapstats
%{_bindir}/xtrapchar
%{_bindir}/xtrapinfo
%{_bindir}/xtrapout
%{_mandir}/man1/xtrapstats.1x.bz2
%{_mandir}/man1/xtrapproto.1x.bz2
%{_mandir}/man1/xtrapreset.1x.bz2
%{_mandir}/man1/xtrapout.1x.bz2
%{_mandir}/man1/xtrapinfo.1x.bz2
%{_mandir}/man1/xtrapin.1x.bz2
%{_mandir}/man1/xtrapchar.1x.bz2
%{_mandir}/man1/xtrap.1x.bz2


