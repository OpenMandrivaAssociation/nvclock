%define beta b4

Summary:	Overclocking tool for NVIDIA graphic boards
Name:		nvclock
Version:	0.8
Release:	%mkrel 0.%{beta}.4
License:	GPLv2+
Group:		System/Configuration/Hardware
URL:		https://www.linuxhardware.org/nvclock/
Source:		http://www.linuxhardware.org/nvclock/%{name}%{version}%{beta}.tar.bz2
Patch0:		%{name}0.8b4-makefile.patch
BuildRequires:	gtk+2-devel
BuildRequires:	desktop-file-utils
Obsoletes:	%{name}-gtk < 0.8-0.b4.1
Obsoletes:	%{name}-qt3 < 0.8-0.b4.1
Provides:	%{name}-gtk
Provides:	%{name}-qt3
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This program allows you to overclock your nvidia card under linux.

%prep
%setup -q -n %{name}%{version}%{beta}
%patch0 -p1

%build
%configure2_5x \
	--enable-gtk \
	--disable-qt \
	--enable-nvcontrol

%make -j1

%install
rm -rf %{buildroot}

%makeinstall_std

desktop-file-install \
	--add-category="HardwareSettings" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

sed -i -e 's/^Icon=%{name}.png$/Icon=%{name}/g' %{buildroot}%{_datadir}/applications/*

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_mandir}/man1/*


%changelog
* Sat Apr 16 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8-0.b4.4mdv2011.0
+ Revision: 653306
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.8-0.b4.2mdv2010.0
+ Revision: 440355
- rebuild

* Tue Jan 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8-0.b4.1mdv2009.1
+ Revision: 334633
- update to new version 0.82-beta4
- drop qt3 subpackage
- drop patch 1
- rediff patch 0

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.8-0.b3.1mdv2009.0
+ Revision: 218425
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Jan 05 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8-0.b3.1mdv2008.1
+ Revision: 145770
- new license policy
- export %%qt3dir
- update to latest release (beta3)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8-0.b2.4mdv2008.0
+ Revision: 76390
- tune up desktop files

* Thu Aug 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8-0.b2.3mdv2008.0
+ Revision: 76301
- fix build on x86_64 (P1)
- fix makefile (P0)
- move binaries to the separate subpackages, now we have gtk and qt3 frontend ;)
- use a hack for make
- provide desktop files
- fix desktop file
- some cleans
- drop old menu style
- Import nvclock



* Mon Oct 09 2006 Lenny Cartier <lenny@mandriva.com> 0.8-0.b2.1mdv2007.1
- beta2
- fix menu & xdg

* Fri Jan 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.8-0.b.1mdk
- New release
- spec cleanup

* Tue Aug 17 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.7-2mdk
- rebuild

* Tue Jul 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.7-1mdk
- 0.7

* Sun Jul  6 2003 Götz Waschk <waschk@linux-mandrake.com> 0.6.2-2mdk
- fix url (thanks to Nilmoni Deb)

* Tue Feb  4 2003 Götz Waschk <waschk@linux-mandrake.com> 0.6.2-1mdk
- new version

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.6.1-2mdk
- rebuild

* Thu Jan 23 2003 Götz Waschk <waschk@linux-mandrake.com> 0.6.1-1mdk
- new version

* Mon Nov 18 2002 Götz Waschk <waschk@linux-mandrake.com> 0.6-2mdk
- remove unpackaged but installed files
- fix URL (thanks Nilmoni Deb) 

* Mon Oct  7 2002 Götz Waschk <waschk@linux-mandrake.com> 0.6-1mdk
- fix icon
- 0.6
- gtk2

* Thu Mar 21 2002 Götz Waschk <waschk@linux-mandrake.com> 0.5-2mdk
- add menu entry

* Tue Mar 19 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.5-1mdk
- 0.5

* Wed Aug 22 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.4.1-1mdk
- updated to 0.4.1

* Wed Jun 06 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.4-1mdk
- updated by Götz Waschk <waschk@linux-mandrake.com> :
	- 0.4
	- enable gtk gui

* Mon Apr 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.2-1mdk
- added in contribs by Götz Waschk <waschk@linux-mandrake.com> :
	- initial package
