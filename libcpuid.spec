%global commit ee88463
%global snapshot .git20161023.%{commit}

Name:           libcpuid
Version:        0.4.0
Release:        1%{snapshot}%{?dist}
Summary:        A small C library for x87 CPU detection and feature extraction

License:        BSD
URL:            http://libcpuid.sourceforge.net

# git clone https://github.com/anrieff/libcpuid
# cd libcpuid
# libtoolize
# autoreconf --install
# ./configure
# make dist
Source0:        libcpuid-%{version}.tar.bz2

BuildRequires:  libtool
BuildRequires:  autoconf

%description
libcpuid is a small C library for x86 CPU detection and feature extraction.
Using it, you can:

    o get the processor vendor, model, brand string, code name, ...
    o get information about CPU features such as: number of cores or logical
    CPUs, cache sizes, CPU clock, ...
    o check if the processor implements a specific instruction set such as the
    SSE2, 3DNow!, ...
    o execute the CPUID and RDTSC instructions (portably!) ...
    o and have this all in your commercial application, without getting into
    trouble.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        -n cpuid_tool
Summary:        Command line interface to libcpuid

%description    -n cpuid_tool
This program provides a direct interface to libcpuid.


%prep
%setup -q


%build
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS ChangeLog Readme.md
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3*

%files -n cpuid_tool
%{_bindir}/*


%changelog
* Sun Oct 23 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.4.0-1.git20161023.ee88463
- Public release
