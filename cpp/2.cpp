#include <iostream>



int compute_even_fibonacci_sum(unsigned int max_limit){

    long int even_fibonacci_sum = 2;
    int F_1 = 1;
    int F_2 = 2;
    int F_3 = 0;

    while(F_3 <= max_limit){

        F_3 = F_2 + F_1;
        if (F_3 % 2 == 0){
            even_fibonacci_sum += F_3;
        }
        F_1 = F_2;
        F_2 = F_3;

    }

    return even_fibonacci_sum;


}


int main()
{
    int n;
    std::cin >> n;
    std::cout << compute_even_fibonacci_sum(n) << std::endl;

    return 0;
}