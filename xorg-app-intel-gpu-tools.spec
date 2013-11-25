%define		rname	intel-gpu-tools

Summary:	Tools for Intel DRM driver
Name:		xorg-app-intel-gpu-tools
Version:	1.5
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{rname}-%{version}.tar.bz2
# Source0-md5:	6165a9054de2609f5b1bf0ca0d913f31
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdrm-devel
BuildRequires:	libpciaccess-devel
BuildRequires:	pkg-config
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of tools for development and testing of the Intel DRM driver.

%prep
%setup -qn %{rname}-%{version}

%{__sed} -i -e '1s,#!/usr/bin/env python3,#!/usr/bin/python3,' \
	tools/quick_dump/{quick_dump,reg_access}.py

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/I915ChipsetPython.so
%{_pkgconfigdir}/intel-gen4asm.pc
%{_mandir}/man1/*.1*

