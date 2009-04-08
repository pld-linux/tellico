# TODO
# - mimelnk/x-tellico.desktop is handled how in kde4?
# - not found:
#   poppler-qt4.pc
#   KSaneConfig.cmake
#   ksane-config.cmake
#-----------------------------------------------------------------------------
#-- The following OPTIONAL packages could NOT be located on your system.
#-- Consider installing them to enable more features from this software.
#+ libpoppler: Support for reading PDF files <http://poppler.freedesktop.org/>
#+ libksane, 4.2.0 or higher: Support for scanning images <http://www.kde.org/>

#
# Conditional build:
%bcond_with	webcam	# build with webcam barcode recognition
#
%define		svn	950843
Summary:	A collection manager
Summary(pl.UTF-8):	Zarządca zbiorów wideo, audio i książek
Name:		tellico
Version:	2.0
Release:	0.%{svn}.1
License:	GPL v2
Group:		X11/Applications
# svn co svn://anonsvn.kde.org/home/kde/trunk/playground/office/tellico
# tar --exclude=.svn -cjf tellico.tar.bz2 tellico/
Source0:	%{name}.tar.bz2
# Source0-md5:	c2ccd790c5c2110d3a1dadf1c858c1b1
#Patch0: %{name}-u64.patch
#Patch1: %{name}-desktop.patch
URL:		http://www.periapsis.org/tellico/
BuildRequires:	QtSvg-devel
BuildRequires:	QtTest-devel
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	exempi-devel
BuildRequires:	kde4-kdemultimedia-devel
BuildRequires:	kde4-kdepimlibs-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.19
BuildRequires:	phonon-devel
BuildRequires:	poppler-qt-devel
BuildRequires:	qimageblitz-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	taglib-devel
BuildRequires:	yaz-devel
Requires:	desktop-file-utils
Requires:	libxslt >= 1.0.19
Obsoletes:	bookcase
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tellico is a personal catalog application for your book, video and
audio collection.

%description -l pl.UTF-8
Tellico to osobista aplikacja katalogowa przeznaczona do
księgozbiorów, archiwów wideo i audio.

%prep
%setup -q -n %{name}
#%patch0 -p1
#%patch1 -p1

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_mime_database

%postun
%update_desktop_database_postun
%update_mime_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
#%{_datadir}/mimelnk/application/x-%{name}.desktop
%{_datadir}/config/tellico-script.knsrc
%{_datadir}/config/tellico-template.knsrc
%{_datadir}/apps/kconf_update/%{name}-rename.upd
%{_datadir}/apps/kconf_update/tellico.upd
%{_datadir}/apps/kconf_update/tellico-1-3-update.pl
%{_datadir}/apps/%{name}
%{_datadir}/config/tellicorc
%{_datadir}/config.kcfg/tellico_config.kcfg
%{_datadir}/mime/packages/*.xml
%{_desktopdir}/kde4/%{name}.desktop
%{_iconsdir}/*/*/*/*.png
