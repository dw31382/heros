# include <stdio.h>
int main() {
    int hold = 0;
    int i = 0;
    int status = 0;
    int lines[] = {199, 200, 208, 210, 200, 207, 240, 269, 260, 263};
    for (int x = 0; x < 10; x++) {
        if (x == 0) {
            status = 0;
        } else {
            if (lines[x] > hold) {
                status = 1;
                i++;
            } else if (lines[x] < hold) {
                status = -1;
            } else {
                status = 0;
            }
        }
        printf("%d (%d), ", lines[x], status);
        hold = lines[x];
    }
    printf("%d ", i);
    return 0;
}
