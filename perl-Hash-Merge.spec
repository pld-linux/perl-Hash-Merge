#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Hash
%define		pnam	Merge
Summary:	Hash::Merge - merges arbitrarily deep hashes into a single hash
Summary(pl.UTF-8):	Hash::Merge - moduł Perla służący do łączenia tablic asocjacyjnych w jedną
Name:		perl-Hash-Merge
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Hash/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	875e2d9101bde2f6b410dd12f7e10964
URL:		http://search.cpan.org/dist/Hash-Merge/
BuildRequires:	perl-Clone
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hash::Merge merges two arbitrarily deep hashes into a single hash.
That is, at any level, it will add non-conflicting key-value pairs
from one hash to the other, and follows a set of specific rules
when there are key value conflicts. The hash is followed recursively,
so that deeply nested hashes that are at the same level will be merged
when the parent hashes are merged. Please note that self-referencing
hashes, or recursive references, are not handled well by this method.

%description -l pl.UTF-8
Hash::Merge jest modułem Perla służącym do łączenia dwóch dowolnie
głęboko zagnieżdżonych tablic asocjacyjnych w jedną. Oznacza to, że
do dowolnego poziomu będzie dodawał niekonfliktujące pary
klucz-wartość z jednego hasza do drugiego i postępował zgodnie ze
zbiorem konkretnych reguł w przypadku konfliktu. Tablica asocjacyjna
jest śledzona rekurencyjnie, więc głęboko zagnieżdżone tablice będące
na tym samym poziomie zostaną połączone przy łączeniu tablic przodków.
Należy zauważyć, że samoodwołujące się hasze oraz referencje
rekurencyjne nie są dobrze obsługiwane przez tę metodę.

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
