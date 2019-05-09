#include <Python.h>
/**
 * print_python_list_info - prints the length of a Python list
 * @p: pointer to a PyObject
 */
void print_python_list_info(PyObject *p)
{
	size_t length = 0;

	length = PyList_Size(p);
	printf("[*] Size of the Python List = %lu\n", length);
}
