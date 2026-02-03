#include <stdio.h>
int main(){
    char PROC[] = {'p1', 'p2', 'p3'};
    int AT = 0;
    int BT[] = {3,4,5};
    
    int n = sizeof(BT)/sizeof(BT[0]);
    int CT[n];
    int TAT[n];
    int WT[n];

for(int i = 0 ; i < n; i++){
    if (i == 0)
    CT[i] = BT[i];
    else
    CT[i] = CT[i-1] - BT[i];
    TAT[i] = CT[i] - AT;
    WT[i] = TAT[i] - BT[i];
    print("process %c : WT = %d, TAT = %d, BT = %d\n", PROC[i],WT[i],TAT[i],CT[i]);

}

return 0;
}
