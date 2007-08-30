%define name lmms
%define version 0.2.1
%define release %mkrel 2
%define __libtoolize /bin/true
%define __cputoolize /bin/true


Name:      %{name}
Version:   %{version}
Release:   %{release}
Summary:   FruityLoops clone for linux
License:   GPL
URL:       http://lmms.sourceforge.net/
Group:     Sound
Source:    http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Source10:  %{name}-16.png
Source11:  %{name}-32.png
Source12:  %{name}-48.png
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: kdelibs-devel >= 3.2
BuildRequires: libSDL-devel libalsa-devel libjack-devel
Buildrequires: libsamplerate-devel libvorbis-devel


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
%build

perl -pi -e 's/\$QTDIR\/lib/\$QTDIR\/%{_lib}/' configure
%configure
%make

%install
rm -rf %buildroot
%{makeinstall_std}


#menus
install -d %buildroot/%{_menudir}
cat <<EOF >%buildroot/%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/%{name}" \
                  icon=%{name}.png \
                  needs="x11" \
                  section="Multimedia/Sound" \
                  title="Lmms" \
                  longtitle="FruityLoops clone for linux" \
		  xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Lmms
Comment=FruityLoops clone for linux
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;Audio;Midi;Mixer;Sequencer;Recorder;KDE;
EOF


install -m644 %{SOURCE10} -D %buildroot/%{_miconsdir}/%{name}.png
install -m644 %{SOURCE11} -D %buildroot/%{_iconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %buildroot/%{_liconsdir}/%{name}.png
rm -f %buildroot/%{_libdir}/%{name}/*.a

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%doc README COPYING TODO
%attr(0755,root,root) %_bindir/%{name}
%_menudir/%{name}
%_iconsdir/%{name}.png
%_liconsdir/%{name}.png
%_miconsdir/%{name}.png
%_datadir/%{name}
%_libdir/%{name}
%_mandir/man?/*
%{_datadir}/applications/*.desktop

%post
%{update_menus}

%postun
%{clean_menus}


