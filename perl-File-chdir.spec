%define	upstream_name	 File-chdir

Name:		perl-%{upstream_name}
Version:	0.1011
Release:	2

Summary:	A more sensible way to change directories
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/File-chdir-%{version}.tar.gz
#Old
#Source0:	http://www.cpan.org/modules/by-module/File/File-chdir-%{version}.tar.gz

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
%autosetup -p1 -n %{upstream_name}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%install
%make_install

%files 
%doc Changes
%dir %{perl_vendorlib}/File
%{perl_vendorlib}/File/*
%{_mandir}/*/*
