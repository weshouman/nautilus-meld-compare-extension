# Use a base image with a suitable Debian or Ubuntu version
# python3-nautilus is available starting from bullseye
FROM debian:bullseye

# Install necessary build dependencies
# These can vary based on your specific package requirements
RUN apt-get update && apt-get install -y \
    devscripts \
    lintian \
    debhelper \
    dh-make \
    fakeroot

# Copy project files into the Docker container
# We use a build directory to hold both the source and the pkg
WORKDIR /build/source
COPY . /build/source/

# A less generic, yet meaningful dir naming would be as following
#WORKDIR /build/nautilus-meld-compare-extension
#COPY . /build/nautilus-meld-compare-extension/

# Set up a non-root user to build the package (recommended for debuild)
RUN useradd -ms /bin/bash builder
RUN chown -R builder:builder /build

USER builder

# Build and output files into the /pkg directory
# /pkg could be mounted to get the output of it
#CMD debuild -us -uc
CMD debuild -us -uc && mv ../*.deb ../*.dsc ../*.tar.xz ../*.buildinfo ../*.changes /pkg/
