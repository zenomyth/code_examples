#include <stdio.h>
#include <getopt.h>
#include <stdlib.h>
#include <stdbool.h>

int main(int argc, char *argv[])
{
    int c;
    static int flag_1 = 0;
    while (true) {
        static struct option long_options[] = {
            /* These options set a flag. */
            {"flag-1", no_argument, &flag_1, 77},
            /* These options don’t set a flag.
             We distinguish them by their indices. */
            {"option-1", no_argument, 0, '1'},
            {"option-2", required_argument, 0, '2'},
            {"option-3", no_argument, 0, 0},
            {0, 0, 0, 0}
        };
        /* getopt_long stores the option index here. */
        int option_index = 0;

        c = getopt_long(argc, argv, "12:",
                   long_options, &option_index);

        /* Detect the end of the options. */
        if (c == -1)
            break;

        switch (c) {
        case 0:
            /* If this option set a flag, do nothing else now. */
            if (long_options[option_index].flag != 0)
                break;
            printf("option %s", long_options[option_index].name);
            if (optarg)
                printf(" with arg %s", optarg);
            printf("\n");
            break;

        case '1':
        case '2':
            printf("option_index = %d\n", option_index);
            printf("option %c", c);
            if (optarg)
                printf(" with arg %s", optarg);
            printf("\n");
            break;

        case '?':
            /* getopt_long already printed an error message. */
            printf("Already error???\n");
            break;

        default:
            abort();
        }
    }

    if (flag_1 != 0)
        printf("flag_1 = %d\n", flag_1);

    return 0;
}
