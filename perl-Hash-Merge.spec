#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Hash
%define	pnam	Merge
Summary:	Hash::Merge - Merges arbitrarily deep hashes into a single hash
Name:		perl-Hash-Merge
Version:	0.07
Release:	1
# as perl itself
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	74c9d9fa310f64411c7e933d4e283c22
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Clone
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hash::Merge merges two arbitrarily deep hashes into a single hash.
That is, at any level, it will add non-conflicting key-value pairs
from one hash to the other, and follows a set of specific rules
when there are key value conflicts (as outlined below). The hash 
is followed recursively, so that deeply nested hashes that are at
the same level will be merged when the parent hashes are merged.
Please note that self-referencing hashes, or recursive references,
are not handled well by this method.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Hash/Merge.pm
%{_mandir}/man3/*
