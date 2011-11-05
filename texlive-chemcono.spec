# revision 17119
# category Package
# catalog-ctan /macros/latex/contrib/chemcono
# catalog-date 2010-02-21 19:20:01 +0100
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-chemcono
Version:	1.3
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A LaTeX package for using compound numbers in chemistry
documents. It works like \cite and the \thebibliography, using
\fcite and \theffbibliography instead. It allows compound names
in documents to be numbered and does not affect the normal
citation routines.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chemcono/chemcono.sty
%{_texmfdistdir}/tex/latex/chemcono/drftcono.sty
%{_texmfdistdir}/tex/latex/chemcono/showkeysff.sty
%doc %{_texmfdistdir}/doc/latex/chemcono/chemcono.pdf
%doc %{_texmfdistdir}/doc/latex/chemcono/chemcono.tex
%doc %{_texmfdistdir}/doc/latex/chemcono/example.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
