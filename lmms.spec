%define Werror_cflags %nil
# RemoteZynAddSubFx doesn't work without rpath
#global _cmake_skip_rpath %{nil}

Summary:	Linux MultiMedia Studio
Name:		lmms
Version:	1.2.0
Release:	1
Group:		Sound
License:	GPLv2+
URL:		http://lmms.sourceforge.net/
Source0:	https://github.com/LMMS/lmms/releases/download/v%{version}/lmms_%{version}.tar.xz
Source10:	%{name}-16.png
Source11:	%{name}-32.png
Source12:	%{name}-48.png
#Patch0:		%{name}.desktop.patch
#Patch1:		lmms-0.4.12-gcc47.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  git
BuildRequires:  qmake5
BuildRequires:  icoutils
BuildRequires:  fltk-fluid
BuildRequires:  fltk-devel
BuildRequires:  lame-devel
BuildRequires:  SDL_sound-devel
BuildRequires:  sndio-devel
BuildRequires:  soundio-devel
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(gig)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(vorbis)

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
%setup -q -n %{name}-%{version}%{?prel:~%{prel2}}
%autopatch -p1

# remove spurious x-bits
find . -type f -exec chmod 0644 {} \;

%build
%cmake \
      -Wno-dev \
      -DWANT_QT5=ON \
      -DWANT_SDL:BOOL=ON \
      -DWANT_PORTAUDIO:BOOL=ON \
      -DWANT_CAPS:BOOL=ON \
      -DWANT_TAP:BOOL=ON \
      -DWANT_SWH:BOOL=ON \
      -DWANT_CALF:BOOL=ON \
%ifarch %ix86
      -DWANT_VST:BOOL=ON \
%else
      -DWANT_VST:BOOL=OFF \
%endif
      -DCMAKE_INSTALL_LIBDIR=%{_lib} \
      ../
%make_build VERBOSE=1


%install
%make_install -C build

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


