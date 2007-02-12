%define		_orig_name	cryptopp
%define		_orig_ver	521
Summary:	Cryptopp Library - a free C++ class library of cryptographic schemes
Summary(pl.UTF-8):	Cryptopp - klasa C++ dostarczająca narzędzia do kryptografii
Name:		cryptopp
Version:	5.2.1
Release:	0.1
License:	GPL
Vendor:		Wei Dai
Group:		Libraries
Source0:	http://dl.sourceforge.net/%{name}/%{_orig_name}%{_orig_ver}.zip
# Source0-md5:	82a00c44235ccbae2bedf9cb16c40ac3
Patch0:		crypto-5.2.patch.bz2
URL:		http://www.cryptopp.com/
BuildRequires:	libstdc++-devel
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
chmod 755 configure

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_includedir}/cryptopp
install -d $RPM_BUILD_ROOT%{_datadir}/cryptopp

install .libs/cryptest	$RPM_BUILD_ROOT%{_bindir}
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
