Name:		texlive-chktex
Version:	1.6.4
Release:	1
Summary:	Check for errors in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/chktex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chktex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chktex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-chktex.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The program reports typographic and other errors in LaTeX
documents. Filters are also provided for checking the LaTeX
parts of CWEB documents.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/deweb
%{_texmfdir}/chktex/chktexrc
%{_texmfdir}/scripts/chktex/deweb.pl
%doc %{_texmfdir}/doc/chktex/ChkTeX.pdf
%doc %{_mandir}/man1/chktex.1*
%doc %{_texmfdir}/doc/man/man1/chktex.man1.pdf
%doc %{_mandir}/man1/chkweb.1*
%doc %{_texmfdir}/doc/man/man1/chkweb.man1.pdf
%doc %{_mandir}/man1/deweb.1*
%doc %{_texmfdir}/doc/man/man1/deweb.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdir}/scripts/a2ping/deweb.pl deweb
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
