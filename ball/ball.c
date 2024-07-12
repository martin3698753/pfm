#define DIM 3 //int of fail
#define PI 3.14159
#define RAD 1

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double rnd(double rad)
{
  return ((double)rand() / (double)(RAND_MAX)) * rad;
}
double square_area(double r)
{
  return (r*2);
}
double volume(int dim, double rad)
{
  return ((pow(PI, dim/2)*pow(rad, dim))/tgamma((dim/2)+1));
}

int main()
{
  unsigned int n = 1;
  unsigned int N = 1000000;
  double r;
  double nball;
  unsigned int seed = (unsigned int)time(NULL);
  time_t walltime;
  srand(seed);

  for(int i = 0; i < N; i++) {
    r = 0;
    for(int j = 0; j < DIM; j++) {
      r += pow(rnd(1), 2);
    }
    if(r <= 1) {
      nball++;
    }
  }
  printf("%lf\n", (nball*8)/N);
  printf("%lf\n", volume(3, 1));
  return 0;
}
