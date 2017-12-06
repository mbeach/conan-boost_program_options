from conans import ConanFile, tools


class BoostProgram_OptionsConan(ConanFile):
    name = "Boost.Program_Options"
    version = "1.65.1"

    options = {"shared": [True, False]}
    default_options = "shared=False"

    requires = \
        "Boost.Generator/1.65.1@bincrafters/testing", \
        "Boost.Any/1.65.1@bincrafters/testing", \
        "Boost.Config/1.65.1@bincrafters/testing", \
        "Boost.Core/1.65.1@bincrafters/testing", \
        "Boost.Detail/1.65.1@bincrafters/testing", \
        "Boost.Function/1.65.1@bincrafters/testing", \
        "Boost.Iterator/1.65.1@bincrafters/testing", \
        "Boost.Lexical_Cast/1.65.1@bincrafters/testing", \
        "Boost.Smart_Ptr/1.65.1@bincrafters/testing", \
        "Boost.Static_Assert/1.65.1@bincrafters/testing", \
        "Boost.Throw_Exception/1.65.1@bincrafters/testing", \
        "Boost.Tokenizer/1.65.1@bincrafters/testing", \
        "Boost.Type_Traits/1.65.1@bincrafters/testing"

    lib_short_names = ["program_options"]
    is_header_only = False

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost-program_options"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1"
    license = "www.boost.org/users/license.html"
    short_paths = True
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"

    @property
    def env(self):
        try:
            with tools.pythonpath(super(self.__class__, self)):
                import boostgenerator  # pylint: disable=F0401
                boostgenerator.BoostConanFile(self)
        except:
            pass
        return super(self.__class__, self).env

    # END
