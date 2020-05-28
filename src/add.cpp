#include <arithmetic/add.hpp>

#include <functional>

int add(int a, int b)
{
  // Most straightforward implementation
  return std::plus<int>{}(a, b);
}
