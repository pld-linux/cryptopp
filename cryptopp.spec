#
# Conditional build:
%bcond_without	tests	# testing
%bcond_with	sse2	# SSE2 instructions

%ifarch pentium4 %{x8664} x32
%define	with_sse2	1
%endif

Summary:	Cryptopp Library - a free C++ class library of cryptographic schemes
Summary(pl.UTF-8):	Cryptopp - biblioteka klas C++ dostarczająca narzędzia do kryptografii
Name:		cryptopp
Version:	8.8.0
%define	tag_ver	%(echo %{version} | tr . _)
Release:	1
License:	Boost v1.0 (BSD-like)
Group:		Libraries
#Source0Download: https://github.com/weidai11/cryptopp/releases
Source0:	https://github.com/weidai11/cryptopp/archive/CRYPTOPP_%{tag_ver}/%{name}-%{tag_ver}.tar.gz
# Source0-md5:	6e28c5b76ef8a843478b7b17adfd14e8
Source1:	%{name}.pc
URL:		https://cryptopp.com/
BuildRequires:	libstdc++-devel
BuildRequires:	unzip
%{?with_sse2:Requires:	cpuinfo(sse2)}
Obsoletes:	cryptopp-progs < 5.6
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
%setup -q -n %{name}-CRYPTOPP_%{tag_ver}

%build
CXXFLAGS="%{rpmcxxflags} %{!?with_sse2:-DCRYPTOPP_DISABLE_SSE2} %{?with_sse2:-msse2}" \
%{__make} shared static %{?with_tests:cryptest.exe} \
	CXX="%{__cxx}"

%if %{with tests}
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

install -d $RPM_BUILD_ROOT%{_pkgconfigdir}
sed -e "
	s|@PREFIX@|%{_prefix}|g
	s|@LIBDIR@|%{_libdir}|g
	s|@VERSION@|%{version}|g
" %{SOURCE1} > $RPM_BUILD_ROOT%{_pkgconfigdir}/cryptopp.pc

# tests
%{__rm} $RPM_BUILD_ROOT%{_bindir}/cryptest.exe
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/cryptopp/Test{Data,Vectors}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%triggerpostun -- cryptopp < 5.6.5
rm -f %{_libdir}/libcryptopp.so.5.6
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc License.txt Readme.txt
%attr(755,root,root) %{_libdir}/libcryptopp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcryptopp.so.8

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcryptopp.so
%{_includedir}/cryptopp
%{_pkgconfigdir}/cryptopp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcryptopp.a
