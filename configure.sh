#!/bin/bash

mkdir -p build
pushd build

conan workspace install ../workspace.yml \
    -l ../conanfile.ttlock \
    -s build_type=Release \
    -s test_project:build_type=Debug \
    -pr test_profile \
    --build=outdated \
    || { echo 'conan workspace failed' ; exit 1; }

popd
cmake -GNinja -H. -Bbuild -DCMAKE_BUILD_TYPE=Debug