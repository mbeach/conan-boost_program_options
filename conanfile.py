from conans import ConanFile, tools, os

class BoostProgram_OptionsConan(ConanFile):
    name = "Boost.Program_Options"
    version = "1.64.0"
    generators = "boost" 
    settings = "os", "arch", "compiler", "build_type"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-program_options"
    source_url = "https://github.com/boostorg/program_options"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["program_options"]
    build_requires = "Boost.Generator/0.0.1@bincrafters/testing" 
    requires =  "Boost.Any/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Detail/1.64.0@bincrafters/testing", \
                      "Boost.Function/1.64.0@bincrafters/testing", \
                      "Boost.Iterator/1.64.0@bincrafters/testing", \
                      "Boost.Lexical_Cast/1.64.0@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.Throw_Exception/1.64.0@bincrafters/testing", \
                      "Boost.Tokenizer/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing"

                      #any6 config0 core2 detail5 function5 iterator5 lexical_cast8 smart_ptr4 static_assert1 throw_exception2 type_traits3

    def source(self):
        for lib_short_name in self.lib_short_names:
            self.run("git clone --depth=1 --branch=boost-{0} https://github.com/boostorg/{1}.git"
                     .format(self.version, lib_short_name)) 

    def build(self):
        self.run(self.deps_user_info['Boost.Generator'].b2_command)
        
    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

        self.copy(pattern="*", dst="lib", src="stage/lib")

    def package_info(self):
        self.user_info.lib_short_names = (",").join(self.lib_short_names)
        self.cpp_info.libs = self.collect_libs()
