%define upstream_name    Dist-Zilla-Plugin-PodLoom
%define upstream_version 3.00

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Process module documentation through Pod::Loom
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Dist::Zilla)
BuildRequires: perl(Dist::Zilla::Role::ModuleInfo)
BuildRequires: perl(Hash::Merge::Simple)
BuildRequires: perl(Moose)
BuildRequires: perl(Pod::Loom)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
If included, this plugin will process each _.pm_ and _.pod_ file under
_lib_ or in the root directory through Pod::Loom.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes META.yml LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*


