add_library(ramulator-frontend OBJECT)
target_include_directories(ramulator-frontend PUBLIC ../../include)

target_sources(
  ramulator-frontend PRIVATE

  impl/memory_trace/loadstore_trace.cpp
  impl/memory_trace/readwrite_trace.cpp

  impl/processor/simpleO3/simpleO3.cpp
  impl/processor/simpleO3/core.cpp
  impl/processor/simpleO3/llc.cpp
  impl/processor/simpleO3/trace.cpp

  impl/processor/bhO3/bhO3.h
  impl/processor/bhO3/bhcore.h    impl/processor/bhO3/bhcore.cpp
  impl/processor/bhO3/bhllc.h     impl/processor/bhO3/bhllc.cpp

  impl/external_wrapper/gem5_frontend.cpp
)

target_link_libraries(
  ramulator
  PRIVATE
  ramulator-frontend
)