#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Parse
%define	pnam	Dia-SQL
Summary:	Parse::Dia::SQL - Convert Dia class diagrams into SQL
#Summary(pl.UTF-8):	
Name:		perl-Parse-Dia-SQL
Version:	0.20
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/A/AF/AFF/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6aed27ee22c012ccb47a211465432cac
URL:		http://search.cpan.org/dist/Parse-Dia-SQL/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Log-Log4perl
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Text-Table
BuildRequires:	perl-XML-DOM
BuildRequires:	perl-XML-Parser
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parse::Dia::SQL converts Dia class diagrams into SQL.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc AUTHORS Changes README TODO
%{perl_vendorlib}/Parse/Dia
%{_mandir}/man?/*
