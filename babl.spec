#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : babl
Version  : 0.1.66
Release  : 29
URL      : https://download.gimp.org/pub/babl/0.1/babl-0.1.66.tar.bz2
Source0  : https://download.gimp.org/pub/babl/0.1/babl-0.1.66.tar.bz2
Summary  : Dynamic, any to any, pixel format conversion library
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: babl-lib = %{version}-%{release}
Requires: babl-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : librsvg
BuildRequires : librsvg-dev
BuildRequires : pkgconfig(lcms2)

%description
Babl-0.1.66
Contents
â¢ Babl
â¢   Features
â¢ Download
â¢ Documentation
â¢   Usage
â¢   Vocabulary
â¢   Environment
â¢   Extending
â¢   Directory Overview
â¢ Todo
â¢   Authors

%package dev
Summary: dev components for the babl package.
Group: Development
Requires: babl-lib = %{version}-%{release}
Provides: babl-devel = %{version}-%{release}
Requires: babl = %{version}-%{release}
Requires: babl = %{version}-%{release}

%description dev
dev components for the babl package.


%package lib
Summary: lib components for the babl package.
Group: Libraries
Requires: babl-license = %{version}-%{release}

%description lib
lib components for the babl package.


%package license
Summary: license components for the babl package.
Group: Default

%description license
license components for the babl package.


%prep
%setup -q -n babl-0.1.66
pushd ..
cp -a babl-0.1.66 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1560383049
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffast-math -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-vectorize "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffast-math -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-vectorize "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffast-math -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-vectorize "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffast-math -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-vectorize "
%configure --disable-static --enable-sse4_1
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static --enable-sse4_1
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :
cd ../buildavx2;
make VERBOSE=1 V=1 %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1560383049
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/babl
cp COPYING %{buildroot}/usr/share/package-licenses/babl/COPYING
cp docs/COPYING %{buildroot}/usr/share/package-licenses/babl/docs_COPYING
cp docs/COPYING.LESSER %{buildroot}/usr/share/package-licenses/babl/docs_COPYING.LESSER
pushd ../buildavx2/
%make_install_avx2
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/babl-0.1/babl/babl-introspect.h
/usr/include/babl-0.1/babl/babl-macros.h
/usr/include/babl-0.1/babl/babl-types.h
/usr/include/babl-0.1/babl/babl-version.h
/usr/include/babl-0.1/babl/babl.h
/usr/lib64/haswell/libbabl-0.1.so
/usr/lib64/libbabl-0.1.so
/usr/lib64/pkgconfig/babl.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/babl-0.1/CIE.so
/usr/lib64/babl-0.1/HCY.so
/usr/lib64/babl-0.1/HSL.so
/usr/lib64/babl-0.1/HSV.so
/usr/lib64/babl-0.1/cairo.so
/usr/lib64/babl-0.1/double.so
/usr/lib64/babl-0.1/fast-float.so
/usr/lib64/babl-0.1/float.so
/usr/lib64/babl-0.1/gegl-fixups.so
/usr/lib64/babl-0.1/gggl-lies.so
/usr/lib64/babl-0.1/gggl-table-lies.so
/usr/lib64/babl-0.1/gggl-table.so
/usr/lib64/babl-0.1/gggl.so
/usr/lib64/babl-0.1/gimp-8bit.so
/usr/lib64/babl-0.1/grey.so
/usr/lib64/babl-0.1/half.so
/usr/lib64/babl-0.1/haswell/CIE.so
/usr/lib64/babl-0.1/haswell/HCY.so
/usr/lib64/babl-0.1/haswell/HSL.so
/usr/lib64/babl-0.1/haswell/HSV.so
/usr/lib64/babl-0.1/haswell/cairo.so
/usr/lib64/babl-0.1/haswell/double.so
/usr/lib64/babl-0.1/haswell/fast-float.so
/usr/lib64/babl-0.1/haswell/float.so
/usr/lib64/babl-0.1/haswell/gegl-fixups.so
/usr/lib64/babl-0.1/haswell/gggl-lies.so
/usr/lib64/babl-0.1/haswell/gggl-table-lies.so
/usr/lib64/babl-0.1/haswell/gggl-table.so
/usr/lib64/babl-0.1/haswell/gggl.so
/usr/lib64/babl-0.1/haswell/gimp-8bit.so
/usr/lib64/babl-0.1/haswell/grey.so
/usr/lib64/babl-0.1/haswell/half.so
/usr/lib64/babl-0.1/haswell/naive-CMYK.so
/usr/lib64/babl-0.1/haswell/simple.so
/usr/lib64/babl-0.1/haswell/sse-half.so
/usr/lib64/babl-0.1/haswell/sse2-float.so
/usr/lib64/babl-0.1/haswell/sse2-int16.so
/usr/lib64/babl-0.1/haswell/sse2-int8.so
/usr/lib64/babl-0.1/haswell/sse4-int8.so
/usr/lib64/babl-0.1/haswell/two-table.so
/usr/lib64/babl-0.1/haswell/u16.so
/usr/lib64/babl-0.1/haswell/u32.so
/usr/lib64/babl-0.1/haswell/ycbcr.so
/usr/lib64/babl-0.1/naive-CMYK.so
/usr/lib64/babl-0.1/simple.so
/usr/lib64/babl-0.1/sse-half.so
/usr/lib64/babl-0.1/sse2-float.so
/usr/lib64/babl-0.1/sse2-int16.so
/usr/lib64/babl-0.1/sse2-int8.so
/usr/lib64/babl-0.1/sse4-int8.so
/usr/lib64/babl-0.1/two-table.so
/usr/lib64/babl-0.1/u16.so
/usr/lib64/babl-0.1/u32.so
/usr/lib64/babl-0.1/ycbcr.so
/usr/lib64/haswell/libbabl-0.1.so.0
/usr/lib64/haswell/libbabl-0.1.so.0.165.1
/usr/lib64/libbabl-0.1.so.0
/usr/lib64/libbabl-0.1.so.0.165.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/babl/COPYING
/usr/share/package-licenses/babl/docs_COPYING
/usr/share/package-licenses/babl/docs_COPYING.LESSER
