Summary:	A Image viewer based on X-Window system and GTK+
Summary(es):	Un visualizador de imágenes basado en X Window y GTK+
Summary(pl):	Przegl±darka plików graficznych oparta na bibliotece GTK+
Summary(pt_BR):	Um visualizador de imagens baseado no X Window e GTK+
Name:		gtksee
Version:	0.5.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://download.berlios.de/gtksee/%{name}-%{version}.tar.gz
# Source0-md5:	a5012896f86dde9fc90be71a413e7326
Source1:	%{name}.desktop
Source2:	%{name}.png
Icon:		gtksee.xpm
URL:		http://www.zg169.net/~hotaru/gtksee/index_en.html
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A Image viewer based on X-Window system and GTK+. The main purpose is
to port ACD See, which is a very popular image viewer in M$ world, to
Unix platform.

%description -l es
El visor de imágenes permite visualizar y manejar una variedad de
formatos de imágenes. Pretendes tener las mismas funciones del ACD
See, que es mucho popular.

%description -l pl
Gtksee to przegl±darka plików graficznych dzia³aj±ca pod X Window
System i korzystaj±ca z biblioteki GTK+. Ma jak najbardziej
przypominaæ znan± ze ¶wiata MS Windows przegl±darkê ACD See.

%description -l pt_BR
Um visualizador de imagens baseado no X Window e GTK+. Pretende ter as
mesmas funcionalidades do ACD See, que é bastante popular no mundo
Microsoft(r).

%prep
%setup -q

%build
rm -rf missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
	CPPFLAGS="`pkg-config libpng12 --cflags`"
fi
%configure CPPFLAGS="$CPPFLAGS"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Graphics/Viewers,%{_datadir}/pixmaps}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps


%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gtksee
%{_pixmapsdir}/*
%{_applnkdir}/Graphics/Viewers/gtksee.desktop
