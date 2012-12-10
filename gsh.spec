%define name         	gsh	
%define version      	1.0.2
%define release		11

Name: 		%{name}
Version: 	%{version}
Release:	%{release} 
Summary: 	Run commands on other hosts through ssh
License: 	GPL
Group: 		Networking/Remote access
Url:		http://outflux.net/unix/software/gsh/
Source0: 	%{name}-%{version}.tar.bz2
buildrequires:	perl-devel
Requires:	openssh, openssh-clients, perl 
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

%files
%defattr (-,root,root)
%doc LICENSE MANIFEST README TODO
%attr(755,root,root) %{_bindir}/gsh
%attr(755,root,root) %{_bindir}/ghosts
%attr(755,root,root) %{perl_vendorlib}/*
%{_mandir}/man1/*
%config(noreplace) /etc/ghosts




%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1.0.2-11mdv2011.0
+ Revision: 653382
- rebuild for updated spec-helper

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0.2-10mdv2011.0
+ Revision: 429328
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-9mdv2009.0
+ Revision: 246658
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.2-7mdv2008.1
+ Revision: 140742
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 02 2007 Antoine Ginies <aginies@mandriva.com> 1.0.2-7mdv2007.0
+ Revision: 131000
- Import gsh

* Tue Aug 08 2006 Antoine Ginies <aginies@mandriva.com> 1.0.2-7mdv2007.0
- release 1.0.2
- use mkrel
- add man pages
- use perl macro

* Mon Feb 07 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.9.0-6mdk
- fix sysadmin.pl location
- cleanup

* Sat Feb 05 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.9.0-5mdk
- rebuild for new perl

* Tue May 18 2004 Antoine Ginies <aginies@n2.mandrakesoft.com> 0.9.0-4mdk
- rebuild
- rpmlint fix

