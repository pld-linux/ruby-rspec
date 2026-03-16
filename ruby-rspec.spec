%define	pkgname rspec
Summary:	Behaviour driven development (BDD) framework for Ruby
Summary(pl.UTF-8):	Szkielet do programowania sterowanego zachowaniem (BDD) dla języka Ruby
Name:		ruby-%{pkgname}
Version:	3.13.2
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	f0704eee8cb7df927c007d61b5e71c3e
URL:		http://rspec.info/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RSpec is a behaviour driven development (BDD) framework for Ruby.

%description -l pl.UTF-8
RSpec to szkielet do programowania sterowanego zachowaniem (BDD -
Behaviour Driven Development) dla języka Ruby.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.md
%{ruby_vendorlibdir}/rspec.rb
%{ruby_vendorlibdir}/rspec/version.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
