#include <graphics.h>
#include <stdlib.h>
#include <stdio.h>
#include <conio.h>

void main(void)
{

   /* request auto detection */
   int gdriver = DETECT, gmode, errorcode;

   /* initialize graphics and local variables */
   initgraph(&gdriver, &gmode, "C:\\TurboC3/BGI");

   /* move the C.P. to the center of the screen */
   moveto(0, 0);

   /* output text starting at the C.P. */
   outtext("Abdul Momin");

   getch();
   closegraph();

}

