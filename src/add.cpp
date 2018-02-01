#include <arithmetic/add.hpp>

#include <functional>

int add(int a, int b) noexcept
{
  // Most straightforward implementation
  return std::plus<>{}(a, b);
}
