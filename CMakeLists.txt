cmake_minimum_required(VERSION 3.10)

project(PCSX2_Memcard_Manager VERSION 2.0.0)

# Compile Switch

set(TEST_PROGRESS     OFF)
set(PACK_SETUP_GUI    OFF)

# end of Compile Switch

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
set(LIBRARY_OUTPUT_PATH    ${PROJECT_SOURCE_DIR}/bin)
# in this project, only dll is been created

set(LOGO_RC ${PROJECT_SOURCE_DIR}/ico/logo.rc)
set(CREATECONFIG_MAIN ${PROJECT_SOURCE_DIR}/cc.cpp)
# Create Config.cpp
# =      =

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

add_library(fextension SHARED
    ${FILEEXT_SRC}
)

add_executable(p2mm_shell
    ${SHELL_MAIN}
    ${LOGO_RC}
)

add_executable(p2mm_cc
    ${CREATECONFIG_MAIN}
)

target_link_libraries(fextension
    renaini
)

target_link_libraries(p2mm_shell
    shellextension
    formatextension
)

target_link_libraries(p2mm_cc
    fextension
)

if(${TEST_PROGRESS})

add_executable(test test.cpp)

target_link_libraries(test
    renaini
)

endif()

if(${PACK_SETUP_GUI})

execute_process(COMMAND pyinstaller setup.spec
                WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/gui/setup)   

file(COPY 
        ${PROJECT_SOURCE_DIR}/gui/setup/dist/p2mm_setuphelper.exe
        ${PROJECT_SOURCE_DIR}/gui/setup/setup.ico
     DESTINATION 
        ${PROJECT_SOURCE_DIR}/bin
)

endif()