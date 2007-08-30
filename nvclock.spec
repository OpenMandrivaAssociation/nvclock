%define beta b2

Name:		nvclock
Version:	0.8
Release:	%mkrel 0.%{beta}.2
Summary:	Overclocking tool for NVIDIA graphic boards
URL:		http://www.linuxhardware.org/nvclock/
Source:		http://www.linuxhardware.org/nvclock/%{name}%{version}%{beta}.tar.bz2
License:	GPL
Group:		System/Configuration/Hardware
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This program allows you to overclock your nvidia card under linux.

%package gtk
Summary:	A GTK2 frontend for nvclock
Group:		System/Configuration/Hardware
BuildRequires:	gtk+2-devel
Requires:	%{name} = %{version}-%{release}

%description gtk
A GTK2 frontend for nvclock.

%package qt3
Summary:	A Qt3 frontend for nvclock
Group:		System/Configuration/Hardware
BuildRequires:	qt3-devel
Requires:	%{name} = %{version}-%{release}

%description qt3
A Qt3 frontend for nvclock.

%prep
%setup -q -n %{name}%{version}%{beta}

%build
%configure2_5x \
	--enable-gtk \
	--enable-qt \
	--enable-nvcontrol

# parallel build doesn't work
%(echo %make|perl -pe 's/-j\d+/-j1/g')

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}

%makeinstall

rm -rf %{buildroot}%{_datadir}/doc/nvclock

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}-gtk.desktop << EOF
[Desktop Entry]
Name=nvclock
Comment=Overclocking tool for NVIDIA graphic boards
Exec=%{name}_gtk
Icon=hardware_section
Terminal=false
Type=Application
Categories=GTK;Settings;HardwareSettings;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-qt.desktop << EOF
[Desktop Entry]
Name=nvclock
Comment=Overclocking tool for NVIDIA graphic boards
Exec=%{name}_qt
Icon=hardware_section
Terminal=false
Type=Application
OnlyShowIn=KDE;
Categories=Qt;Settings;HardwareSettings;
EOF

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/*

%files gtk
%defattr(-,root,root)
%{_bindir}/%{name}_gtk
%{_datadir}/applications/%{name}-gtk.desktop

%files qt3
%defattr(-,root,root)
%{_bindir}/%{name}_qt
%{_datadir}/applications/%{name}-qt.desktop
