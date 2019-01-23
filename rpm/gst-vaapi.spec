Name:           gstreamer-vaapi
Version:        1.14.4
Release:        1%{?dist}
Summary:        GStreamer plugins to use VA API video acceleration

License:        LGPLv2+
URL:            https://cgit.freedesktop.org/gstreamer/gstreamer-vaapi
Source0:        https://gstreamer.freedesktop.org/src/gstreamer-vaapi/gstreamer-vaapi-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  glib2-devel >= 2.32
BuildRequires:  gstreamer1.0-devel >= 1.4.0
BuildRequires:  gstreamer1.0-plugins-base-devel >= 1.4.0
BuildRequires:  gstreamer1.0-plugins-bad-devel >= 1.4.0
BuildRequires:  libva-devel >= 1.1.0
BuildRequires:  libdrm-devel
BuildRequires:  libudev-devel
#BuildRequires:  libGL-devel
BuildRequires:  pkgconfig(egl)
BuildRequires:  libvpx-devel
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(wayland-client)  >= 1
BuildRequires:  pkgconfig(wayland-scanner) >= 1
BuildRequires:  pkgconfig(wayland-cursor)  >= 1
BuildRequires:  pkgconfig(wayland-egl)     >= 1
BuildRequires:  pkgconfig(wayland-server)  >= 1

%description
A collection of GStreamer plugins to let you make use of VA API video
acceleration from GStreamer applications.

Includes elements for video decoding, display, encoding and post-processing
using VA API (subject to hardware limitations).

%package        devel-docs
Summary:        Developer documentation for GStreamer VA API video acceleration plugins
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

Provides:       gstreamer1-vaapi-devel = %{version}-%{release}

%description	devel-docs
The %{name}-devel-docs package contains developer documentation
for the GStreamer VA API video acceleration plugins

%prep
%setup -q -n %{name}-%{version}/%{name}

%build

./autogen.sh --disable-silent-rules --disable-fatal-warnings \
           --enable-static=no \
           --disable-builtin-libvpx

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%check
%__make check

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README
%license COPYING.LIB
%{_libdir}/gstreamer-1.0/*.so

%files devel-docs
%doc AUTHORS NEWS README
%doc %{_datadir}/gtk-doc

