%define majorminor 1.0
%define gstreamer  gstreamer

%global _vpath_srcdir subprojects/gstreamer-vaapi
%global _vpath_builddir subprojects/gstreamer-vaapi/_build

Name:		%{gstreamer}%{majorminor}-vaapi
Version:	1.22.10
Release:	1
Summary:	No detailed summary available
License:	LGPLv2+
URL:		http://gstreamer.freedesktop.org/src/gstreamer
Source0:	%{name}-%{version}.tar.xz

%define sonamever %(echo %{version} | cut -d '+' -f 1)

BuildRequires: gobject-introspection
BuildRequires: gobject-introspection-devel
BuildRequires: meson
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0) >= %{sonamever}
BuildRequires: pkgconfig(gstreamer-plugins-bad-1.0) >= %{sonamever}
BuildRequires: pkgconfig(gstreamer-1.0) >= %{sonamever}
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libva)
BuildRequires: pkgconfig(libva-drm)
BuildRequires: pkgconfig(libva-wayland)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)

%description
gstreamer-vaapi
VA-API support to GStreamer

%prep
%autosetup -n %{name}-%{version}/gstreamer

%build
%meson \
  -Dpackage-origin='http://sailfishos.org/' \
  -Ddoc=disabled \
  -Dexamples=disabled \
  -Dtests=disabled \
  -Ddrm=enabled \
  -Degl=disabled \
  -Dglx=disabled \
  -Dwayland=enabled \
  -Dx11=disabled

%meson_build

%install
%meson_install

%files
%license subprojects/gstreamer-vaapi/COPYING.LIB
%{_libdir}/gstreamer-1.0/libgstvaapi.so
