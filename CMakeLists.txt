cmake_minimum_required(VERSION 3.10)

project(PCSX2_Memcard_Manager VERSION 2.0.0)

set(TEST_PROGRESS OFF)

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
set(LIBRARY_OUTPUT_PATH    ${PROJECT_SOURCE_DIR}/bin)
# in this project, only dll is been created

set(LOGO_RC ${PROJECT_SOURCE_DIR}/ico/logo.rc)

include_directories(include)

add_subdirectory(shell)
add_subdirectory(src)

add_library(shellextension SHARED
    ${SHELL_SRC}
)

add_library(formatextension SHARED
    ${FORMAT_SRC}
)

add_library(renaini SHARED
    ${RENAINI_SRC}
)

add_executable(p2mm_shell
    ${SHELL_MAIN}
    ${LOGO_RC}
)

target_link_libraries(p2mm_shell
    shellextension
    formatextension
)

if(${TEST_PROGRESS})

add_executable(test test.cpp)

target_link_libraries(test
    renaini
)

endif()