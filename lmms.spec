%define name lmms
%define version 0.3.0
%define release %mkrel 1

Name:      %{name}
Version:   %{version}
Release:   %{release}
Summary:   FruityLoops clone for linux
License:   GPL
URL:       http://lmms.sourceforge.net/
Group:     Sound
Source:    http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0:    lmms-0.3.0-fix-desktop.patch
Source10:  %{name}-16.png
Source11:  %{name}-32.png
Source12:  %{name}-48.png
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: kdelibs-devel >= 3.2
BuildRequires: libSDL-devel libalsa-devel libjack-devel
BuildRequires: libsamplerate-devel libvorbis-devel
BuildRequires: SDL_sound-devel

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

%build
%configure2_5x --without-singerbot --without-vst 
%make

%install
rm -rf %buildroot
%{makeinstall_std}

install -m644 %{SOURCE10} -D %buildroot/%{_miconsdir}/%{name}.png
install -m644 %{SOURCE11} -D %buildroot/%{_iconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %buildroot/%{_liconsdir}/%{name}.png

rm -f %buildroot/%{_libdir}/%{name}/*.a %buildroot%_datadir/menu/*

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%doc README COPYING TODO
%attr(0755,root,root) %_bindir/%{name}
%_iconsdir/%{name}.png
%_liconsdir/%{name}.png
%_miconsdir/%{name}.png
%_datadir/%{name}
%_libdir/%{name}
%_mandir/man?/*
%{_datadir}/applications/*.desktop
%_datadir/mime/packages/%{name}.xml

%post
%{update_menus}
%update_mime_database

%postun
%{clean_menus}
%clean_mime_database
