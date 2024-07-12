#define DIM 3 //int of fail
#define PI 3.141592653589793
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
double volume()
{
  double a = pow(PI, (double)DIM/2) * pow((double)RAD, (double)DIM);
  double b = tgamma( (double)DIM/2 + (double)1 );
  return ((double)(a/b));
}
double comp_vol(int N)
{
  double r;
  double nball;

  for(int i = 0; i < N; i++) {
    r = 0;
    for(int j = 0; j < DIM; j++) {
      r += pow(rnd(1), 2);
    }
    if(r <= RAD) {
      nball++;
    }
  }
  return (nball * pow(2, DIM))/N;
}

int main()
{
  unsigned int n = 1;
  unsigned int N = 1000000;
  unsigned int seed = (unsigned int)time(NULL);
  time_t walltime;
  srand(seed);
  //printf("%lf\n", pow(PI, (double)1/2));
  //printf("%lf\n", tgamma((double)1/2 + 1));
  printf("%lf\n", volume());
  printf("%lf\n", comp_vol(N));

  //printf("%Computed volume = lf\n", (nball*8)/N);
  //printf("Actual volume = %lf\n", volume(3, 1));
  return 0;
}
