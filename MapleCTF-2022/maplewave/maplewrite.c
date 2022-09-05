#include <stdio.h>
#include <stdlib.h>
#include <pulse/simple.h>
#include <pulse/error.h>


// Pacat sample code: https://freedesktop.org/software/pulseaudio/doxygen/pacat-simple_8c-example.html
int main(int argc, char** argv)
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
 
    static const pa_sample_spec ss = {
        .format = PA_SAMPLE_U8,
        .rate = 44100 >> 2,
        .channels = 1
    };
    int error;
    pa_simple* s = pa_simple_new(NULL, argv[0], PA_STREAM_PLAYBACK, NULL, "playback", &ss, NULL, NULL, &error);

    if (!s)
    {
        puts("Failed to create PulseAudio connection!");
        return -1;
    }
    
    int increment = 8;
    for (int j = 0; j < i-8; j+=increment)
    {
        pa_simple_write(s,buffer+8+j,increment,&error);
    }
    pa_simple_drain(s, &error);
}