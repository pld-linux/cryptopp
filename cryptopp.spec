%define		orig_ver	552
Summary:	Cryptopp Library - a free C++ class library of cryptographic schemes
Summary(pl.UTF-8):	Cryptopp - klasa C++ dostarczająca narzędzia do kryptografii
Name:		cryptopp
Version:	5.5.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/cryptopp/%{name}%{orig_ver}.zip
# Source0-md5:	a889be9d9ad5c202c925fb105caa4857
Patch0:		%{name}-autotools.patch
URL:		http://www.cryptopp.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cryptopp Library is a free C++ class library of cryptographic schemes.

%description -l pl.UTF-8
Cryptopp jest klasą C++ dostarczającą narzędzia do kryptografii.


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

%package progs
Summary:	Cryptopp programs
Summary(pl.UTF-8):	Programy dla Cryptopp
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description progs
Cryptopp programs.

%description progs -l pl.UTF-8
Programy dla Cryptopp.

%prep
%setup -q -c
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	CXXFLAGS="%{rpmcxxflags} -DCRYPTOPP_DISABLE_X86ASM"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_includedir}/cryptopp
install -d $RPM_BUILD_ROOT%{_datadir}/cryptopp

install .libs/cryptest	$RPM_BUILD_ROOT%{_bindir}/cryptest
cp -a .libs/libcryptopp.so*  $RPM_BUILD_ROOT%{_libdir}
install .libs/libcryptopp.a  $RPM_BUILD_ROOT%{_libdir}
install *.h	$RPM_BUILD_ROOT%{_includedir}/cryptopp
install *.dat  $RPM_BUILD_ROOT%{_datadir}/cryptopp

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc License.txt Readme.txt
%attr(755,root,root) %{_libdir}/libcryptopp.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcryptopp.so
%{_includedir}/cryptopp

%files static
%defattr(644,root,root,755)
%{_libdir}/libcryptopp.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/cryptopp
