%define upstream_name    Dist-Zilla-Plugin-PodLoom
Name:		perl-%{upstream_name}
Version:	3.00
Release:	6

Summary:	Process module documentation through Pod::Loom
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Dist::Zilla::Role::ModuleInfo)
BuildRequires:	perl(Hash::Merge::Simple)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Pod::Loom)
BuildArch:	noarch

%description
If included, this plugin will process each _.pm_ and _.pod_ file under
_lib_ or in the root directory through Pod::Loom.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes META.yml LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*

