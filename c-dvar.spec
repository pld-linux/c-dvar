Summary:	D-Bus Variant Type-System
Name:		c-dvar
Version:	1.1.0
Release:	1
License:	Apache 2.0 or LGPL v2.1+
Group:		Libraries
Source0:	https://github.com/c-util/c-dvar/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	18c8f2fb8357440a3b168b13ba39d303
URL:		https://c-util.github.io/c-dvar/
BuildRequires:	c-stdaux-devel >= 1.5.0
BuildRequires:	c-utf8-devel
BuildRequires:	meson >= 0.60.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The c-dvar project implements the D-Bus Variant Type-System. It is a
simple stream encoder and decoder, according to the D-Bus
Specification. It is a self-contained implementation centered around
the D-Bus Variant Type-System, suitable for any project handling
D-Bus.

%package devel
Summary:	Header files for c-dvar library
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for c-dvar library.

%package static
Summary:	Static c-dvar library
Group:		Development/Libraries
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static c-dvar library.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS.md README.md
%attr(755,root,root) %{_libdir}/libcdvar-1.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcdvar-1.so
%{_includedir}/c-dvar.h
%{_includedir}/c-dvar-type.h
%{_pkgconfigdir}/libcdvar-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcdvar-1.a
