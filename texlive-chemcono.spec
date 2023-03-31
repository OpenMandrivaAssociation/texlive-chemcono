Name:		texlive-chemcono
Version:	17119
Release:	2
Summary:	Support for compound numbers in chemistry documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chemcono
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcono.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcono.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
