Summary:	A collection manager
Summary(pl.UTF-8):   Zarządca zbiorów wideo, audio i książek
Name:		tellico
Version:	1.2.8
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.periapsis.org/tellico/download/%{name}-%{version}.tar.gz
# Source0-md5:	ac9be76e26edaf9f75cddb03ee4ed73b
URL:		http://www.periapsis.org/tellico/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.3.1
BuildRequires:	kdemultimedia-devel
BuildRequires:	kdepim-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.19
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	taglib-devel
BuildRequires:	yaz-devel
Requires:	desktop-file-utils
Requires:	kdebase-core >= 9:3.3.1
Requires:	libxslt >= 1.0.19
Obsoletes:	bookcase
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bookcase is a personal catalog application for your book, video and
audio collection.

%description -l pl.UTF-8
Bookcase to osobista aplikacja katalogowa przeznaczona do
księgozbiorów, archiwów wideo i audio.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%{__perl} admin/am_edit
%configure \
	--enable-final \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mimelnk/application/x-%{name}.desktop
%{_datadir}/apps/kconf_update/%{name}-rename.upd
%{_datadir}/apps/kconf_update/tellico.upd
%{_datadir}/apps/%{name}
%{_datadir}/config.kcfg/tellico_config.kcfg
%{_desktopdir}/kde/%{name}.desktop
%{_iconsdir}/*/*/*/%{name}.png
