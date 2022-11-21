cmake_minimum_required(VERSION 3.10)

project(PCSX2_Memcard_Manager VERSION 2.0.0)

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
set(LIBRARY_OUTPUT_PATH    ${PROJECT_SOURCE_DIR}/bin)
# in this project, only dll is been created

add_subdirectory(shell)

add_executable(PCSX2_Memcard_Manager_Shell
    ${SHELL_SRC}
    ${SHELL_MAIN}
)