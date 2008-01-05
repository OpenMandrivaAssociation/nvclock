%define beta b3

Summary:	Overclocking tool for NVIDIA graphic boards
Name:		nvclock
Version:	0.8
Release:	%mkrel 0.%{beta}.1
License:	GPLv2+
Group:		System/Configuration/Hardware
URL:		http://www.linuxhardware.org/nvclock/
Source:		http://www.linuxhardware.org/nvclock/%{name}%{version}%{beta}.tar.bz2
Patch0:		%{name}0.8b2-makefile.patch
Patch1:		%{name}0.8b2-lib64.patch
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
%patch0 -p1
%patch1 -p1

%build
./autogen.sh
export PATH=%{qt3dir}/bin:$PATH

%configure2_5x \
	--enable-gtk \
	--enable-qt \
	--enable-nvcontrol \
	--with-qtdir=%{qt3dir} \
	--with-qt-libs=%{qt3lib}

# parallel build doesn't work
%(echo %make|perl -pe 's/-j\d+/-j1/g')

%install
rm -rf %{buildroot}

%makeinstall_std mandir=%{_mandir}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}-gtk.desktop << EOF
[Desktop Entry]
Name=nvclock-gtk
Comment=Overclocking tool for NVIDIA graphic boards
Exec=%{name}_gtk
Icon=hardware_section
Terminal=false
Type=Application
Categories=GTK;Settings;HardwareSettings;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-qt.desktop << EOF
[Desktop Entry]
Name=nvclock-qt3
Comment=Overclocking tool for NVIDIA graphic boards
Exec=%{name}_qt
Icon=hardware_section
Terminal=false
Type=Application
OnlyShowIn=KDE;
Categories=QT;Settings;HardwareSettings;
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
