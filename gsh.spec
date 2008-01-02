%define name         	gsh	
%define version      	1.0.2
%define release		%mkrel 7

Name: 		%{name}
Version: 	%{version}
Release:	%{release} 
Summary: 	Run commands on other hosts through ssh
License: 	GPL
Group: 		Networking/Remote access
Url:		http://outflux.net/unix/software/gsh/
Source: 	%{name}-%{version}.tar.bz2
Requires:	openssh, openssh-clients, perl 
BuildRoot: 	%{_tmppath}/%{name}-%{version}
Prefix:		%{_prefix}
buildArch:	noarch

%description 
Run commands on other hosts through ssh

%prep
%setup -n %{name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

mkdir -p %{buildroot}/etc

cat > $RPM_BUILD_ROOT/etc/ghosts <<EOF
# Macros
#mdkprod=mdk82
# Machines
# Name		Group		Hardware	OS
#n1		prod		intel		linux
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc LICENSE MANIFEST README TODO
%attr(755,root,root) %{_bindir}/gsh
%attr(755,root,root) %{_bindir}/ghosts
%attr(755,root,root) %{perl_vendorlib}/*
%{_mandir}/man1/*
%config(noreplace) /etc/ghosts


