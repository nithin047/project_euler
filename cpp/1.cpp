#include <iostream>


int main()
{
    std::cout << "Enter max_num, the output will be the sum of all multiples of 3 or 5 less than max_num" << std::endl;

    int max_num, max_threes_multiple, max_fives_multiple, max_fifteens_multiple, three_five_multiple_sum;

    std::cin >> max_num;

    max_threes_multiple = (max_num-1)/3;
    max_fives_multiple = (max_num-1)/5;
    max_fifteens_multiple = (max_num-1)/15;

    three_five_multiple_sum = (3 * (max_threes_multiple * (max_threes_multiple + 1)) + 5 * (max_fives_multiple * (max_fives_multiple + 1)) - 15 * (max_fifteens_multiple * (max_fifteens_multiple + 1)))/2;

    std::cout << "Answer: " << three_five_multiple_sum << std::endl;

    return 0;
}
