# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\QTwidgetsAPP_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\QTwidgetsAPP_autogen.dir\\ParseCache.txt"
  "QTwidgetsAPP_autogen"
  )
endif()
