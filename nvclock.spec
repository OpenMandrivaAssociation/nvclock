%define name	nvclock
%define version 0.8
%define beta	b2
%define release %mkrel 0.%{beta}.1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Overclocking tool for NVIDIA graphic boards
URL:		http://www.linuxhardware.org/nvclock/
Source:		http://www.linuxhardware.org/nvclock/%{name}%{version}%{beta}.tar.bz2
License:	GPL
Group:		System/Configuration/Hardware
BuildRequires:	gtk+2-devel
BuildRequires:	qt3-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This program allows you to overclock your nvidia card under linux.

%prep

%setup -q -n %{name}%{version}%{beta}

%build
export PATH=$PATH:%{_libdir}/qt3/bin
%configure
# parallel build doesn't work
make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%_bindir

%makeinstall

mkdir -p %{buildroot}%{_menudir}
cat << EOF > %{buildroot}/%{_menudir}/%name
?package(%name):\
	needs="x11"\
	section="System/Configuration/Hardware"\
	title="Nvclock"\
	longtitle="Overclocking tool for NVIDIA graphic boards"\
	icon="hardware_section.png"\
	command="nvclock" \
	xdg="true"
EOF
rm -rf %buildroot/%_datadir/doc/nvclock

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=nvclock
Comment=Overclocking tool for NVIDIA graphic boards
Exec=%{name}
Icon=hardware_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-System-Configuration-Hardware;Settings;HardwareSettings;
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
%{_bindir}/*
%{_menudir}/%name
%{_mandir}/man1/*
%_datadir/applications/*
