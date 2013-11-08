#
# Conditional build:
%bcond_with	webcam	# build with webcam barcode recognition
#
Summary:	A collection manager
Summary(pl.UTF-8):	Zarządca zbiorów wideo, audio i książek
Name:		tellico
Version:	2.3.8
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://tellico-project.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	3f85002f6f369bdcf72ac7499d39297a
Patch1:		%{name}-desktop.patch
Patch2:		libkcddb.patch
URL:		http://tellico-project.org/
BuildRequires:	cmake
BuildRequires:	exempi-devel
BuildRequires:	kde4-kdepimlibs-devel
BuildRequires:	kde4-libksane-devel
BuildRequires:	kde4-libkcddb-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.19
BuildRequires:	poppler-Qt-devel
BuildRequires:	qimageblitz-devel
BuildRequires:	qjson-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	shared-desktop-ontologies-devel
BuildRequires:	soprano-devel
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
%setup -q
%patch1 -p1
%patch2 -p1

%build
%cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}
exit
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT/nogo

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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/kconf_update/%{name}-rename.upd
%{_datadir}/apps/kconf_update/tellico.upd
%{_datadir}/apps/kconf_update/tellico-1-3-update.pl
%{_datadir}/apps/%{name}
%{_datadir}/config/tellicorc
%{_datadir}/config/tellico-script.knsrc
%{_datadir}/config/tellico-template.knsrc
%{_datadir}/config.kcfg/tellico_config.kcfg
%{_datadir}/mime/packages/*.xml
%{_desktopdir}/kde4/%{name}.desktop
%{_iconsdir}/*/*/*/*.png
