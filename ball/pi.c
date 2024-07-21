#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
  unsigned int seed = (unsigned int)time(NULL);
  int n = 100000;
  int ncircle = 0;
  time_t walltime;
  srand(seed);

  walltime = time(NULL);
  for(int i = 0; i < n; i++) {
    double x = rand()/(RAND_MAX+1.);
    double y = rand()/(RAND_MAX+1.);
    printf("%lf, %lf\n", x, y);
    if(x*x + y*y < 1) {
      ncircle++;
    }
  }
  walltime = time(NULL)-walltime;
  printf("Elapsed time: %ld\n", (long)walltime);
  printf("pi = %12.10f\n", ((double)4*ncircle)/n);
  return 0;
}
