#include <Python.h>
/**
  * print_python_list_info - print basic info about pyobject
  * @p: pointer to pyobject
  * Return: void
  */
void print_python_list_info(PyObject *p)
{
	int size, mem, x;
	PyObject *obj;

	size = PY_SIZE(p);
	mem = ((PyObject *)p)->allocated;

	printf("[*} Size of the Python List = %d\n", size);
	printf("[*} Allocated = %d\n", mem);

	for (x = 0, x < size; x++)
	{
		printf("Element %d: ", x);

		obj = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
