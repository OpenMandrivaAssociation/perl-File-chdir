%define	module	File-chdir
%define	name	perl-%{module}
%define	version	0.10
%define	release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A more sensible way to change directories
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/File/%{module}-%{version}.tar.bz2
Buildrequires:	perl-devel
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Perl's chdir() has the unfortunate problem of being very, very, very
global.  If any part of your program calls chdir() or if any library
you use calls chdir(), it changes the current working directory for
the B<whole> program.

File::chdir gives you an alternative, $CWD and @CWD.  These two
variables combine all the power of C<chdir()>, File::Spec and Cwd.

%prep
%setup -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc Changes
%dir %{perl_vendorlib}/File
%{perl_vendorlib}/File/*
%{_mandir}/*/*

