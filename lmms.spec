Summary:	Linux MultiMedia Studio
Name:		lmms
Version:	0.3.2
Release:	%mkrel 1
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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
LMMS aims to be a free alternative to popular (but commercial and closed- source) 
programs like FruityLoops/FL Studio, Cubase and Logic allowing you to produce music 
with your computer.This includes creation of loops, synthesizing and mixing sounds,
arranging samples, having fun with your MIDI-keyboard and much more...

LMMS combines the features of a tracker-/sequencer-program and those of powerful
synthesizers, samplers, effects etc. in a modern, user-friendly and easy to use
graphical user-interface.

Features

* Song-Editor for arranging the song
* creating beats and basslines using the Beat-/Bassline-Editor
* easy-to-use piano-roll for editing patterns and melodies
* instrument and effect-plugins
* support for hosting VST(i)- and LADSPA-plugins (instruments/effects)
* automation-editor
* MIDI-support

%prep
%setup -q
%patch0 -p0 -b .desktop

%if "%{_lib}" != "lib"
%patch1 -p1 -b .plugins
%endif

%build
perl -pi -e 's/\$QTDIR\/lib/\$QTDIR\/%{_lib}/' configure
%configure2_5x \
	--without-singerbot \
	--without-vst \
	--with-linux \
	--disable-static \
	--enable-hqsinc
%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -m644 %{SOURCE1} -D %{buildroot}%{_datadir}/mimelnk/application/x-lmms-project.desktop

install -m644 %{SOURCE10} -D %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE11} -D %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}/%{_iconsdir}/hicolor/48x48/apps/%{name}.png

rm -f %{buildroot}/%{_libdir}/%{name}/*.a %{buildroot}%{_datadir}/menu/*

%post
%{update_menus}
%{update_mime_database}
%update_icon_cache hicolor

%postun
%{clean_menus}
%{clean_mime_database}
%clean_icon_cache hicolor

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
