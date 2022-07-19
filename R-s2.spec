#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-s2
Version  : 1.1.0
Release  : 16
URL      : https://cran.r-project.org/src/contrib/s2_1.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/s2_1.1.0.tar.gz
Summary  : Spherical Geometry Operators Using the S2 Geometry Library
Group    : Development/Tools
License  : Apache-2.0
Requires: R-s2-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-wk
BuildRequires : R-Rcpp
BuildRequires : R-wk
BuildRequires : buildreq-R
BuildRequires : openssl-dev

%description
the sphere. High-performance constructors and exporters provide high compatibility
    with existing spatial packages, transformers construct new geometries from existing
    geometries, predicates provide a means to select geometries based on spatial 
    relationships, and accessors extract information about geometries.

%package lib
Summary: lib components for the R-s2 package.
Group: Libraries

%description lib
lib components for the R-s2 package.


%prep
%setup -q -c -n s2
cd %{_builddir}/s2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658190063

%install
export SOURCE_DATE_EPOCH=1658190063
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library s2
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library s2
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library s2
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc s2 || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/s2/DESCRIPTION
/usr/lib64/R/library/s2/INDEX
/usr/lib64/R/library/s2/Meta/Rd.rds
/usr/lib64/R/library/s2/Meta/data.rds
/usr/lib64/R/library/s2/Meta/features.rds
/usr/lib64/R/library/s2/Meta/hsearch.rds
/usr/lib64/R/library/s2/Meta/links.rds
/usr/lib64/R/library/s2/Meta/nsInfo.rds
/usr/lib64/R/library/s2/Meta/package.rds
/usr/lib64/R/library/s2/NAMESPACE
/usr/lib64/R/library/s2/NEWS.md
/usr/lib64/R/library/s2/R/s2
/usr/lib64/R/library/s2/R/s2.rdb
/usr/lib64/R/library/s2/R/s2.rdx
/usr/lib64/R/library/s2/data/Rdata.rdb
/usr/lib64/R/library/s2/data/Rdata.rds
/usr/lib64/R/library/s2/data/Rdata.rdx
/usr/lib64/R/library/s2/extdata/emptyfile
/usr/lib64/R/library/s2/help/AnIndex
/usr/lib64/R/library/s2/help/aliases.rds
/usr/lib64/R/library/s2/help/figures/rc300.png
/usr/lib64/R/library/s2/help/paths.rds
/usr/lib64/R/library/s2/help/s2.rdb
/usr/lib64/R/library/s2/help/s2.rdx
/usr/lib64/R/library/s2/html/00Index.html
/usr/lib64/R/library/s2/html/R.css
/usr/lib64/R/library/s2/tests/area.R
/usr/lib64/R/library/s2/tests/area.Rout
/usr/lib64/R/library/s2/tests/testthat.R
/usr/lib64/R/library/s2/tests/testthat/test-data.R
/usr/lib64/R/library/s2/tests/testthat/test-plot.R
/usr/lib64/R/library/s2/tests/testthat/test-s2-accessors.R
/usr/lib64/R/library/s2/tests/testthat/test-s2-bounds.R
/usr/lib64/R/library/s2/tests/testthat/test-s2-cell-union.R
/usr/lib64/R/library/s2/tests/testthat/test-s2-cell.R
/usr/lib64/R/library/s2/tests/testthat/test-s2-constructors-formatters.R
/usr/lib64/R/library/s2/tests/testthat/test-s2-earth.R
/usr/lib64/R/library/s2/tests/testthat/test-s2-geography.R
/usr/lib64/R/library/s2/tests/testthat/test-s2-lnglat.R
/usr/lib64/R/library/s2/tests/testthat/test-s2-matrix.R
/usr/lib64/R/library/s2/tests/testthat/test-s2-options.R
/usr/lib64/R/library/s2/tests/testthat/test-s2-point.R
/usr/lib64/R/library/s2/tests/testthat/test-s2-predicates.R
/usr/lib64/R/library/s2/tests/testthat/test-s2-transformers.R
/usr/lib64/R/library/s2/tests/testthat/test-utils.R
/usr/lib64/R/library/s2/tests/testthat/test-vctrs.R
/usr/lib64/R/library/s2/tests/testthat/test-wk-utils.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/s2/libs/s2.so
/usr/lib64/R/library/s2/libs/s2.so.avx2
/usr/lib64/R/library/s2/libs/s2.so.avx512
