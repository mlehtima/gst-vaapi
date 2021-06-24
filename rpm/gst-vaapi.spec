%define majorminor   1.0
%define gstreamer    gstreamer

Name     : %{gstreamer}%{majorminor}-vaapi
Version  : 1.16.1
Release  : 1
URL      : https://cgit.freedesktop.org/gstreamer/gstreamer-vaapi
Source0  : %{name}-%{version}.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1

%define sonamever %(echo %{version} | cut -d '+' -f 1)

BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-devel
BuildRequires : pkgconfig(gstreamer-plugins-base-1.0) >= %{sonamever}
BuildRequires : pkgconfig(gstreamer-plugins-bad-1.0) >= %{sonamever}
BuildRequires : pkgconfig(gstreamer-1.0) >= %{sonamever}
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(glesv2)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libva-drm)
BuildRequires : pkgconfig(libva-wayland)
BuildRequires : pkgconfig(wayland-client)

%description
gstreamer-vaapi
VA-API support to GStreamer
License
-------
gstreamer-vaapi helper libraries and plugin elements are available
under the terms of the GNU Lesser General Public License v2.1+

%prep
%setup -q -n %{name}-%{version}/gstreamer-vaapi

%build
NOCONFIGURE=1 ./autogen.sh
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547489839
%configure --disable-static --prefix=%_prefix --sysconfdir=%{_sysconfdir} \
	--enable-x11=no --enable-egl=no --enable-glx=no --with-gtk=no \
	--enable-wayland=yes --enable-drm=yes
make %{?jobs:-j%jobs}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1547489839
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gstreamer-vaapi
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/gstreamer-vaapi/COPYING.LIB
%make_install

%files
%defattr(-,root,root,-)
%{_libdir}/gstreamer-1.0/libgstvaapi.so
%{_datadir}/package-licenses/gstreamer-vaapi/COPYING.LIB
