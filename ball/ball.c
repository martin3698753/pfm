#define DIM 4 //Dimenze
#define PI 3.141592653589793
#define RAD 1 //Poloměr koule

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double rnd(double rad)
{
  return ((double)rand() / (double)(RAND_MAX)) * rad;
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
  double nball = 0;

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
double vol_mean(int n, double vol[n])
{
  double vol_mean = 0;
  for(int i = 0; i < n; i++){
    vol_mean += vol[i];
  }
  return (vol_mean/n);
}
double sigma(int n, double vol[n], double mean)
{
  double a = 0;
  double b = (double)(n*(n-1));
  for(int i = 0; i < n; i++) {
    a += pow( (vol[i] - mean), 2 );
  }
  return sqrt(a/b);
}

int main()
{
  unsigned int n = 100;
  unsigned int N = 1000000;
  unsigned int seed = (unsigned int)time(NULL);
  time_t walltime;
  srand(seed);
  double vol[n];
  for(int i = 0; i < n; i++) {
    vol[i] = comp_vol(N);
    printf("vol[%d] = %lf\n", i, vol[i]);
  }
  double mean = vol_mean(n, vol);
  double sig = sigma(n, vol, mean);
  printf("-------------------------------------\n");
  printf("Theoretical val = %lf\n", volume());
  printf("mean = %lf\n", mean);
  printf("sigma = %lf\n", sig);
  printf("-------------------------------------\n");

  //printf("%Computed volume = lf\n", (nball*8)/N);
  //printf("Actual volume = %lf\n", volume(3, 1));
  return 0;
}
