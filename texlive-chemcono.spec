# revision 17119
# category Package
# catalog-ctan /macros/latex/contrib/chemcono
# catalog-date 2010-02-21 19:20:01 +0100
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-chemcono
Version:	1.3
Release:	8
Summary:	Support for compound numbers in chemistry documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chemcono
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcono.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcono.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX package for using compound numbers in chemistry
documents. It works like \cite and the \thebibliography, using
\fcite and \theffbibliography instead. It allows compound names
in documents to be numbered and does not affect the normal
citation routines.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chemcono/chemcono.sty
%{_texmfdistdir}/tex/latex/chemcono/drftcono.sty
%{_texmfdistdir}/tex/latex/chemcono/showkeysff.sty
%doc %{_texmfdistdir}/doc/latex/chemcono/chemcono.pdf
%doc %{_texmfdistdir}/doc/latex/chemcono/chemcono.tex
%doc %{_texmfdistdir}/doc/latex/chemcono/example.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 750135
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 718040
- texlive-chemcono
- texlive-chemcono
- texlive-chemcono
- texlive-chemcono
- texlive-chemcono

