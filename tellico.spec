#
# Conditional build:
%bcond_with	webcam	# build with webcam barcode recognition
#
%define		qt_ver	5.4.0
Summary:	A collection manager
Summary(pl.UTF-8):	Zarządca zbiorów wideo, audio i książek
Name:		tellico
Version:	3.1.1
Release:	2
License:	GPL v3
Group:		X11/Applications
Source0:	http://tellico-project.org/files/%{name}-%{version}.tar.xz
# Source0-md5:	8c503a21b12d5bfc62f55b287855fa6e
URL:		http://tellico-project.org/
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5DBus-devel >= %{qt_ver}
BuildRequires:	Qt5Network-devel >= %{qt_ver}
BuildRequires:	Qt5Test-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	Qt5Xml-devel >= %{qt_ver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	exempi-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.19
BuildRequires:	kf5-karchive-devel
BuildRequires:	kf5-kcodecs-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kguiaddons-devel
BuildRequires:	kf5-khtml-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kitemmodels-devel
BuildRequires:	kf5-kjobwidgets-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-solid-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.19
BuildRequires:	poppler-qt5-devel
BuildRequires:	qimageblitz-devel
BuildRequires:	qjson-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	shared-desktop-ontologies-devel
BuildRequires:	soprano-devel
BuildRequires:	taglib-devel
BuildRequires:	yaz-devel
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5DBus >= %{qt_ver}
Requires:	Qt5Network >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	Qt5Xml >= %{qt_ver}
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

%build
%cmake . \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	%{cmake_on_off webcam ENABLE_WEBCAM}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

rm -r $RPM_BUILD_ROOT%{_docdir}

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
/etc/xdg/tellicorc
/etc/xdg/tellico-script.knsrc
/etc/xdg/tellico-template.knsrc
%{_datadir}/kconf_update/%{name}-rename.upd
%{_datadir}/kconf_update/tellico.upd
%{_datadir}/kconf_update/tellico-1-3-update.pl
%{_datadir}/%{name}
%{_datadir}/config.kcfg/tellico_config.kcfg
%{_datadir}/mime/packages/*.xml
%{_datadir}/kxmlgui5/tellico
%{_datadir}/metainfo/org.kde.tellico.appdata.xml
%{_desktopdir}/org.kde.tellico.desktop
%{_iconsdir}/*/*/*/*.png
