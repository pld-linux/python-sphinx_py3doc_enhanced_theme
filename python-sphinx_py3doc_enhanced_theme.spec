#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Enhanced Sphinx theme (based on Python 3 docs)
Summary(pl.UTF-8):	Rozszerzony motyw dla Sphinksa (oparty na dokumentacji Pythona 3)
Name:		python-sphinx_py3doc_enhanced_theme
Version:	2.4.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/sphinx_py3doc_enhanced_theme
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx_py3doc_enhanced_theme/sphinx-py3doc-enhanced-theme-%{version}.tar.gz
# Source0-md5:	38af7b770835cca10a6034abdcc58989
URL:		https://github.com/ionelmc/sphinx-py3doc-enhanced-theme
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A theme based on the theme of https://docs.python.org/3/ with some
responsive enhancements.

%description -l pl.UTF-8
Motyw oparty na motywie https://docs.python.org/3/ z pewnymi
reagującymi rozszerzeniami.

%package -n python3-sphinx_py3doc_enhanced_theme
Summary:	Enhanced Sphinx theme (based on Python 3 docs)
Summary(pl.UTF-8):	Rozszerzony motyw dla Sphinksa (oparty na dokumentacji Pythona 3)
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-sphinx_py3doc_enhanced_theme
A theme based on the theme of https://docs.python.org/3/ with some
responsive enhancements.

%description -n python3-sphinx_py3doc_enhanced_theme -l pl.UTF-8
Motyw oparty na motywie https://docs.python.org/3/ z pewnymi
reagującymi rozszerzeniami.

%prep
%setup -q -n sphinx-py3doc-enhanced-theme-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.rst CHANGELOG.rst LICENSE README.rst
%{py_sitescriptdir}/sphinx_py3doc_enhanced_theme
%{py_sitescriptdir}/sphinx_py3doc_enhanced_theme-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sphinx_py3doc_enhanced_theme
%defattr(644,root,root,755)
%doc AUTHORS.rst CHANGELOG.rst LICENSE README.rst
%{py3_sitescriptdir}/sphinx_py3doc_enhanced_theme
%{py3_sitescriptdir}/sphinx_py3doc_enhanced_theme-%{version}-py*.egg-info
%endif
