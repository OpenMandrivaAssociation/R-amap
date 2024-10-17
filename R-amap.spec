%global packname  amap
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.8_7
Release:          3
Summary:          Another Multidimensional Analysis Package
Group:            Sciences/Mathematics
License:          GPL
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-7.tar.gz
Requires:         R-Biobase 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-Biobase 

%description
Tools for Clustering and Principal Component Analysis (With robusts
methods, and parallelized functions).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

#%check
#%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/exec
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/po


%changelog
* Mon Feb 20 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.8_7-1
+ Revision: 777816
- Import R-amap
- Import R-amap

