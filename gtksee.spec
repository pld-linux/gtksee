Summary:	An Image viewer based on X-Window system and GTK+
Summary(es.UTF-8):	Un visualizador de imágenes basado en X Window y GTK+
Summary(pl.UTF-8):	Przeglądarka plików graficznych oparta na bibliotece GTK+
Summary(pt_BR.UTF-8):	Um visualizador de imagens baseado no X Window e GTK+
Name:		gtksee
Version:	0.5.6
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
#Source0Download: http://developer.berlios.de/project/showfiles.php?group_id=735
Source0:	http://download.berlios.de/gtksee/%{name}-%{version}.tar.gz
# Source0-md5:	1f5a43a869938c7a2bef1276203dfdc5
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-localenames.patch
URL:		http://gtksee.berlios.de/index.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An Image viewer based on X-Window system and GTK+. The main purpose is
to port ACD See, which is a very popular image viewer in M$ world, to
Unix platform.

%description -l es.UTF-8
El visor de imágenes permite visualizar y manejar una variedad de
formatos de imágenes. Pretendes tener las mismas funciones del ACD
See, que es mucho popular.

%description -l pl.UTF-8
Gtksee to przeglądarka plików graficznych działająca pod X Window
System i korzystająca z biblioteki GTK+. Ma jak najbardziej
przypominać znaną ze świata MS Windows przeglądarkę ACD See.

%description -l pt_BR.UTF-8
Um visualizador de imagens baseado no X Window e GTK+. Pretende ter as
mesmas funcionalidades do ACD See, que é bastante popular no mundo
Microsoft(r).

%prep
%setup -q
%patch0 -p1

# it's encoded in gb2312
mv -f po/{zh_CN.EUC,zh_CN}.po
# it's Ukrainian, not Russian
mv -f po/{ru_UA,uk}.po

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gtksee
%{_pixmapsdir}/*.png
%{_desktopdir}/gtksee.desktop
