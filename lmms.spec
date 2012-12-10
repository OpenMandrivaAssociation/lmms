%define Werror_cflags %nil

Summary:	Linux MultiMedia Studio
Name:		lmms
Version:	0.4.13
Release:	2
Group:		Sound
License:	GPLv2+
URL:		http://lmms.sourceforge.net/
Source0:	https://downloads.sourceforge.net/project/lmms/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source10:	%{name}-16.png
Source11:	%{name}-32.png
Source12:	%{name}-48.png
Patch0:		%{name}.desktop.patch
Patch1:		lmms-0.4.12-gcc47.patch
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	SDL_sound-devel
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xinerama)

%description
LMMS aims to be a free alternative to popular (but commercial and closed-
source) programs like FruityLoops/FL Studio, Cubase and Logic allowing you
to produce music with your computer.This includes creation of loops,
synthesizing and mixing sounds, arranging samples, having fun with your
MIDI-keyboard and much more...

LMMS combines the features of a tracker-/sequencer-program and those
of powerful synthesizers, samplers, effects etc. in a modern, user-friendly
and easy to use graphical user-interface.

Features

* Song-Editor for arranging the song
* creating beats and basslines using the Beat-/Bassline-Editor
* easy-to-use piano-roll for editing patterns and melodies
* instrument and effect-plugins
* support for hosting VST(i)- and LADSPA-plugins (instruments/effects)
* automation-editor
* MIDI-support

%package devel
Summary:	Development package for %{name}
Group:		Development/C

%description devel
Development files and headers for %{name}.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

# remove spurious x-bits
find . -type f -exec chmod 0644 {} \;

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib}
%make

%install
%makeinstall_std -C build

install -m644 %{SOURCE10} -D %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE11} -D %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}/%{_iconsdir}/hicolor/48x48/apps/%{name}.png

rm -f %{buildroot}/%{_libdir}/%{name}/*.a %{buildroot}%{_datadir}/menu/*

%files
%doc README AUTHORS TODO
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man?/*
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/lmms.png

%files devel
%{_includedir}/lmms


