#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : babl
Version  : 0.1.30
Release  : 9
URL      : https://download.gimp.org/pub/babl/0.1/babl-0.1.30.tar.bz2
Source0  : https://download.gimp.org/pub/babl/0.1/babl-0.1.30.tar.bz2
Summary  : Dynamic, any to any, pixel format conversion library
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: babl-lib
BuildRequires : librsvg
BuildRequires : librsvg-dev

%description
Babl-0.1.30
Contents
â¢ Babl
â¢   Features
â¢ Download
â¢ Documentation
â¢   Usage
â¢   Vocabulary
â¢   Shortcut Coverage
â¢   Environment
â¢   Extending
â¢   Directory Overview
â¢ Todo
â¢   Authors

%package dev
Summary: dev components for the babl package.
Group: Development
Requires: babl-lib
Provides: babl-devel

%description dev
dev components for the babl package.


%package lib
Summary: lib components for the babl package.
Group: Libraries

%description lib
lib components for the babl package.


%prep
%setup -q -n babl-0.1.30
pushd ..
cp -a babl-0.1.30 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506290355
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffast-math -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-vectorize "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffast-math -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-vectorize "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffast-math -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-vectorize "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffast-math -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-vectorize "
%configure --disable-static --enable-sse4_1
make V=1  %{?_smp_mflags}

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static --enable-sse4_1   --libdir=/usr/lib64/haswell --bindir=/usr/bin/haswell
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1506290355
rm -rf %{buildroot}
pushd ../buildavx2/
%make_install
popd
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/haswell/pkgconfig/babl.pc

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
/usr/lib64/babl-0.1/16bit.so
/usr/lib64/babl-0.1/CIE.so
/usr/lib64/babl-0.1/HCY.so
/usr/lib64/babl-0.1/HSL.so
/usr/lib64/babl-0.1/HSV.so
/usr/lib64/babl-0.1/cairo.so
/usr/lib64/babl-0.1/fast-float.so
/usr/lib64/babl-0.1/float-half.so
/usr/lib64/babl-0.1/float.so
/usr/lib64/babl-0.1/gegl-fixups.so
/usr/lib64/babl-0.1/gggl-lies.so
/usr/lib64/babl-0.1/gggl-table-lies.so
/usr/lib64/babl-0.1/gggl-table.so
/usr/lib64/babl-0.1/gggl.so
/usr/lib64/babl-0.1/gimp-8bit.so
/usr/lib64/babl-0.1/grey.so
/usr/lib64/babl-0.1/naive-CMYK.so
/usr/lib64/babl-0.1/simple.so
/usr/lib64/babl-0.1/sse-half.so
/usr/lib64/babl-0.1/sse2-float.so
/usr/lib64/babl-0.1/sse2-int16.so
/usr/lib64/babl-0.1/sse2-int8.so
/usr/lib64/babl-0.1/sse4-int8.so
/usr/lib64/babl-0.1/two-table.so
/usr/lib64/babl-0.1/ycbcr.so
/usr/lib64/haswell/babl-0.1/16bit.so
/usr/lib64/haswell/babl-0.1/CIE.so
/usr/lib64/haswell/babl-0.1/HCY.so
/usr/lib64/haswell/babl-0.1/HSL.so
/usr/lib64/haswell/babl-0.1/HSV.so
/usr/lib64/haswell/babl-0.1/cairo.so
/usr/lib64/haswell/babl-0.1/fast-float.so
/usr/lib64/haswell/babl-0.1/float-half.so
/usr/lib64/haswell/babl-0.1/float.so
/usr/lib64/haswell/babl-0.1/gegl-fixups.so
/usr/lib64/haswell/babl-0.1/gggl-lies.so
/usr/lib64/haswell/babl-0.1/gggl-table-lies.so
/usr/lib64/haswell/babl-0.1/gggl-table.so
/usr/lib64/haswell/babl-0.1/gggl.so
/usr/lib64/haswell/babl-0.1/gimp-8bit.so
/usr/lib64/haswell/babl-0.1/grey.so
/usr/lib64/haswell/babl-0.1/naive-CMYK.so
/usr/lib64/haswell/babl-0.1/simple.so
/usr/lib64/haswell/babl-0.1/sse-half.so
/usr/lib64/haswell/babl-0.1/sse2-float.so
/usr/lib64/haswell/babl-0.1/sse2-int16.so
/usr/lib64/haswell/babl-0.1/sse2-int8.so
/usr/lib64/haswell/babl-0.1/sse4-int8.so
/usr/lib64/haswell/babl-0.1/two-table.so
/usr/lib64/haswell/babl-0.1/ycbcr.so
/usr/lib64/haswell/libbabl-0.1.so.0
/usr/lib64/haswell/libbabl-0.1.so.0.129.1
/usr/lib64/libbabl-0.1.so.0
/usr/lib64/libbabl-0.1.so.0.129.1
