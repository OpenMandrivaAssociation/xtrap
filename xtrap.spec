Name:		xtrap
Version:	1.0.2
Release:	9
Summary:	XTrap sample clients 
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xtrap) >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
These commands are SAMPLE CLIENTS provided with the XTrap X Server
Extension Sources, Version 3.3. XTrap is an X Server extension which
facilitates the capturing of server protocol and synthesizing core
input events.

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
%{_mandir}/man1/xtrapstats.*
%{_mandir}/man1/xtrapproto.*
%{_mandir}/man1/xtrapreset.*
%{_mandir}/man1/xtrapout.*
%{_mandir}/man1/xtrapinfo.*
%{_mandir}/man1/xtrapin.*
%{_mandir}/man1/xtrapchar.*
%{_mandir}/man1/xtrap.*



%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-7mdv2011.0
+ Revision: 671373
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-6mdv2011.0
+ Revision: 608244
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-5mdv2010.1
+ Revision: 524474
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.2-4mdv2009.1
+ Revision: 350748
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.0.2-3mdv2008.1
+ Revision: 140994
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.2-3mdv2008.0
+ Revision: 80788
- rebuild for 2008
- add description
- slight spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages extension


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

