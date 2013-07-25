%define	upstream_name	 File-chdir
%define upstream_version 0.1008

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.1008
Release:	1

Summary:	A more sensible way to change directories
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/File-chdir-0.1008.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Perl's chdir() has the unfortunate problem of being very, very, very
global.  If any part of your program calls chdir() or if any library
you use calls chdir(), it changes the current working directory for
the B<whole> program.

File::chdir gives you an alternative, $CWD and @CWD.  These two
variables combine all the power of C<chdir()>, File::Spec and Cwd.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc Changes
%dir %{perl_vendorlib}/File
%{perl_vendorlib}/File/*
%{_mandir}/*/*


%changelog
* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.400-1mdv2011.0
+ Revision: 552287
- update to 0.1004

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.200-1mdv2010.0
+ Revision: 395187
- fix wrong macro name
- update to 0.1002
- using %%perl_convert_version
- fixed license field

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.10-4mdv2009.0
+ Revision: 256873
- rebuild

* Mon Feb 11 2008 Thierry Vignaud <tv@mandriva.org> 0.10-2mdv2008.1
+ Revision: 165301
- fix description

* Sat Feb 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.1
+ Revision: 164629
- update to new version 0.10

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 06 2007 Funda Wang <fwang@mandriva.org> 0.09-1mdv2008.0
+ Revision: 59446
- New version 0.09

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2008.0
+ Revision: 48163
- spec cleanup
- update to new version 0.08


* Thu Feb 17 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.06-2mdk
- Make rpmlint happy

* Wed Jan 28 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.06-1mdk
- from Robin Rosenberg <robin.rosenberg@dewire.com> :
	- initial contrib import. Needed for building Captive-NTFS


