Summary:	A collection manager
Summary(pl):	Zarz±dca zbiorów wideo, audio i ksi±¿ek
Name:		tellico
Version:	1.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.periapsis.org/bookcase/download/%{name}-%{version}.tar.gz
# Source0-md5:	40510766a67c90064d74e452092983d8
URL:		http://www.periapsis.org/bookcase/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.2
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.19
BuildRequires:	pcre-devel
BuildRequires:	qt-devel > 3.1
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	kdebase-core >= 3.1
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

%configure \
	--enable-final \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT *.lang
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%find_lang %{name}  --with-kde
mv -f $RPM_BUILD_ROOT{%{_datadir}/applnk/*/*.desktop,%{_desktopdir}}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mimelnk/application/x-%{name}.desktop
%{_datadir}/apps/kconf_update/%{name}-rename.upd
%{_datadir}/apps/kconf_update/tellico.upd
%{_iconsdir}/*/*/*/%{name}.png
%{_datadir}/apps/%{name}
%{_desktopdir}/%{name}.desktop
