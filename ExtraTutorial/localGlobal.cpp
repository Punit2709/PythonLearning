#include<iostream>
int variable = 10;

void fun1()
{
    int variable = 20;
    std::cout << "local : " << variable  << std::endl;
    std::cout << "global : " << ::variable << std::endl ; // :: ---> use for access global variable with same name as local
}

int main()
{
    fun1();
    return 0;
}

