Summary:	Cryptopp Library is a free C++ class library of cryptographic schemes.	
Summary(pl): 	Cryptopp jest klas± C++ dostarczaj±c± narzêdzia do kryptografii. 	
Name:		cryptopp	
Version:	5.1	
Release:	0.1	
License:	GPL
Vendor:		Wei Dai
Group:		Libraries	
Source0:	http://dl.sourceforge.net/sourceforge/cryptopp/crypto51.zip	
# Source0-md5:	f4bfd4ac39dc1b7f0764d61a1ec4df16
Patch: 		crypto-5.1.patch.bz2
URL:		http://www.cryptopp.com	
BuildRequires:	gcc-c++	
BuildRequires: 	unzip 
Requires:	gcc-c++	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cryptopp Library is a free C++ class library of cryptographic schemes.

%description -l pl
Cryptopp jest klas± C++ dostarczaj±c± narzêdzia do kryptografii.


%package devel
Summary: 	Files for development of applications which will use Cryptopp.  
Summary(pl): 	Files for development of applications which will use Cryptopp.
Group: 		Libraries

%description devel
Cryptopp Library is a free C++ class library of cryptographic schemes

%description devel -l pl
Cryptopp jest klas± C++ dostarczaj±c± narzêdzia do kryptografii.

%package progs 
Summary: 	Files for development of applications which will use Crypto++
Summary(pl): 	Files for development of applications which will use Crypto++
Group: 		Libraries

%description progs 
Cryptopp Library is a free C++ class library of cryptographic schemes

%description progs -l pl
Cryptopp jest klas± C++ dostarczaj±c± narzêdzia do kryptografii.


%prep
%setup -c -n %{name}-%{version}
%patch -p1 -b .autotools
chmod 755 configure

%build
%configure
%{__make}

%install
%{__rm} -rf %{buildroot}
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_includedir}/cryptopp
install -d $RPM_BUILD_ROOT%{_datadir}/cryptopp

cp .libs/cryptest	$RPM_BUILD_ROOT%{_bindir}
cp .libs/libcryptopp.so*  $RPM_BUILD_ROOT%{_libdir}
cp .libs/libcryptopp.a  $RPM_BUILD_ROOT%{_libdir}
cp *.h	$RPM_BUILD_ROOT%{_includedir}/cryptopp
cp *.dat  $RPM_BUILD_ROOT%{_datadir}/cryptopp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0755)
%doc License.txt Readme.txt
%{_libdir}/libcryptopp.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/cryptopp/*.h
%{_libdir}/*.a
%{_libdir}/*.so

%files progs
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/cryptopp/*.dat
