Summary:	A collection manager
Summary(pl):	Zarz±dca zbiorów wideo, audio i ksi±¿ek
Name:		bookcase
Version:	0.9.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.periapsis.org/bookcase/download/%{name}-%{version}.tar.gz
# Source0-md5:	ccb7035054fbbba18f47c24929881205
Patch0:		%{name}-gcc34.patch
URL:		http://www.periapsis.org/bookcase/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	libgcrypt-devel
BuildRequires:	libxslt-devel >= 1.0.19
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	qt-devel > 3.1
BuildRequires:	pcre-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040805-1
Requires:	kdebase-core >= 3.1
Requires:	libxslt >= 1.0.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bookcase is a personal catalog application for your book, video and
audio collection.

%description -l pl
Bookcase to osobista aplikacja katalogowa przeznaczona do
ksiêgozbiorów, archiwów wideo i audio.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

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

%files -f bookcase.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mimelnk/application/x-bookcase.desktop
%{_iconsdir}/*/*/*/bookcase.png
%{_datadir}/apps/%{name}
%{_desktopdir}/bookcase.desktop
