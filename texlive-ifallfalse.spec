Name:		texlive-ifallfalse
Version:	60027
Release:	1
Summary:	Compare a string against a set of other strings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ifallfalse
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifallfalse.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifallfalse.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifallfalse.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows you to check whether a string is contained
within another set of strings, and perform an action if it is
not. This is done by using the allfalse environment and passing
in a string and an action to be performed if the string is not
contained in the set. Then, passing in a string to the \orcheck
macro inside the respective allfalse environment adds that to
the set of strings. This package does not work with the LuaTeX
engine.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/ifallfalse
%{_texmfdistdir}/tex/latex/ifallfalse
%doc %{_texmfdistdir}/doc/latex/ifallfalse

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
