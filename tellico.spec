Summary:	A book collection manager
Summary(pl):	Maned¿er ksiêgozbiorów
Name:		bookcase
Version:	0.5.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.periapsis.org/bookcase/
Requires:	kdebase >= 3.0
Requires:	libxslt >= 1.0.19
BuildRequires:	qt-devel > 3.0 
BuildRequires:	kdelibs-devel  >= 3.0
BuildRequires:	libxslt-devel >= 1.0.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

%description
Bookcase is a personal catalog application for your book collection.

%description -l pl

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure --enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang      bookcase        --with-kde

%files -f bookcase.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL README TODO
%attr(755,root,root) %{_bindir}/*
#%{_mandir}/man1/*
#%{_datadir}/applnk/Applications/bookcase.desktop
%{_datadir}/mimelnk/application/x-bookcase.desktop
%{_datadir}/pixmaps/*/*/*/bookcase.png
%{_datadir}/apps/%{name}

%{_applnkdir}/Applications/bookcase.desktop


%clean
rm -rf $RPM_BUILD_ROOT
