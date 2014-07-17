%define	gem_name rspec
Summary:	Behaviour driven development (BDD) framework for Ruby
Name:		ruby-%{gem_name}
Version:	2.13.0
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{gem_name}-%{version}.gem
# Source0-md5:	72bb51053e955418b9e06818729ab164
URL:		http://rspec.info/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	ruby-rspec-core >= %{version}
Requires:	ruby-rspec-expectations >= %{version}
Requires:	ruby-rspec-mocks >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RSpec is a behaviour driven development (BDD) framework for Ruby.

%prep
%setup -q -n %{gem_name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md License.txt
%{ruby_vendorlibdir}/rspec.rb
%{ruby_vendorlibdir}/rspec
