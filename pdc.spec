%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%define srcname pdc

Name:           python-%{srcname}
Version:        0.1.0
Release:        alpha.3%{?dist}
Summary:        Red Hat Product Definition Center
Group:          Development/Libraries
License:        MIT
URL:            https://github.com/release-engineering/product-definition-center
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx
Requires:       python-requests
Requires:       python-requests-kerberos
Requires:       beanbag

%description
The Product Definition Center, at its core, is a database that defines every Red Hat products, and their relationships with several important entities.


%package -n %{srcname}-server
Summary: Product Definition Center (PDC) server part
Requires:       Django >= 1.8.1
Requires:       django-rest-framework >= 3.1
Requires:       django-rest-framework < 3.2
Requires:       django-mptt >= 0.7.1
Requires:       kobo >= 0.4.2
Requires:       kobo-django
Requires:       kobo-rpmlib
Requires:       koji
Requires:       patternfly1
Requires:       productmd
Requires:       python-django-filter >= 0.9.2
Requires:       python-ldap
Requires:       python-markdown
Requires:       python-mock
Requires:       python-psycopg2
Requires:       python-requests
Requires:       python-requests-kerberos
Requires:       python-django-cors-headers

%description -n %{srcname}-server
This package contains server part of Product Definition Center (PDC)

%prep
%setup -q -n %{name}-%{version}

%build
make -C docs/ html

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --root=%{buildroot}


mkdir -p %{buildroot}/%{_datadir}/%{srcname}/static
mkdir -p %{buildroot}%{_defaultdocdir}/%{srcname}
cp pdc/settings_local.py.dist %{buildroot}/%{python_sitelib}/%{srcname}
cp -R docs %{buildroot}%{_defaultdocdir}/%{srcname}
cp manage.py %{buildroot}/%{python_sitelib}/%{srcname}


# don't need egg info
for egg_info in $(find %{buildroot}/%{python_sitelib} -type d -name '*.egg-info'); do
  rm -rf $egg_info
done

# Install apache config for the app:
install -m 0644 -D -p conf/pdc-httpd.conf.sample %{buildroot}%{_defaultdocdir}/pdc/pdc.conf.sample

# only remove static dir when it's a uninstallation
# $1 == 0: uninstallation
# $1 == 1: upgrade
%preun
if [ "$1" = 0 ]; then
  rm -rf %{_datadir}/%{srcname}/static
fi


%files -n %{srcname}-server
%defattr(-,root,apache,-)
%{_defaultdocdir}/pdc
%{python_sitelib}/%{srcname}
%{python_sitelib}/contrib
%{python_sitelib}/%{srcname}
%exclude %{python_sitelib}/%{srcname}/conf
%{_datadir}/%{srcname}


%changelog
* Thu Aug 27 2015 Xiangyang Chu <xchu@redhat.com> 0.1.0-alpha.3
- new package built with tito

* Thu Aug 27 2015 Xiangyang Chu <xchu@redhat.com> 0.1.0-alpha.2
- Use release tagger. (xchu@redhat.com)
- init spec for copr build
