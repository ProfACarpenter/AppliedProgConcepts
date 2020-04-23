#include <iostream>
#include <cmath>

using namespace std;

const int size = 6;

double mean(double a[], int size){
	double total = 0;
	for(int i = 0; i < size - 1; i++){
		total += a[i];
	}
	return (double)(total/size);
}

double hmean(double a[], int size){
	double total = 0;
	for(int i = 0; i < size - 1; i++){
		total += 1/a[i];
	}
	return (double)(size/total);
}

double gmean(double a[], int size){
	double total = 0;
	for(int i = 0; i < size - 1; i++){
		total *= a[i];
	}
	return pow(total, size);
}

int main(){
	
	double array[size];
	for(int i = 0; i < size - 1; i++){
		cout << "Type a number: ";
		cin >> array[i];
		cout << endl;

	}
	cout << "Arithmetic: " << mean(array, size) << endl;
	cout << "Harmonic: " << hmean(array, size) << endl;
	cout << "Geometric: " << gmean(array, size) << endl;

	return 0; 
}