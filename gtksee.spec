%define name gtksee
%define version 0.3.0
%define release 2cl

Summary: A Image viewer based on X-Window system and GTK+.
Summary(pt_BR): Um visualizador de imagens baseado no X Window e GTK+.
Summary(es): Un visualizador de imágenes basado en X Window y GTK+.
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL2
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
URL: http://www.zg169.net/~hotaru/gtksee/index_en.html
Source: %{name}-%{version}.tar.gz
Source2:gtksee.po
Source800: gtksee-wmconfig.i18n.tgz
patch0:gtksee.inter.patch
BuildRoot: /tmp/%{name}-%{version}

%description
A Image viewer based on X-Window system and GTK+.
The main purpose is to port ACD See, which is a very popular
image viewer in M$ world, to Unix platform. 

%description -l pt_BR
Um visualizador de imagens baseado no X Window e GTK+.
Pretende ter as mesmas funcionalidades do ACD See, que é bastante
popular no mundo Microsoft(r).

%description -l es
El visor de imágenes permite visualizar y manejar una variedad de
formatos de imágenes. Pretendes tener las mismas funciones del ACD
See, que es mucho popular.

%prep

%setup -q
%patch0 -p1


%build
CFLAGS=$RPM_OPT_FLAGS \
./configure --prefix=/usr

make CC=gcc

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT ; fi
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
mkdir -p $RPM_BUILD_ROOT/usr/{bin,share/{pixmaps,apps/Graphics}}

make prefix=$RPM_BUILD_ROOT/usr install-strip

install -m 644 icons/gtksee.xpm $RPM_BUILD_ROOT/usr/share/pixmaps

cat > $RPM_BUILD_ROOT/usr/share/apps/Graphics/gtksee.desktop <<EOF
[Desktop Entry]
Name=GtkSee
Comment=Image Viewer
Exec=gtksee
Icon=gtksee.xpm
Terminal=0
Type=Application
EOF


mkdir -p $RPM_BUILD_ROOT/usr/share/locale/pt_BR/LC_MESSAGES
msgfmt -o $RPM_BUILD_ROOT/usr/share/locale/pt_BR/LC_MESSAGES/gtksee.mo $RPM_SOURCE_DIR/gtksee.po  





tar xvfpz $RPM_SOURCE_DIR/gtksee-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO icons
/usr/bin/gtksee
/etc/X11/wmconfig/gtksee
/usr/share/pixmaps/gtksee.xpm
/usr/share/apps/Graphics/gtksee.desktop
/usr/share/locale/pt_BR/LC_MESSAGES/gtksee.mo


%changelog

* Fri Feb 04 2000 Francisco Ganacim (Conectiva) <francisco@conectiva.com>
- Internacionalization 
- pt_BR potfile added 

* Mon Aug 30 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- updated to 0.3.0

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 17 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Feb 22 1999 Ryan Weaver <ryanw@infohwy.com>
  [gtksee-0.2.2-1]
- 0.2.2  (1999/02/20)
- Image Viewer:
  o New short-cut keys: Spacebar, Arrow-keys
- Other:
  o Compiled successfully under gtk+-1.1.15
  o New command-line options and parameters:
    gtksee [-R[directory]] [-fis] [files...]
  o Some new icons. See icons/README.icons
  o Bzip2 patch applied.
    (From: Roman Belenov <roman@nstl.nnov.ru>)
- Bug-fixed:
  o Checks for os2.h and -lsocket
    (Asbjoern Pettersen <ape@spacetec.no>'s hints)

* Thu Dec  7 1998 Ryan Weaver <ryanw@infohwy.com>
  [gtksee-0.2.1-3]
- Added patch to allow it to compile under gtk+-1.1.5
  and glib-1.1.5

* Thu Dec  7 1998 Ryan Weaver <ryanw@infohwy.com>
  [gtksee-0.2.1-2]
- Added the bzip2 support patch from gtksee homepage.

* Thu Dec  3 1998 Ryan Weaver <ryanw@infohwy.com>
  [gtksee-0.2.1-1]
- 0.2.1  (1998/12/03)
- Image Browser:
	o Thumbnails cache
	o Tooltips for thumbnails mode and small icons mode
	o New feature: Quick-refresh, Auto-refresh
	o About dialog's look and feel; Help menus
- Image Viewer:
	o Full-screen mode, and a popup-menu for it
	o Double-click on the image to return to browse mode
- Other:
	o configure: new option: --with-im-incs, --with-im-libs
- Fixed bugs:
	o Auto-update preview box when size changed
	o Seg-faults on some bmp and gif files (Thanks BaZe for giving
	  me such a funny bmp :) )
	o Screen shrinking problem (preview box and thumbnails list)
	o Pyun YongHyeon's patch(im_xcf.c): compiled under FreeBSD 3.0
	o Maybe more :)

* Tue Nov 24 1998 Ryan Weaver <ryanw@infohwy.com>
  [gtksee-0.2.0-2]
- Split into 2 packages. 1 statically linked and one dynamically
  linked.
- Including the gtksee.xpm resized to 48x48
- Added a wmconfig file and a gtksee.desktop file
- In static package, %post install to link gtksee-static to gtksee
  and %preun to rm the link if it's there.

* Tue Nov 24 1998 Ryan Weaver <ryanw@infohwy.com>
  [gtksee-0.2.0-1]
- 0.2.0  (1998/11/22)
- Image Browser:
	o Show/Hide non-images
	o Fast preview option. If you haven't upgraded your CPU to
	  PII, you will probably love this. :)
	o Thumbnails list. Cool feature.
	o Small icon list. M$-explorer-like.
- Image Viewer:
	o Support Drag-N-Drop (instead of scrolled window)
	o Support short-cut keys (Home, End, PgUp, PgDn, Esc)
	o Slideshow
- Other:
	o Support bitmap(1BPS) format PSD image
	o configure: detect libtiff34
	o Auto-detect supported image formats, without depending on
	  filename extensions.
	o xpm files have been move to src/pixmap
- And always some bug-fixed.
