%define majorminor   1.0
%define gstreamer    gstreamer

Name     : %{gstreamer}%{majorminor}-vaapi
Version  : 1.18.5
Release  : 1
URL      : https://cgit.freedesktop.org/gstreamer/gstreamer-vaapi
Source0  : %{name}-%{version}.tar.xz
Summary  : No detailed summary available
License  : LGPLv2+

%define sonamever %(echo %{version} | cut -d '+' -f 1)

BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-devel
BuildRequires : meson
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

%prep
%autosetup -n %{name}-%{version}/gstreamer-vaapi

%build
%meson \
  -Dpackage-origin='http://sailfishos.org/' \
  -Ddoc=disabled \
  -Dexamples=disabled \
  -Dtests=disabled \
  -Dwith_drm=yes \
  -Dwith_egl=no \
  -Dwith_glx=no \
  -Dwith_egl=no \
  -Dwith_wayland=yes \
  -Dwith_x11=no

%meson_build

%install
%meson_install

%files
%defattr(-,root,root,-)
%license COPYING.LIB
%{_libdir}/gstreamer-1.0/libgstvaapi.so
