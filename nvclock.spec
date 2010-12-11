%define beta b4

Summary:	Overclocking tool for NVIDIA graphic boards
Name:		nvclock
Version:	0.8
Release:	%mkrel 0.%{beta}.3
License:	GPLv2+
Group:		System/Configuration/Hardware
URL:		http://www.linuxhardware.org/nvclock/
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
