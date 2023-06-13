#include <Python.h>

/**
 * print_python_list_info - Function prints info about Python lists.
 * @p: A list.
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	int allc, sze, i;
	PyObject *obj;

	sze = Py_SIZE(p);
	allc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", sze);
	printf("[*] Allocated = %d\n", allc);

	for (i = 0; i < sze; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
