#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <Python.h>

/**
 * print_python_list - Print info about python lists
 *
 * @p: PyObject
 *
 */
void print_python_list(PyObject *p)
{
    int i, size;
    PyObject *element;

    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_GET_SIZE(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        element = PyList_GET_ITEM(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(element)->tp_name);
        if (PyBytes_Check(element))
            print_python_bytes(element);
        if (PyFloat_Check(element))
            print_python_float(element);
    }
}

/**
 * print_python_bytes - Print info about python bytes
 *
 * @p: PyObject
 *
 */
void print_python_bytes(PyObject *p)
{
    ssize_t i, size;
    char *string = NULL;

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);
    for (i = 0; i < size && i < 10; i++)
        printf("%02x%c", (unsigned char)string[i], i + 1 == 10 || i + 1 == size ? '\n' : ' ');
}

/**
 * print_python_float - Print info about python float
 *
 * @p: PyObject
 *
 */
void print_python_float(PyObject *p)
{
    char *string = NULL;
    double value = ((PyFloatObject *)p)->ob_fval;

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

    printf("[.] float object info\n");
    printf("  value: %s\n", string);
    PyMem_Free(string);
}
