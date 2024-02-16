import os

from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMake, CMakeToolchain


class RamulatorConan(ConanFile):
    name = "ramulator"
    version = "2.0.0"
    description = "A modern, modular, and extensible cycle-accurate DRAM simulator"
    url = "https://github.com/CMU-SAFARI/ramulator2"
    license = "MIT"

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "CMakeDeps"

    def requirements(self):
        self.requires("argparse/2.9")
        self.requires("fmt/10.2.1")
        self.requires("spdlog/1.12.0")
        self.requires("yaml-cpp/0.8.0")
        self.requires(self.tested_reference_str)

    exports_sources = (
        "CMakeLists.txt",
        "LICENSE",
        "README.md",
        "compose-dev.yaml",
        "conan.cmake",
        "example_config.yaml",
        "example_inst.trace",
        "ext/*",
        "include/*",
        "perf_comparison",
        "rh_study",
        "src/*",
        "test/*",
        "verilog_verification",
    )
    no_copy_source = True

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self, generator='Ninja')
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if not self.conf.get("tools.build:skip_test", default=False):
            self.run("ctest test")

    def test(self):
        if can_run(self):
            cmd = os.path.join(self.cpp.build.bindir, "example")
            self.run(cmd, env="conanrun")

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["ramulator"]
