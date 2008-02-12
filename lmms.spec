Summary:	FruityLoops clone for linux
Name:		lmms
Version:	0.3.1
Release:	%mkrel 2
Group:		Sound
License:	GPLv2+
URL:		http://lmms.sourceforge.net/
Source:		http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Source1:	x-lmms-project.desktop
Patch0:		lmms-0.3.0-fix-desktop.patch
Patch1:		lmms-0.3.1-lib64-plugins.patch
Source10:	%{name}-16.png
Source11:	%{name}-32.png
Source12:	%{name}-48.png
BuildRequires:	kdelibs-devel >= 3.2
BuildRequires:	libSDL-devel
BuildRequires:	libjack-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	SDL_sound-devel

%description
LMMS aims to be a free alternative to popular 
(but commercial and closed- source) 
programs like FruityLoops, Cubase and Logic giving 
you the ability of producing 
music with your computer by creating/synthesizing sounds, 
arranging samples, 
playing live with keyboard and much more...

LMMS combines the features of a tracker-/sequencer-program 
(pattern-/channel-/ sample-/song-/effect-management) 
and those of powerful synthesizers and samplers in a modern, 
user-friendly and easy to use graphical user-interface

%prep
%setup -q
%patch0 -p0 -b .desktop

%ifnarch ix86
%patch1 -p1 -b .plugins
%endif

%build
perl -pi -e 's/\$QTDIR\/lib/\$QTDIR\/%{_lib}/' configure
%configure2_5x --without-singerbot --without-vst 
%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -m644 %{SOURCE1} -D %{buildroot}%{_datadir}/mimelnk/application/x-lmms-project.desktop

install -m644 %{SOURCE10} -D %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE11} -D %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}/%{_iconsdir}/hicolor/48x48/apps/%{name}.png

rm -f %{buildroot}/%{_libdir}/%{name}/*.a %{buildroot}%{_datadir}/menu/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS TODO
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man?/*
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/mimelnk/application/*.desktop

%post
%{update_menus}
%{update_mime_database}
%update_icons_cache hicolor

%postun
%{clean_menus}
%clean_mime_database
%clean_icons_cache hicolor
