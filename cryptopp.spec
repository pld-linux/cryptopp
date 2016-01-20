#
# Conditional build:
%bcond_without	asm		# disable x86 assembly code
%bcond_without	tests		# build without tests

%ifarch x32
%undefine	with_asm
%endif

%define		orig_ver	561
Summary:	Cryptopp Library - a free C++ class library of cryptographic schemes
Summary(pl.UTF-8):	Cryptopp - biblioteka klas C++ dostarczająca narzędzia do kryptografii
Name:		cryptopp
Version:	5.6.1
Release:	3
License:	BSD-like
Group:		Libraries
Source0:	http://downloads.sourceforge.net/cryptopp/%{name}%{orig_ver}.zip
# Source0-md5:	96cbeba0907562b077e26bcffb483828
Patch0:		%{name}-autotools.patch
Patch1:		cxx.patch
URL:		http://www.cryptopp.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	unzip
Obsoletes:	cryptopp-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cryptopp Library is a free C++ class library of cryptographic schemes.

%description -l pl.UTF-8
Cryptopp jest biblioteką klas C++ dostarczającą narzędzia do
kryptografii.

%package devel
Summary:	Files for development of applications which will use Cryptopp
Summary(pl.UTF-8):	Pliki do tworzenia aplikacji używających Cryptopp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Files for development of applications which will use Cryptopp.

%description devel -l pl.UTF-8
Pliki do tworzenia aplikacji używających Cryptopp.

%package static
Summary:	Static Cryptopp library
Summary(pl.UTF-8):	Statyczna biblioteka Cryptopp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Cryptopp library.

%description static -l pl.UTF-8
Statyczna biblioteka Cryptopp.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%if %{without asm}
CFLAGS="%{rpmcflags} -DCRYPTOPP_DISABLE_X86ASM"
CXXFLAGS="%{rpmcxxflags} -DCRYPTOPP_DISABLE_X86ASM"
%endif
%configure
%{__make}

%if %{with tests}
./cryptest v
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL="install -p -c " \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_bindir}/cryptest

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc License.txt Readme.txt
%attr(755,root,root) %{_libdir}/libcryptopp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcryptopp.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcryptopp.so
%{_libdir}/libcryptopp.la
%{_includedir}/cryptopp

%files static
%defattr(644,root,root,755)
%{_libdir}/libcryptopp.a
