#include <stdio.h>
#include <stdlib.h>
#include <pulse/simple.h>
#include <pulse/error.h>

int main()
{
    char *buffer = malloc(1 << 18);
    FILE* f = fopen("flag0.maplewave","rb");

    if (!f)
    {
        puts("FAILED TO OPEN FILE!!");
    }
    int ch = getc(f);
    int i = 0;
    while (ch != EOF && i != 1 << 18)
    {
        buffer[i++] = ch;
        ch = getc(f);
    }

    printf("%d bytes read!\n",i);
    int error;
    pa_simple* s = pa_simple_new(NULL, argv[0], PA_STREAM_PLAYBACK, NULL, "playback", &ss, NULL, NULL, &error);

    if (!s)
        puts("Failed to create PulseAudio connection!");
    
    pa_simple_write(s,buffer+8,i-8,i++);

    pa_simple_drain(s, &error);
}