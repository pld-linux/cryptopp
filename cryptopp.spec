#
# Conditional build:
%bcond_without	tests		# build without tests

Summary:	Cryptopp Library - a free C++ class library of cryptographic schemes
Summary(pl.UTF-8):	Cryptopp - biblioteka klas C++ dostarczająca narzędzia do kryptografii
Name:		cryptopp
Version:	5.6.5
%define	 f_ver	%(echo %{version} | tr -d .)
Release:	1
License:	Boost v1.0 (BSD-like)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/cryptopp/%{name}%{f_ver}.zip
# Source0-md5:	839aa27c70fa70037185ae7be8d8d24d
Source1:	%{name}.pc
Patch0:		%{name}-opt.patch
URL:		http://www.cryptopp.com/
BuildRequires:	libstdc++-devel
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

%build
CXXFLAGS="%{rpmcxxflags}" \
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
%attr(755,root,root) %ghost %{_libdir}/libcryptopp.so.5.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcryptopp.so
%{_includedir}/cryptopp
%{_pkgconfigdir}/cryptopp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcryptopp.a
