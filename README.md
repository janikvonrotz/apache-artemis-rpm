# Apache Artemis RPM

Build an rpm for Apache Artemis from tarball.

Blog post: [Janik von Rotz - The final rpm packaging guide](https://janikvonrotz.ch/2019/03/20/the-final-rpm-packaging-guide/)

## Requirements

[rpmbuild](https://rpm.org/) - Utility to build rpms.

`sudo yum install rpm-build`

## Gradle Tasks

**createRpmbuildFolders**  
Creates the rpmbuild folder structure.

**copyRpmbuild**  
Copies spec and build script into build folder.

**rpmBuild**  
Runs the rpm build.

**rpmDist**  
Copies rpm file into distribution folder.
