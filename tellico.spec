Summary:	A collection manager
Summary(pl):	Zarz±dca zbiorów wideo, audio i ksi±¿ek
Name:		tellico
Version:	1.1.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.periapsis.org/tellico/download/%{name}-%{version}.tar.gz
# Source0-md5:	f2ca0b4d63463327e74d2330d392aec2
URL:		http://www.periapsis.org/tellico/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.2
BuildRequires:	kdemultimedia-devel
BuildRequires:	kdepim-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.19
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	taglib-devel
BuildRequires:	yaz-devel
Requires:	kdebase-core >= 3.2
Requires:	libxslt >= 1.0.19
Obsoletes:	bookcase
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bookcase is a personal catalog application for your book, video and
audio collection.

%description -l pl
Bookcase to osobista aplikacja katalogowa przeznaczona do
ksiêgozbiorów, archiwów wideo i audio.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
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
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mimelnk/application/x-%{name}.desktop
%{_datadir}/apps/kconf_update/%{name}-rename.upd
%{_datadir}/apps/kconf_update/tellico.upd
%{_iconsdir}/*/*/*/%{name}.png
%{_datadir}/apps/%{name}
%{_desktopdir}/kde/%{name}.desktop
