# Copyright (c) 2020 - 2021 TomTom N.V. All rights reserved.
#
# This software is the proprietary copyright of TomTom N.V. and its subsidiaries and may be
# used for internal evaluation purposes or commercial use strictly subject to separate
# licensee agreement between you and TomTom. If you are the licensee, you are only permitted
# to use this Software in accordance with the terms of your license agreement. If you are
# not the licensee, then you are not authorized to use this software in any manner and should
# immediately return it to TomTom N.V.

from conans import ConanFile, CMake, tools, python_requires
import os


class TestProject(ConanFile):
    name = "test_project"
    description = "Conan.io recipe for test project"
    generators = "cmake"

    settings = "os", "compiler", "build_type", "arch", "toolchain"

    options = {
        "shared": [True, False],
    }

    default_options = {
        "shared": True,
    }

    exports_sources = ["include/*", "src/*", "CMakeLists.txt"]

    def imports(self):
        self.copy(pattern="*.dylib*", dst="lib", src="lib")
        self.copy(pattern="*.so*", dst="lib", src="lib")

    def _fetch_env_vars(self, env_vars_names):
        result = {}
        for name in env_vars_names:
            value = tools.get_env(name)
            if value is not None:
                result[name] = value
        return result

    def _configure_cmake(self):
        cmake = CMake(self)

        cmake.definitions["CMAKE_EXPORT_COMPILE_COMMANDS"] = True
        cmake.definitions.update(
            self._fetch_env_vars(["TEST_LOGS_OUTPUT_DIRECTORY", "COVERAGE", "COVERAGE_REPORT_DIR"]))

        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()
        if not tools.cross_building(self.settings) and self.should_test:
            if self.settings.os == "Macos":
                lib_path = os.path.join(self.build_folder, "lib")
                prefix = "DYLD_LIBRARY_PATH={} ".format(lib_path)
            else:
                prefix = ""
            self.run("{}ctest -C {} --verbose --output-on-failure".format(prefix,
                                                                          self.settings.build_type),
                                                                          run_environment=True)

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = [self.name]
