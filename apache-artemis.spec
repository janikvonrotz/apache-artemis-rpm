##### HEADER SECTION #####

Name:           apache-artemis
Version:        @ARTEMIS_VERSION@
Release:        1
Summary:        Rpm package for Apache ActiveMQ Artemis

License:        ASL 2.0
URL:            http://activemq.apache.org/artemis/
Source0:        %{name}-%{version}-bin.tar.gz

Requires:       shadow-utils,bash

BuildArch:      x86_64

%description
%{summary}

# disable debuginfo, which is useless on binary-only packages
%define debug_package %{nil}

##### PREPARATION SECTION #####
%prep

# unpack tarball
%setup -q

##### BUILD SECTION #####
%build

# empty section

##### PREINSTALL SECTION #####
%pre

# create Apache Artemis service group
getent group artemis >/dev/null || groupadd -f -g 30101 -r artemis

# create Apache Artemis service user
if ! getent passwd artemis >/dev/null ; then
    if ! getent passwd 30101 >/dev/null ; then
      useradd -r -u 30101 -g artemis -d /home/artemis -s /sbin/nologin -c "Apache Artemis service account" artemis
    else
      useradd -r -g artemis -d /home/artemis -s /sbin/nologin -c "Apache Artemis service account" artemis
    fi
fi
exit 0

##### INSTALL SECTION #####
%install

app_dir=%{buildroot}/opt/icamapp/artemis
data_dir=%{buildroot}/opt/icamdata/artemis

# cleanup build root
rm -rf %{buildroot}
mkdir -p  %{buildroot}

# create app folder
mkdir -p $app_dir

# create data folder
mkdir -p $data_dir

# copy all files
cp LICENSE $app_dir
cp README.html $app_dir
cp -R bin $app_dir
cp -R lib $app_dir
cp -R schema $app_dir
cp -R web $app_dir

##### FILES SECTION #####
%files

# define default file attributes
%defattr(-,artemis,artemis,-)

# list of directories that are packaged
%dir /opt/icamapp/artemis
/opt/icamapp/artemis/bin/*
/opt/icamapp/artemis/lib/*
/opt/icamapp/artemis/schema/*
/opt/icamapp/artemis/web/*
%dir %attr(660, -, -) /opt/icamdata/artemis

# list of files that are packaged
%doc /opt/icamapp/artemis/README.html
%license /opt/icamapp/artemis/LICENSE

##### UNINSTALL SECTION #####
%postun

case "$1" in
	0) # This is a package remove

		# remove app and data folders
		rm -rf /opt/icamapp/artemis
    	rm -rf /opt/icamdata/artemis

		# remove Apache Artemis service user and group
  		userdel artemis
	;;
	1) # This is a package upgrade
  		# do nothing
	;;
esac

##### CHANGELOG SECTION #####
%changelog

* Wed Mar 20 2019 Janik vonRotz <contact@janikvonrotz.ch> - 2.6.4-1
- First apache-artemis package
